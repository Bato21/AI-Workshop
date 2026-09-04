# Monza 2021 · Teaching snapshots

These files are normalized teaching extracts, not an official FIA publication and not proof that your own API access works.

| File | Scope | Source at instructor capture |
|---|---|---|
| `monza_2021_results_v1.csv` | 20 driver-result rows, 2021 round 14 | Jolpica HTTP response, one complete requested page |
| `monza_2021_laps_v1.csv` | 892 recorded driver-lap rows, 2021 Italy race | FastF1 session loader; the library may use its cache |

The [manifest](snapshot_manifest_v1.json) records source provenance, retrieval timestamps, row counts and SHA-256 hashes. The helper verifies file hashes and reports `PROVIDED_SNAPSHOT` when you use these files. Historical capture provenance and your current execution provenance are different facts.

Sources: [Jolpica result endpoint](https://api.jolpi.ca/ergast/f1/2021/circuits/monza/results/), [Jolpica documentation](https://github.com/jolpica/jolpica-f1/blob/main/docs/README.md), [FastF1 documentation](https://docs.fastf1.dev/).

Driver identifiers and numbers remain strings. Missing lap times remain missing, and grid zero is not silently converted into a normal starting position. Recorded laps need not equal an ideal complete driver-by-lap grid; inspect missing values and status. This is a single-race teaching extract, not a full training dataset. Read the dictionary before combining tables.
