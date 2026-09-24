# W02 Thursday · Local snapshots

| File | Scope | Rows |
|---|---|---:|
| `qualifying_2019_2021_v1.csv` | All records returned by paginated Jolpica queries for 2019, 2020 and 2021 | 1197 |
| `results_2019_2021_v1.csv` | All race-result entries returned for the same years | 1200 |
| `italy_2026_ferrari_mclaren_v1.csv` | Official Italy 2026 result, Ferrari and McLaren only; instructor transcription | 4 |

The result-left join retains 1200 entries: 1197 matched qualifying records and 3 unmatched result entries. Qualifying rows by year: 418, 340, 439. Result rows by year: 420, 340, 440. Missing qualifying records are not synthesized to make the counts match.

`snapshot_manifest_v1.json` records source URLs, UTC retrieval times, pagination totals/offsets, transformations, row counts and SHA-256 checksums. Raw API responses are retained separately by the instructor. Real snapshots are the default; synthetic practice is an explicit, labelled helper mode with fictional drivers and events.

The 2026 prediction case is stored separately from the historical EDA. `w01_shared_evidence_2026_v1.json` preserves the original chart data; it is not a new audit of all 2026 results. Spain has no result in this packet.

No live access is required in class. Do not alter these source files to write your answers. Copy outputs and record decisions in your notebook instead.
