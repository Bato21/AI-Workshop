# W02 Thursday · Data dictionary

The historical files are normalized snapshots from Jolpica. The manifest contains every capture URL, timestamp and checksum. Source CSVs should remain unchanged.

| Field | Meaning | Interpretation caution |
|---|---|---|
| `season`, `round`, `driver_id` | Composite key: driver in a race within a season | All three are needed; do not join by name or driver alone |
| `race_name`, `circuit_id`, `race_date` | Event context and race date | Circuit names and calendar patterns differ between years |
| `driver_name` | Readable driver label | Display field, not a join key |
| `constructor_id` | Team identifier for this entry | A driver can change teams over time |
| `qualifying_position` | Classification order in qualifying | Not necessarily the race starting grid, especially with penalties or Sprint formats |
| `q1`, `q2`, `q3` | Recorded segment times; text or missing | Formats include `1:23.456` and sub-minute `53.904`; absent Q3 is not zero |
| `q1_seconds`, `q2_seconds`, `q3_seconds` | Parsed numeric segment times, created by helper | Missing remains missing; do not compare raw times across circuits as though distance/conditions matched |
| `grid` | Race starting position recorded by source | Zero is retained as a special recorded value; investigate, do not treat as pole |
| `position` | Numeric race classification order | It can exist for a retired driver; it is not proof of finishing |
| `position_text` | Source classification label | Inspect alongside numeric position and status |
| `status` | Recorded race outcome/status | A retired driver can still have a classification order; no blanket NaN rule |
| `points` | Driver's points from the result endpoint | Race-result points, not cumulative standings or automatically an entire Sprint weekend |
| `laps` | Completed laps in the result record | Post-race information, not known before the race |
| `qualifying_match` | Left-join coverage indicator | `left_only` preserves a race entry with no matched qualifying record |
| `qualifying_band` | P1–P10, P11–P15, P16+, or no qualifying record | A descriptive grouping, not a trained model |
| `top10` | Numeric race classification order ≤10 | Operational target definition; inspect source labels for unusual classifications |
| `scored_points` | Observed race-result points >0 | Separate definition from top10; retain actual fractional points if present |

## Forecasting files

`italy_2026_ferrari_mclaren_v1.csv` contains four driver rows transcribed from the official Italy table. `classification` retains `NC`; `status` normalizes completed-race time gaps to `Finished` and retains `DNF`. Both Ferrari drivers remain included. Team totals are calculated, not entered as cumulative standings.

`w01_shared_evidence_2026_v1.json` is the original shared evidence packet. Its measure is team points per weekend, including Sprint where `sprint` is true. It is preserved as context, not refreshed or used as historical development data. `prediction_context_v1.json` records the instructor's anonymous 9/1 report and the unresolved horizon. No values are inferred for missing personal confidence or unconfirmed photographed margins.

All forecast gaps use Ferrari minus McLaren. Probabilities, if supplied, refer to Ferrari winning, a tie, or McLaren winning over the complete two-GP points sum. No championship tie-break rule is applied: equal new points is a tie for this exercise.
