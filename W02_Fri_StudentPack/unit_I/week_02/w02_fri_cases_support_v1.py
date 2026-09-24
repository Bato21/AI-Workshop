"""Visible calculation/plotting support for three offline audit cases. No answer key."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import uuid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 414
DATA_DIR = Path('data/samples/w02_fri_v1')


def find_root(start=None):
    p=Path(start or Path.cwd()).resolve()
    for candidate in (p,*p.parents):
        if (candidate/'.iit414w-root').is_file(): return candidate
    raise FileNotFoundError('Extract the whole Friday ZIP, including .iit414w-root, before opening the notebook.')


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_results(df):
    columns=['season','round','race_name','driver_id','constructor_id','points']
    if set(columns)-set(df): raise ValueError('Required result columns missing.')
    if df.empty: raise ValueError('Empty data is not a valid case dataset.')
    keys=['season','round','driver_id']
    if df[keys].isna().any().any() or df.duplicated(keys).any():
        raise ValueError('Driver-race keys must be present and unique.')
    if not df.season.isin([2019,2020,2021]).all():
        raise ValueError('Use development data 2019-2021 only; 2026 and held-out years are separate.')
    if not pd.api.types.is_numeric_dtype(df.points) or not np.isfinite(df.points).all() or df.points.lt(0).any():
        raise ValueError('Points must be finite and nonnegative; retain zero and fractional points.')


def synthetic_results():
    rng=np.random.default_rng(SEED)
    rows=[]
    for year in [2019,2020,2021]:
        for rd in range(1,13):
            for team,base in [('team_a',12),('team_b',10),('team_c',0)]:
                total=float(rng.integers(max(0,base-5),base+6)) if base else (float(rng.integers(1,6)) if rd%4==0 else 0.)
                for driver in [1,2]:
                    rows.append({'season':year,'round':rd,'race_name':f'Fictional event {rd}',
                                 'driver_id':f'fictional_{team}_{driver}','constructor_id':team,
                                 'points':total/2})
    return pd.DataFrame(rows)


def load_results(root,mode='snapshot'):
    if mode=='snapshot':
        directory=Path(root)/DATA_DIR
        manifest_path=directory/'source_manifest_v1.json'
        if not manifest_path.is_file(): raise FileNotFoundError('Friday data manifest missing. Restore the complete ZIP.')
        manifest=json.loads(manifest_path.read_text(encoding='utf-8'))
        p=directory/manifest['file']
        if not p.is_file(): raise FileNotFoundError('Friday results CSV missing. Restore the original package.')
        if sha256(p)!=manifest['sha256']: raise ValueError('Snapshot hash mismatch. Restore the original; no silent fallback.')
        df=pd.read_csv(p,dtype={'driver_id':'string','constructor_id':'string'})
        if len(df)!=manifest['rows'] or list(df.columns)!=manifest['columns']:
            raise ValueError('Snapshot count/schema differs from manifest.')
        teams=['ferrari','mclaren','williams']; labels=['Ferrari','McLaren','Williams']
        provenance='PROVIDED_REAL_SNAPSHOT: Jolpica 2019-2021, race-result points only; no live request'
    elif mode=='synthetic':
        df=synthetic_results();teams=['team_a','team_b','team_c'];labels=['Fictional A','Fictional B','Fictional C']
        provenance='SYNTHETIC: fictional teams/events and teaching points, seed 414; not observed F1 evidence'
    else: raise ValueError('Choose snapshot or synthetic explicitly.')
    validate_results(df)
    return df,teams,labels,provenance


def team_race_table(results,year,teams):
    validate_results(results)
    if year not in [2019,2020,2021]: raise ValueError('Choose 2019, 2020 or 2021.')
    selected=results.loc[results.season.eq(year)&results.constructor_id.isin(teams)].copy()
    if selected.empty: raise ValueError('Selected year/team slice is empty.')
    counts=selected.groupby(['round','constructor_id'],observed=True).size()
    if not counts.eq(2).all(): raise ValueError('Expected two driver-result rows per selected team/race; inspect missing or extra rows.')
    points=selected.groupby(['round','constructor_id'],observed=True).points.sum().unstack().sort_index()
    if set(points)!=set(teams) or points.isna().any().any():
        raise ValueError('All selected teams must cover the same races; do not fill missing races with zero.')
    return points[teams]


def correlation(x,y):
    if len(x)<2 or np.std(x)==0 or np.std(y)==0: return None
    return float(np.corrcoef(x,y)[0,1])


def plot_case1(cumulative,teams,labels,year):
    fig,ax=plt.subplots(figsize=(8.8,4.8))
    a,b=teams[:2];r=correlation(cumulative[a],cumulative[b])
    scatter=ax.scatter(cumulative[a],cumulative[b],c=cumulative.index,cmap='viridis',s=48)
    fig.colorbar(scatter,ax=ax,label='Race round')
    ax.set(xlabel=f'{labels[0]} cumulative race-result points',ylabel=f'{labels[1]} cumulative race-result points',
           title=f'Case 1 · Cumulative relationship, {year} · r={r:.3f}' if r is not None else 'Case 1 · Correlation undefined')
    fig.tight_layout()
    return fig


def plot_case2(selected,label,year):
    fig,ax=plt.subplots(figsize=(8.8,4.8))
    if selected.empty:
        ax.text(.5,.5,'No positive-point races in this selection',ha='center',transform=ax.transAxes)
    else:
        bars=ax.bar(selected.index.astype(str),selected.values,color='#1A3A5C')
        ax.bar_label(bars,fmt='%.2f',padding=4)
        ax.axhline(selected.mean(),color='#E63946',linestyle='--',label=f'Selected mean: {selected.mean():.2f}')
        ax.legend();ax.set_ylim(0,selected.max()*1.22)
    ax.set(xlabel='Race round included by analyst',ylabel='Team race-result points',
           title=f'Case 2 · {label}, {year} · analyst-selected races')
    fig.tight_layout()
    return fig


def plot_case3(means,labels,year,zero=False):
    fig,ax=plt.subplots(figsize=(8.8,4.8))
    bars=ax.bar(labels[:2],means.values,color=['#E63946','#F28C28'])
    ax.bar_label(bars,fmt='%.2f',padding=5)
    low=0 if zero else float(np.floor(means.min()))
    # Avoid a degenerate axis on alternate/synthetic data, preserving the same values.
    top=max(float(means.max()*1.12),low+1)
    ax.set_ylim(low,top)
    ax.set(ylabel='Mean team race-result points per race',
           title=f'Case 3 · View {"B" if zero else "A"} · {year} · {"zero baseline" if zero else "truncated baseline"}')
    ax.text(.02,.96,f'Axis starts at {low:g}',transform=ax.transAxes,va='top',fontsize=10)
    fig.tight_layout()
    return fig


def save_work(root,tables,responses,provenance,year,mode):
    p=Path(root)/'outputs'/('w02_fri_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S_%fZ')+'_'+uuid.uuid4().hex[:5])
    p.mkdir(parents=True,exist_ok=False)
    for name,table in tables.items():
        if not name.replace('_','').isalnum(): raise ValueError('Unsafe output name.')
        table.to_csv(p/(name+'.csv'))
    (p/'responses_and_feedback.json').write_text(json.dumps(responses,ensure_ascii=False,indent=2,allow_nan=False),encoding='utf-8')
    manifest={'year':year,'mode':mode,'seed':SEED,'provenance':provenance,
              'files':{f.name:sha256(f) for f in p.iterdir()},
              'note':'Execution and written work are separate evidence. No automatic grade or cognitive-bias diagnosis.'}
    if mode=='snapshot':manifest['source_csv_sha256']=sha256(Path(root)/DATA_DIR/'results_2019_2021_v1.csv')
    (p/'run_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return p
