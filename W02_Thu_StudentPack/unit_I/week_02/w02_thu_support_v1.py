"""Portable, offline data checks for IIT414W W02. No network or installs."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import platform
import re
import uuid

import numpy as np
import pandas as pd

RANDOM_SEED = 414
KEYS = ['season', 'round', 'driver_id']
DATA_REL = Path('data/samples/w02_thu_v1')


def find_root(start=None):
    start = Path(start or Path.cwd()).resolve()
    for p in (start, *start.parents):
        if (p / '.iit414w-root').is_file():
            return p
    raise FileNotFoundError('Course root missing. Extract the complete ZIP, including .iit414w-root, and open it there.')


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verified_file(root, filename):
    directory = Path(root) / DATA_REL
    manifest_path = directory / 'snapshot_manifest_v1.json'
    if not manifest_path.is_file():
        raise FileNotFoundError('Data manifest missing. Extract the complete course package again.')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    records = [r for r in manifest['files'] if r['file'] == filename]
    if len(records) != 1:
        raise ValueError(f'Exactly one manifest record required: {filename}')
    p = directory / filename
    if not p.is_file():
        raise FileNotFoundError(f'Missing {filename}. Extract the full package; do not download a substitute silently.')
    if sha256(p) != records[0]['sha256']:
        raise ValueError(f'Hash mismatch: {filename}. Restore the original; do not edit the source snapshot.')
    return p, records[0]


def read_verified_csv(root, filename):
    path, meta = verified_file(root, filename)
    df = pd.read_csv(path, dtype={'driver_id':'string','constructor_id':'string','circuit_id':'string',
                                  'position_text':'string','status':'string'})
    if len(df) != meta['rows'] or list(df.columns) != meta['columns']:
        raise ValueError(f'Row count or schema differs from manifest: {filename}')
    return df


def time_to_seconds(value):
    if pd.isna(value) or value == '':
        return np.nan
    # Sub-minute laps (e.g. Sakhir 2020) are returned as seconds only.
    m = re.fullmatch(r'(?:(\d+):)?(\d{1,2}(?:\.\d+)?)', str(value))
    if not m or float(m[2]) >= 60:
        raise ValueError(f'Unexpected qualifying time: {value!r}')
    return int(m[1] or 0) * 60 + float(m[2])


def validate_table(df, kind):
    required = KEYS + ['race_name','circuit_id','race_date','driver_name','constructor_id']
    required += ['qualifying_position','q1','q2','q3'] if kind == 'qualifying' else ['grid','position','position_text','status','points','laps']
    missing = set(required) - set(df)
    if missing: raise ValueError(f'{kind}: missing columns {sorted(missing)}')
    if df.empty: raise ValueError(f'{kind}: empty data')
    if df[KEYS].isna().any().any() or df.duplicated(KEYS).any():
        raise ValueError(f'{kind}: null or duplicate season/round/driver keys')
    if not df['season'].isin([2019,2020,2021]).all():
        raise ValueError('Historical EDA is limited to 2019-2021; do not mix the 2026 exercise or held-out years.')
    columns = ['qualifying_position'] if kind == 'qualifying' else ['grid','position','points','laps']
    for c in columns:
        if not pd.api.types.is_numeric_dtype(df[c]) or df[c].isna().any() or not np.isfinite(df[c]).all():
            raise ValueError(f'{kind}: {c} must contain finite numbers')
        if (df[c] < 0).any(): raise ValueError(f'{kind}: negative {c}')
    if kind == 'qualifying' and (df['qualifying_position'] < 1).any():
        raise ValueError('Qualifying ranks start at 1')
    if kind == 'results' and (df['position'] < 1).any():
        raise ValueError('Classification order starts at 1; inspect position_text and status separately')


def synthetic_tables():
    """Small explicitly fictional data. Not a replacement for Italy 2026 facts."""
    rng = np.random.default_rng(RANDOM_SEED)
    qualifying, results = [], []
    for season in [2019,2020,2021]:
        for rd in [1,2,3]:
            finishes = rng.permutation(np.arange(1,21))
            for i in range(1,21):
                common = dict(season=season,round=rd,race_name=f'Fictional event {rd}',
                              circuit_id=f'fictional_{rd}',race_date=f'{season}-06-{rd:02}',
                              driver_id=f'fictional_driver_{i:02}',driver_name=f'Fictional driver {i}',
                              constructor_id=f'fictional_team_{(i-1)//2+1}')
                q = dict(common,qualifying_position=i,q1=f'1:{20+i/5:.3f}',
                         q2=f'1:{19+i/5:.3f}' if i<=15 else '',q3=f'1:{18+i/5:.3f}' if i<=10 else '')
                pos = int(finishes[i-1])
                points = [25,18,15,12,10,8,6,4,2,1][pos-1] if pos<=10 else 0
                r = dict(common,grid=i if i<20 else 0,position=pos,position_text=str(pos),
                         status='Finished' if pos<=17 else 'Engine',points=float(points),laps=50 if pos<=17 else 20)
                qualifying.append(q); results.append(r)
    return pd.DataFrame(qualifying),pd.DataFrame(results)


def load_historical(root, mode='snapshot'):
    if mode == 'snapshot':
        q = read_verified_csv(root,'qualifying_2019_2021_v1.csv')
        r = read_verified_csv(root,'results_2019_2021_v1.csv')
        provenance = 'PROVIDED_REAL_SNAPSHOT: Jolpica 2019-2021, no current API request'
    elif mode == 'synthetic':
        q,r = synthetic_tables()
        provenance = 'SYNTHETIC_TEACHING_DATA: fictional events/drivers, seed 414; no empirical F1 claims'
    else:
        raise ValueError('Choose snapshot or synthetic explicitly; no silent fallback.')
    validate_table(q,'qualifying'); validate_table(r,'results')
    q = q.copy()
    for c in ['q1','q2','q3']: q[c+'_seconds'] = q[c].map(time_to_seconds)
    return q,r,provenance


def merge_historical(q,r):
    validate_table(q,'qualifying'); validate_table(r,'results')
    # Results define the population. Missing qualifying is kept, not silently dropped.
    qcols = KEYS+['qualifying_position','q1','q2','q3','q1_seconds','q2_seconds','q3_seconds']
    joined = r.merge(q[qcols],on=KEYS,how='left',validate='one_to_one',indicator='qualifying_match')
    key_check = r[KEYS].merge(q[KEYS],on=KEYS,how='outer',validate='one_to_one',indicator=True)
    audit = key_check['_merge'].value_counts().rename_axis('coverage').reset_index(name='rows')
    joined['top10'] = joined['position'].le(10)
    joined['scored_points'] = joined['points'].gt(0)
    joined['qualifying_band'] = pd.cut(joined['qualifying_position'],[0,10,15,np.inf],labels=['P1–P10','P11–P15','P16+'])
    joined['qualifying_band'] = joined['qualifying_band'].astype('string').fillna('No qualifying record')
    joined['qualifying_band'] = pd.Categorical(joined['qualifying_band'],
        categories=['P1–P10','P11–P15','P16+','No qualifying record'],ordered=True)
    return joined,audit


def feature_audit(df):
    return pd.DataFrame([{'field':c,'dtype':str(df[c].dtype),'missing_n':int(df[c].isna().sum()),
                          'missing_pct':float(df[c].isna().mean()*100),'distinct_nonmissing':int(df[c].nunique())}
                         for c in df.columns])


def summary_by(df,group):
    return df.groupby(group,observed=True,dropna=False).agg(
        driver_race_rows=('driver_id','size'),top10_n=('top10','sum'),
        top10_rate_pct=('top10',lambda x:100*x.mean()),
        scored_points_rate_pct=('scored_points',lambda x:100*x.mean())).reset_index()


def load_italy(root):
    df = read_verified_csv(root,'italy_2026_ferrari_mclaren_v1.csv')
    if len(df)!=4 or df['driver_id'].duplicated().any() or set(df['constructor_id']) != {'ferrari','mclaren'}:
        raise ValueError('Italy extract requires four unique drivers from Ferrari and McLaren.')
    if not df['season'].eq(2026).all() or not df['event'].eq('Italy').all():
        raise ValueError('Wrong forecast observation: expected Italy 2026 only.')
    if not np.isfinite(df['points']).all() or df['points'].lt(0).any():
        raise ValueError('Invalid observed points')
    totals = df.groupby('constructor_id')['points'].sum()
    return df,totals,float(totals['ferrari']-totals['mclaren'])


def update_forecast(observed_gap,spain_gap,low=None,high=None,probabilities=None):
    """All gaps = Ferrari minus McLaren. Probabilities refer to the full horizon."""
    for v in [observed_gap,spain_gap]:
        if not isinstance(v,(int,float,np.number)) or not math.isfinite(v):
            raise ValueError('Enter finite signed gaps, with Ferrari positive and McLaren negative.')
    if (low is None)!=(high is None): raise ValueError('Enter both interval endpoints, or leave both empty.')
    answer = {'observed_italy_gap':float(observed_gap),'expected_spain_gap':float(spain_gap),
              'expected_total_gap':float(observed_gap+spain_gap)}
    if low is not None:
        if not all(math.isfinite(float(v)) for v in [low,high]) or not low<=spain_gap<=high:
            raise ValueError('Require low <= expected Spain gap <= high, with finite values.')
        answer.update(total_gap_low=float(observed_gap+low),total_gap_high=float(observed_gap+high))
    if probabilities is not None:
        if set(probabilities)!={'Ferrari','Tie','McLaren'}: raise ValueError('Use Ferrari, Tie and McLaren probabilities.')
        vals=list(probabilities.values())
        if not all(isinstance(v,(int,float,np.number)) and math.isfinite(v) and 0<=v<=100 for v in vals) or not math.isclose(sum(vals),100,abs_tol=1e-6):
            raise ValueError('The three full-horizon probabilities must be in 0-100 and sum to 100.')
        answer['subjective_probabilities_pct']=probabilities
    return answer


def export_evidence(root,tables,personal,provenance,figures=None):
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')
    out=Path(root)/'outputs'/f'w02_thu_{stamp}_{uuid.uuid4().hex[:6]}'
    out.mkdir(parents=True,exist_ok=False)
    for name,df in tables.items():
        if not re.fullmatch(r'[A-Za-z0-9_]+',name): raise ValueError('Unsafe output name')
        df.to_csv(out/f'{name}.csv',index=False)
    (out/'prediction_and_decisions.json').write_text(json.dumps(personal,indent=2,ensure_ascii=False,allow_nan=False),encoding='utf-8')
    for name,fig in (figures or {}).items():
        if not re.fullmatch(r'[A-Za-z0-9_]+',name): raise ValueError('Unsafe figure name')
        fig.savefig(out/f'{name}.png',dpi=150,bbox_inches='tight')
    manifest={'created_at_utc':datetime.now(timezone.utc).isoformat(),'seed':RANDOM_SEED,
              'historical_provenance':provenance,'forecast_provenance':'Official F1 Italy 2026 table, instructor-transcribed snapshot; not synthetic',
              'python':platform.python_version(),'pandas':pd.__version__,'numpy':np.__version__,
              'source_manifest_sha256':sha256(Path(root)/DATA_REL/'snapshot_manifest_v1.json'),
              'note':'Files and computations are evidence of execution, not a grade or proof of understanding.',
              'files':{p.name:sha256(p) for p in sorted(out.iterdir())}}
    (out/'run_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return out
