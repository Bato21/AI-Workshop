# Data dictionary · Monza 2021 teaching case · v1

Use this reference beside your own output. The real-data case is one season, circuit and race session. Synthetic mode uses generic identifiers and `synthetic_circuit`; it is not a record of the real event.

## Results: one driver in one race

Composite key: `season + round + driver_id`. `driver_number` is also retained to identify drivers in the lap data within this case. Neither a surname nor a row index is a reliable cross-source key. Do not perform a many-to-many join or assume numbers are globally unique across seasons.

| Field | Meaning | Read with care |
|---|---|---|
| `season` | Championship year | Not the class year |
| `round` | Event number within the season | Synthetic examples use 0, not an actual round |
| `circuit_id` | Circuit identifier | A circuit can host events in different years |
| `driver_id` | Source's driver identifier | Prefer it to matching surnames |
| `driver_number` | Number represented as text | Used only within the specified season/event |
| `constructor_id` | Team identifier | Different from the driver |
| `grid` | Recorded starting-position field | 0 is not P0; investigate special/unspecified starts |
| `position` | Recorded finishing classification | Not a stand-alone DNF flag |
| `position_text` | Text classification supplied by the API | Distinct from the numeric field |
| `points` | Points attributed to that race result | Not cumulative season points; no missing-to-zero conversion |
| `status` | Description of the race outcome | Consult together with classification; do not infer from rank alone |

## Laps: one driver on one lap of the session

Composite key for this table: `season + round + driver_number + lap_number`. Session type is fixed to `R` in this package; include session in a key when combining different session types.

| Field | Meaning | Read with care |
|---|---|---|
| `season`, `round`, `circuit_id` | Event identifiers | Must agree before combining tables |
| `driver_number` | Driver number in this event | Stored as text, not a measurement |
| `lap_number` | Lap index for that driver | Drivers need not complete the same number of laps |
| `lap_time_s` | Recorded lap duration converted to seconds | Missing values can occur; investigate rather than automatically deleting |
| `compound` | Tyre-compound label | Not numerical; values depend on source and session |
| `is_accurate` | FastF1's timing-consistency flag | Not proof that a lap is comparable, representative or suitable for every analysis |

## Checks are questions with evidence

The helper reports empty tables, duplicate keys, missing critical fields, simple value constraints and review counts. PASS means only that the named check passed. It does not establish completeness against an independent source, prediction validity, causal meaning or student understanding.

## Individual dictionary record

Complete these in your notebook. Read first, then work at your own pace.

1. What does one row represent in each table?
2. Explain two fields using a row you can actually see.
3. Select one computed check. What is its observed result, and why does it matter?
4. For a prediction just before the race starts, name one usable candidate field and one unavailable field, with reasons. Availability must refer to the stated time, not today's ability to download the completed race.
5. Record feedback, your correction/recheck, and your next action for Lab 0.

The course's later modelling split remains train through 2021, calibration 2022, test 2023–2024. No model is fitted today. Describing results after a race is not the same task as forecasting them before it.

Sources: [Jolpica result-field documentation](https://github.com/jolpica/jolpica-f1/blob/main/docs/endpoints/results.md) and [FastF1 source/documentation](https://github.com/theOehrly/Fast-F1). The transformation code is visible in `w01_fri_support_v1.py`.
