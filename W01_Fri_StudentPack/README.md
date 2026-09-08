# IIT414W · Lab 0 — Reproducible setup and source evidence

| | |
|---|---|
| **Python** | **3.10.3** |
| **Data mode** | **`snapshot`** (Monza 2021 teaching snapshot) |
| **Seed** | `414` |
| **Repository** | https://github.com/Bato21/AI-Workshop |
| **Submitted commit** | [`aa8d2d5`](https://github.com/Bato21/AI-Workshop/commit/aa8d2d575282cf97a7ff6a892864615ff68d286f) — full hash `aa8d2d575282cf97a7ff6a892864615ff68d286f`. This is the content commit; the line you are reading was added by the follow-up commit that is the current `HEAD` of `main`. |
| **AI-use record** | [`PROMPTS.md`](PROMPTS.md) |

## 1. Setup

From the repository root (one level above this folder):

```powershell
py -3.10 -m venv .venv
.venv\Scripts\python.exe -m pip install -r W01_Fri_StudentPack\requirements.txt
.venv\Scripts\python.exe -m ipykernel install --user ^
    --name iit414w-w01 --display-name "IIT414W W01 (venv 3.10.3)"
```

**Select the kernel `IIT414W W01 (venv 3.10.3)` in both notebooks.** Its spec
launches the interpreter by absolute path. This matters: the kernel specs
originally on this machine launched `"python"` by relative name, resolved through
`PATH`, so the interpreter depended on the shell that started Jupyter.

**Deviation.** `requirements_w01_fri_v1.txt` documents Python 3.12.4. No 3.12
interpreter exists here, so the venv was built on 3.10.3 — the newest present for
which every pinned version has a wheel. All five package pins match exactly.
`nbclient` / `nbconvert` were used to run the notebooks headlessly; they are
tooling, not lab dependencies, and are excluded from `requirements.txt`.

## 2. Run order

Restart the kernel, then run all cells:

| # | Notebook | Writes |
|---|---|---|
| 1 | `unit_I/week_01/W01_Thu_setup_and_reproducibility_v2.ipynb` | `outputs/setup_evidence_<UTC>.json` |
| 2 | `unit_I/week_01/W01_Fri_f1_data_ecosystem_v1.ipynb` | `outputs/w01_fri_<UTC>_<id>/` |

Thursday first — Friday's opening block expects Thursday's status to exist. Both
submitted notebooks carry `execution_count [1,2,3,4,5,6]` with no error outputs.

> The evidence files cannot certify the restart themselves:
> `"restart_and_run_all": "NOT CHECKED …"` and
> `"student_restart_run_all": "NOT VERIFIED BY THIS CELL"` are fixed strings in
> the supplied material (Thursday cell 12; helper line 202), not blanks left
> unfilled. The restart claim rests on this entry and the execution counts.

## 3. Data mode and source

`MODE = "snapshot"` (Friday cell 6). No network access is attempted or required.

| | Path |
|---|---|
| Snapshot | `data/samples/w01_fri_v1/monza_2021_{results,laps}_v1.csv` |
| Manifest | `data/samples/w01_fri_v1/snapshot_manifest_v1.json` |
| Dictionary | `unit_I/week_01/W01_Fri_DataDictionary_v1.md` |

The helper verifies each file's SHA-256 against the manifest before returning it.

## 4. Outputs

```
outputs/
├── setup_evidence_20260908T140226_610632Z.json      <- Thursday
└── w01_fri_20260908T140228_575936Z_255561/          <- Friday
    ├── results.csv   1da5e255696cd6d3…
    ├── laps.csv      8f0b7a03b038324b…
    ├── checks.csv    0bf399ea2f1719a4…
    └── run_manifest.json
```

Each Friday run creates a new folder and never overwrites earlier evidence. Only
the final run is submitted.

## 5. Evidence notes

### Note 1 · Source

Both tables loaded on the snapshot route: `run_manifest.json` records
`"origin": "PROVIDED_SNAPSHOT"` and `"api_access_confirmed": false` for `results`
and for `laps`. One event only — 2021, round 14, `monza` — verified as the single
distinct `(season, round, circuit_id)` in each table.

| Table | Shape | One row is | Evidence |
|---|---|---|---|
| `results.csv` | 20 × 11 | one driver's classified result | 20 rows, 20 distinct `driver_id`, 0 duplicates |
| `laps.csv` | 892 × 8 | one recorded lap by one driver | 0 duplicates on `(driver_number, lap_number)`; laps 1–53; 20 drivers |

Different grain: a complete grid would be 20 × 53 = 1060 rows, so 168 are absent.
Joining without aggregating first would multiply the result rows.

Three distinct things:

1. **Source data** — Jolpica's HTTP endpoint for `results`; FastF1's session
   loader (`2021 Italy R`) for `laps`.
2. **Stored copy** — the CSVs in `data/samples/w01_fri_v1/`, captured by the
   instructor on 2026-09-02T23:38Z with SHA-256 in the manifest. This run read
   those files and made no network request.
3. **Teaching data** — normalised extracts for one race; not an FIA publication,
   not a training dataset.

**`laps` caveat.** Its `original_source.origin` is **`FASTF1_SESSION`**, recorded
as `"api_access_confirmed": "NOT VERIFIED: library may use cache"`. A table from
FastF1's session loader **does not prove a new network request** — the library
may serve it from cache. `results` is recorded as `api_access_confirmed: true`,
but that confirms the *instructor's* HTTP access on 2 September, not any request
made here.

### Note 2 · Check

`Nonempty laps with unique keys` in `checks.csv`: **`PASS`**, observed
`892 rows; 0 duplicate keys`. Reproduced independently from `laps.csv`.

- **Establishes:** `(driver_number, lap_number)` is a usable key, so the table can
  be joined or indexed on it without silently duplicating rows.
- **Does not establish:** completeness. 168 of 1060 rows are absent, and
  `Missing lap times` is `REVIEW` with `36; investigate, do not automatically
  drop`. A `PASS` here is an absence of duplicates, not a presence of all laps.

Both `REVIEW` rows were left as `REVIEW`. `Grid zero` reports `2; special/
unspecified start encoding, not P0` — confirmed as `gasly` (P19, `Suspension`)
and `tsunoda` (P20, `Brakes`). `grid = 0` is a pit-lane or unspecified start, not
a place ahead of first.

### Note 3 · Decision and verification

**Decision.** Build a venv on Python 3.10.3 and register a kernel pointing at it
by absolute path, rather than run on whatever `python` resolved to.

**Why.** The machine reported three Python versions for one lab: 3.12.4 in the
handout, 3.13.7 in the saved notebooks' `language_info`, and 3.14.3 on `PATH` —
which has no `ipykernel`. Both available kernel specs used relative
`"argv": ["python", …]`. I accepted a documented Python-version deviation in
order to match all five package pins exactly, rather than the reverse.

**Verified.** `run_manifest.json` records `"python": "3.10.3"` with
`numpy 1.26.4`, `pandas 2.3.1`, `requests 2.32.4`, `fastf1 3.5.3` — identical to
the pins. `setup_evidence_20260908T140226_610632Z.json` reports all three health
checks `PASS` and all five packages available.

**A correction happened.** The first execution ran with the shipped default
`MODE = "live"`: the manifest recorded `JOLPICA_HTTP` and `FASTF1_SESSION`, and a
5.4 MB `data/cache/fastf1_w01/` appeared. I set `MODE = "snapshot"`, deleted the
cache, discarded that run and re-ran from a fresh kernel in order. The new
manifest records `PROVIDED_SNAPSHOT` with `api_access_confirmed: false`, and
`data/cache/` was **not** recreated — independent confirmation FastF1 was never
invoked. The discarded run's CSVs were byte-identical to the snapshot; identical
data did not make it acceptable, because provenance was what differed.

**Repeat check.** Two runs from a fresh kernel: `results.csv`, `laps.csv` and
`checks.csv` byte-identical; manifests, evidence file and all cell outputs
identical once timestamps were normalised. Only folder names and timestamps
differed. A second correction was needed here — the first comparison script
picked a folder with `next(...)` while the previous run's folder was still on
disk, compared run 1 against itself, and would have reported a false
`IDENTICAL`. Caught because both printed names matched; fixed by selecting run 2
explicitly.

---

Excluded from the submission ZIP: `.git/`, `.venv/`, `__pycache__/`,
`.ipynb_checkpoints/`, FastF1 caches, and any credential or personal data.
