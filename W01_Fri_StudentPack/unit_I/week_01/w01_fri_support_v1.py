"""Visible data-loading helpers for W01 Friday. No student answers are stored here."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import random
import shutil
import sys
import time
import uuid

SEED = 414
SEASON = 2021
CIRCUIT = 'monza'
URL = 'https://api.jolpi.ca/ergast/f1/2021/circuits/monza/results/'
RESULT_COLUMNS = ['season','round','circuit_id','driver_id','driver_number','constructor_id','grid','position','position_text','points','status']
LAP_COLUMNS = ['season','round','circuit_id','driver_number','lap_number','lap_time_s','compound','is_accurate']

def find_root(start=None):
    start = Path(start or Path.cwd()).resolve()
    for candidate in [start, *start.parents]:
        if (candidate / '.iit414w-root').is_file():
            return candidate
    raise RuntimeError('Project marker .iit414w-root not found. Open the full course folder, not the notebook alone. No output folder was created.')

def versions():
    result = {'python':sys.version.split()[0], 'seed':SEED, 'git_available':bool(shutil.which('git'))}
    for name in ['numpy','pandas','requests','fastf1']:
        try: result[name] = importlib.metadata.version(name)
        except importlib.metadata.PackageNotFoundError: result[name] = 'MISSING'
    return result

def require_pandas():
    try:
        import pandas as pd
        return pd
    except ImportError as exc:
        raise RuntimeError('pandas is missing in this kernel. Use the runbook dependency instructions or the written data dictionary with a partner. This device remains BLOCKED; do not claim successful execution.') from exc

def normalize_results(pages):
    pd = require_pandas()
    rows = []
    for page in pages:
        races = page['MRData']['RaceTable']['Races']
        for race in races:
            for r in race.get('Results', []):
                rows.append({'season':race['season'],'round':race['round'],
                  'circuit_id':race['Circuit']['circuitId'],
                  'driver_id':r['Driver']['driverId'],'driver_number':r.get('number'),
                  'constructor_id':r.get('Constructor',{}).get('constructorId'),
                  'grid':r.get('grid'),'position':r.get('position'),
                  'position_text':r.get('positionText'),'points':r.get('points'),
                  'status':r.get('status')})
    df = pd.DataFrame(rows, columns=RESULT_COLUMNS)
    for col in ['season','round','grid','position']:
        df[col] = pd.to_numeric(df[col], errors='raise').astype('Int64')
    df['points'] = pd.to_numeric(df['points'], errors='raise')
    for col in ['circuit_id','driver_id','driver_number','constructor_id','position_text','status']:
        df[col] = df[col].astype('string')
    return df

def fetch_jolpica(requester=None, pause=time.sleep):
    if requester is None:
        import requests
        requester = requests.get
    pages=[]; offset=0; target_total=None
    for _ in range(20):
        response = requester(URL, params={'limit':100,'offset':offset},
                             headers={'User-Agent':'IIT414W-Teaching/1.0'}, timeout=(5,20))
        if response.status_code == 429:
            raise RuntimeError('Jolpica returned HTTP 429. Stop requests and use the provided snapshot; do not repeatedly retry.')
        response.raise_for_status()
        payload=response.json(); meta=payload['MRData']
        total=int(meta['total']); actual_offset=int(meta['offset']); page_limit=int(meta['limit'])
        if total <= 0 or actual_offset != offset or page_limit <= 0:
            raise ValueError('Unexpected pagination metadata or empty endpoint.')
        if target_total is not None and total != target_total:
            raise ValueError('Endpoint total changed during pagination; retry later with a stable source.')
        target_total=total
        rows=sum(len(r.get('Results',[])) for r in meta['RaceTable']['Races'])
        if rows <= 0 or rows > page_limit:
            raise ValueError('Unexpected or empty page before completion.')
        pages.append(payload); offset += rows
        if offset == total:
            df=normalize_results(pages)
            if len(df)!=total or df.duplicated(['season','round','driver_id']).any():
                raise ValueError('Incomplete or duplicated result pages.')
            if set(df['season']) != {SEASON} or set(df['circuit_id']) != {CIRCUIT}:
                raise ValueError('Response is outside the requested teaching case.')
            return df, {'origin':'JOLPICA_HTTP','api_access_confirmed':True,'url':URL,'pages':len(pages),'total':total,'retrieved_utc':datetime.now(timezone.utc).isoformat()}
        if offset > total:
            raise ValueError('Received more results than declared.')
        pause(.35)
    raise RuntimeError('Pagination safety limit reached; no partial table accepted.')

def fetch_fastf1(root):
    import fastf1
    pd=require_pandas()
    cache=find_root(root) / 'data/cache/fastf1_w01'
    cache.mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(str(cache))
    session=fastf1.get_session(SEASON, 'Italy', 'R')
    session.load(laps=True, telemetry=False, weather=False, messages=False)
    if session.laps.empty:
        raise ValueError('FastF1 returned no laps.')
    raw=session.laps
    df=pd.DataFrame({'season':SEASON,'round':int(session.event['RoundNumber']),
                     'circuit_id':CIRCUIT,'driver_number':raw['DriverNumber'].astype('string'),
                     'lap_number':raw['LapNumber'].astype('Int64'),
                     'lap_time_s':raw['LapTime'].dt.total_seconds(),
                     'compound':raw['Compound'].astype('string'),
                     'is_accurate':raw['IsAccurate'].astype('boolean')})
    return df.reset_index(drop=True), {'origin':'FASTF1_SESSION','api_access_confirmed':'NOT VERIFIED: library may use cache',
        'provider':'FastF1','session':'2021 Italy R','retrieved_utc':datetime.now(timezone.utc).isoformat(),
        'telemetry_loaded':False,'weather_loaded':False}

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load_snapshot(root, name):
    pd=require_pandas(); base=find_root(root)/'data/samples/w01_fri_v1'
    info=json.loads((base/'snapshot_manifest_v1.json').read_text(encoding='utf-8'))
    entry=info['files'][name]; path=base/entry['file']
    if path.parent.resolve()!=base.resolve() or digest(path)!=entry['sha256']:
        raise ValueError('Snapshot path or SHA-256 check failed.')
    dtype={'driver_number':'string','driver_id':'string','position_text':'string','circuit_id':'string'}
    df=pd.read_csv(path, dtype=dtype)
    if df.empty: raise ValueError('Empty snapshot.')
    expected=RESULT_COLUMNS if name=='results' else LAP_COLUMNS
    if list(df.columns)!=expected: raise ValueError('Snapshot schema mismatch.')
    return df, {'origin':'PROVIDED_SNAPSHOT','api_access_confirmed':False,'file':entry['file'],
                'sha256':entry['sha256'],'original_source':entry['provenance']}

def synthetic(name):
    pd=require_pandas(); rng=random.Random(SEED)
    if name=='results':
        rows=[]
        for i in range(1,7):
            rows.append([2021,0,'synthetic_circuit',f'driver_{i:02}',str(i),f'team_{(i+1)//2}',
                         [2,1,4,0,6,5][i-1],i,str(i),float(7-i),'Synthetic status'])
        df=pd.DataFrame(rows,columns=RESULT_COLUMNS)
    else:
        rows=[[2021,0,'synthetic_circuit',str(i),lap,round(80+rng.uniform(0,5),3),'SYNTHETIC',True]
              for i in range(1,7) for lap in range(1,4)]
        rows[1][5]=None
        df=pd.DataFrame(rows,columns=LAP_COLUMNS)
    return df, {'origin':'SYNTHETIC','api_access_confirmed':False,'seed':SEED,
                'notice':'Invented teaching records. Not Monza results, not API data, not evidence of successful API access.'}

def load_table(root, name, mode='live'):
    if name not in {'results','laps'} or mode not in {'live','snapshot','synthetic'}:
        raise ValueError('Unknown table or mode.')
    root=find_root(root); failures=[]
    if mode=='live':
        try:
            result=fetch_jolpica() if name=='results' else fetch_fastf1(root)
            print(f'{name}: {result[1]["origin"]}')
            return result
        except Exception as exc:
            failures.append(type(exc).__name__)
            print(f'{name}: LIVE LOAD FAILED ({type(exc).__name__}). Trying the provided snapshot. Record this limitation.')
    if mode in {'live','snapshot'}:
        try:
            df, provenance=load_snapshot(root,name)
            provenance['previous_failures']=failures
            print(f'{name}: PROVIDED SNAPSHOT. No API access is demonstrated by this load.')
            return df,provenance
        except Exception as exc:
            failures.append(type(exc).__name__)
            print(f'{name}: SNAPSHOT UNAVAILABLE/INVALID ({type(exc).__name__}). Switching to labelled SYNTHETIC data.')
    df,provenance=synthetic(name); provenance['previous_failures']=failures
    print(f'{name}: SYNTHETIC teaching records. These are NOT real race results.')
    return df,provenance

def quality_checks(results,laps):
    pd=require_pandas(); rows=[]
    def add(name,ok,detail): rows.append({'check':name,'status':'PASS' if ok else 'FAIL','observed':str(detail)})
    key=['season','round','driver_id']
    add('Results are not empty',len(results)>0,len(results))
    dup=int(results.duplicated(key).sum()); add('Unique result keys',len(results)>0 and dup==0,dup)
    missing=int(results[key+['driver_number','grid','position']].isna().sum().sum())
    add('Critical result fields present',len(results)>0 and missing==0,missing)
    valid=results['grid'].notna() & results['position'].notna() & (results['grid']>=0) & (results['position']>=1)
    add('Nonnegative grid and positive classification',len(results)>0 and bool(valid.all()),int((~valid).sum()))
    dup_laps=int(laps.duplicated(['season','round','driver_number','lap_number']).sum())
    add('Nonempty laps with unique keys',len(laps)>0 and dup_laps==0,f'{len(laps)} rows; {dup_laps} duplicate keys')
    rows.append({'check':'Missing lap times','status':'REVIEW','observed':str(int(laps['lap_time_s'].isna().sum()))+'; investigate, do not automatically drop'})
    rows.append({'check':'Grid zero','status':'REVIEW','observed':str(int((results['grid']==0).sum()))+'; special/unspecified start encoding, not P0'})
    return pd.DataFrame(rows)

def export_evidence(root,results,laps,provenance,checks):
    root=find_root(root)
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')+'_'+uuid.uuid4().hex[:6]
    folder=root/'outputs'/f'w01_fri_{stamp}'
    folder.mkdir(parents=True,exist_ok=False)
    for name,df in [('results',results),('laps',laps),('checks',checks)]:
        df.to_csv(folder/f'{name}.csv',index=False)
    hashes={p.name:digest(p) for p in folder.glob('*.csv')}
    manifest={'session':'W01 Friday 2026-09-04','seed':SEED,'versions':versions(),
       'provenance':provenance,'files_sha256':hashes,'created_utc':datetime.now(timezone.utc).isoformat(),
       'student_interpretation':'NOT RECORDED BY AUTOMATION','student_restart_run_all':'NOT VERIFIED BY THIS CELL'}
    (folder/'run_manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('Saved evidence:',folder.relative_to(root).as_posix())
    return folder
