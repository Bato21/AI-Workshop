# PROMPTS.md · AI-use log

Activity: IIT414W Lab 0 · Date: 2026-09-08 · Author: Baptiste Vial

**AI use: Used.**

## Tools

| Tool | Model | Purpose |
|---|---|---|
| Claude (chat) | Not recorded | Helped me draft the structured prompt that governed the Claude Code session: the phase breakdown and the constraints (never fabricate output, never turn a failed check into `PASS`, keep seed 414, `MODE = "snapshot"`, label FastF1 tables `FASTF1_SESSION`). Did not touch the repository. |
| Claude Code | Claude Opus 5 | Ran the work in the repository: inventory, environment build, notebook execution, output comparison, and drafts I reviewed and edited. |

Prompts below are faithful summaries, not transcripts. No credentials or personal
data were included in any prompt.

## Log

### 1 · Choosing the Python environment

**Context:** three Python versions disagreed — 3.12.4 in the handout, 3.13.7 in
my saved notebooks, 3.14.3 on `PATH`.
**Asked:** report the real Python and kernel, parse the actual imports, and build
`requirements.txt` from installed versions, not from memory.
**Got:** no Python 3.13 existed here at all, so my earlier outputs were not
reproducible; the only kernel spec launched `"python"` relatively and resolved to
an interpreter with no `ipykernel`; four options with trade-offs.
**Accepted:** a venv on the already-present 3.10.3 — the newest interpreter for
which every pinned version has a wheel, so I matched all five pins without a
download.
**Changed:** I also installed `requests` and `fastf1`, which the snapshot route
never imports, so the manifest shows real versions instead of `MISSING`.
**Rejected:** installing 3.12.4 (manual download), 3.14.3 (would force
`pandas 3.0.x`, breaking the pins), Anaconda 3.11.4 (older pandas, no isolation).
**Verification:** `run_manifest.json` records `"python": "3.10.3"` with
`numpy 1.26.4`, `pandas 2.3.1`, `requests 2.32.4`, `fastf1 3.5.3` — identical to
the pins; `setup_evidence_20260908T140226_610632Z.json` reports all checks
`PASS`.
**Limit:** verifies the packages, not the Python version, which still deviates
from 3.12.4. I did not test that the lab behaves identically there.

### 2 · Detecting that my run took the live route

**Context:** I ran both notebooks and reported them done. The declared route was
`snapshot`.
**Asked:** "Acabo de ejecutar los 2 notebooks con el venv creado recién, dime qué
falta por hacer."
**Got:** both ran clean, but Friday cell 6 still held `MODE = "live"`, the
manifest recorded `JOLPICA_HTTP` and `FASTF1_SESSION`, a 5.4 MB
`data/cache/fastf1_w01/` had appeared, and the notebooks had run in the wrong
order.
**Accepted:** the finding — backed by two independent pieces of evidence, not an
assertion.
**Changed:** I set `MODE = "snapshot"` myself, then had the cache deleted and
both notebooks re-run in order.
**Rejected:** that the run might be acceptable because the live CSVs were
byte-identical to the snapshot. Matching data does not make the provenance right.
**Verification:** the re-run's manifest records `PROVIDED_SNAPSHOT` with
`api_access_confirmed: false`, and `data/cache/` was not recreated.
**Limit:** shows FastF1 was not invoked on this run; not that nothing else on the
machine reached the network.

### 3 · Executing and comparing two runs

**Asked:** run from a fresh kernel in the documented order, run again, and diff
the stable outputs; flag anything beyond timestamps and folder names.
**Got:** both notebooks at `execution_count [1,2,3,4,5,6]` with no errors, and a
comparison reporting everything identical.
**Rejected:** the first comparison. It printed the same folder name for both
runs — the script picked a folder with `next(...)` while the previous run's
folder was still on disk, so it compared run 1 against itself and would have
reported a false `IDENTICAL`. Fixed by selecting run 2 explicitly.
**Verification:** with the corrected script, `results.csv`, `laps.csv` and
`checks.csv` were byte-identical (`1da5e255…`, `8f0b7a03…`, `0bf399ea…`), and
manifests, evidence and cell outputs matched once timestamps were normalised.
**Limit:** shows the pipeline is deterministic on an unchanged snapshot, not that
the code is correct. It would not hold on a live route.

### 4 · Reverting an edit I made to supplied instrumentation

**Context:** the evidence file kept reporting
`"restart_and_run_all": "NOT CHECKED"`, so I had edited Thursday cell 12 to say
`'Done'`.
**Asked:** check my answers against the rubric.
**Got:** the string is hardcoded, so it would read `Done` whether or not I
restarted anything — no evidential value; the course wrote it that way
deliberately.
**Accepted / changed:** I reverted it to the supplied literal and moved the
restart claim into the README, where it rests on the execution counts.
**Verification:** the reverted line was diffed against a backup of the unmodified
notebook and matches; the current evidence file again reports `NOT CHECKED`.
**Limit:** the evidence file therefore still cannot confirm a restart.

### 5 · Drafting my notebook answers

**Asked:** draft Friday cells 3, 11 and 18 from the real outputs, mark every
judgement call for review, invent nothing. Later: simplify into clean text.
**Accepted:** the factual scaffolding — 20 rows / 20 distinct `driver_id`; 892
rows with no duplicates on `(driver_number, lap_number)`; the 1060 − 892 = 168
gap; 36 missing lap times; `grid = 0` for `gasly` and `tsunoda` — after checking
each against my own exports.
**Changed:** the tagged drafts were too cluttered, so I had them rewritten as
plain prose, and had the "Feedback received" field state honestly that no
lecturer feedback was received this session.
**Rejected:** a proposed rewrite of my own cell 7. I had written that the source
was HTTP and that we were downloading directly from the API, contradicting my own
manifest; I corrected that myself and kept my wording, adding one sentence on the
limitation.
**Verification:** every number in cells 11 and 18 was recomputed from the
exported CSVs; `checks.csv` shows the `PASS` and the two `REVIEW` rows as
described.
**Limit:** written from one run of one race; the row-unit claims hold for these
two files, not for the providers' full datasets.

## Reflection

- **Most useful:** catching that my "successful" run had taken the live route.
  Both notebooks executed cleanly, so nothing on the surface suggested a problem;
  the evidence was in `run_manifest.json` and a cache directory I had not thought
  to check.
- **Least reliable:** the first comparison script, which compared a run against
  itself and would have reported a false `IDENTICAL`. A tool reporting `PASS` is
  not the same as a verification.
- **My own decision:** accepting a documented Python-version deviation (3.10.3
  instead of 3.12.4) to match all five package pins exactly. A reproducible
  package set with one recorded deviation is more useful than a matching Python
  version with five drifting packages.
- **Next verification:** rebuild on Python 3.12.4 and confirm the same three CSV
  hashes, closing the one deviation this submission carries.
