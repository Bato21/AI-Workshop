# Thursday class record · F1 forecasts and AI check

IIT414W · 24 September 2026 · 12:30–15:00 · Formative, no grade

**What you will do:** close your old Italy–Spain prediction; write criteria before reading an AI answer; check that answer against sources; predict the next two GPs separately; then complete the leakage and validation notebook. **Why:** a plausible answer is useful only when its evidence, timing and limits can be checked.

**Hand in:** this completed class record **on paper at 15:00 today**. If you use a digital accommodation, show the completed file to the lecturer at 15:00 instead. Keep a copy or photo of your two new forecasts for a later update. Save the notebook for your own study; it is not a second submission. Short phrases are enough. If an old card is missing, write “not recorded”.

The target throughout this sheet is **Grand Prix race points only**, excluding sprint points. `Gap = Ferrari points − McLaren points`: positive favours Ferrari, negative favours McLaren, zero is a tie.

## Step 1 · Old records and observed result · 12:35–12:50

Copy what you actually recorded on 3 September and after Italy on 10 September. Do this before looking at the observed total.

| Date of forecast | Predicted winner for Italy + Spain | Predicted two-GP gap (F−M), if recorded | Reason available then |
|---|---|---:|---|
| 3 Sep · before Italy | | | |
| 10 Sep · after Italy | | | |

Use the local `recent_race_points.csv` to add both drivers for each team.

| GP | Ferrari race points | McLaren race points | Observed gap (F−M) |
|---|---:|---:|---:|
| Italy, 6 Sep | | | |
| Spain (Madrid), 13 Sep | | | |
| Both GPs | | | |

Which recorded winner was correct? ________  Did your 10 Sep update improve the numerical gap error, if both numbers were recorded? ________

If a numerical gap was recorded, use `absolute error = |predicted gap − observed two-GP gap|`. Do not create a missing number. The original class vote was 9 Ferrari and 1 McLaren: this is a count of answers, not a 90% probability.

## Step 2 · Criteria before the AI answer · 12:50–12:55

Write one check in each row. Do not read Step 4 first.

| Check | This answer is usable only if… |
|---|---|
| Form · can I inspect it quickly? | |
| Content · are facts and sources right? | |
| Utility · can I make each GP decision from it? | |

## Step 3 · A prompt you can actually use · 12:55–13:00

Use or adapt this prompt. Fill in the bracketed time. The lecturer will show how to open an AI tool, paste the prompt and inspect its answer. If you have access, you may try it yourself; do not enter private information. You do not need an AI account: everyone audits the same printed example in Step 4. The links are part of the prompt so a tool with browsing can check them; a tool without browsing must say it could not.

> **Purpose:** Help me examine evidence so **I** can predict Ferrari versus McLaren race points separately for Azerbaijan (26 September) and the Bahrain GP at Sepang, Malaysia (4 October 2026). Do not make my final prediction for me. My decision time is **24 September 2026, [time]**. Count Grand Prix race points only, not sprint points.
>
> **Data already available:** Netherlands (23 August): Ferrari 22, McLaren 33; Italy (6 September): Ferrari 8, McLaren 22; Spain/Madrid (13 September): Ferrari 12, McLaren 19. Leclerc did not finish Italy; Hamilton did not finish Spain. These are observations, not proof of future performance.
>
> **Sources to check if you can open links:** calendar https://www.formula1.com/en/racing/2026 ; Netherlands https://www.formula1.com/en/results/2026/races/1292/netherlands/race-result ; Italy https://www.formula1.com/en/results/2026/races/1293/italy/race-result ; Spain https://www.formula1.com/en/results/2026/races/1294/spain/race-result . If you cannot open a link, say “provided by the student, not independently checked”; do not claim you verified it.
>
> **Tasks:** (1) Check the two GP names, dates and venues against the calendar if possible. (2) For **each GP separately**, identify two relevant signals, the dated observation supporting each, and one reason the signal may not transfer to that circuit. (3) Name one important fact unavailable at this decision time. Distinguish observed facts from assumptions.
>
> **Output:** a table with one row per GP and columns for signals, source/date, limitation and missing information; then at most three sentences on what I should verify next. Cite only pages you actually opened. Do not supply a winner, team-point estimate or combined two-GP total: I will record those myself after reviewing your evidence.

One change I made **before using** the prompt, and why: ___________________________________

## Step 4 · Audit a model answer · 13:00–13:07

This is a **deliberately flawed classroom example**, not a source of F1 facts:

> “Ferrari will beat McLaren by 15 points across the next two races, Azerbaijan and Singapore. Ferrari is ahead in the team standings, so the result is certain. I included all championship points in the estimate. No sources are needed.”

Mark at least two problems against your **Form / Content / Utility** criteria. Verify the calendar and the meaning of race points with the linked official pages or the local README. Write a corrected, limited claim; do not merely replace the wrong race name.

| Criterion | Where the answer fails | Evidence or check |
|---|---|---|
| | | |
| | | |

Corrected claim: ________________________________________________________________________

One change I would make to the prompt **after reviewing an answer**, and why: ________________

## Step 5 · Two forecasts, not one total · 13:07–13:25

Use at least two distinct signals available at your decision time. The local table contains recent race points and non-finishes; official links can provide more context if you have internet. A non-finish is relevant but does not prove the next car will retire. Keep today's forecasts frozen even if later evidence changes your mind.

| GP; forecast time | Ferrari race points | McLaren race points | Gap (F−M) and winner | Plausible gap range | Two signals, sources/dates, and one limitation |
|---|---:|---:|---|---|---|
| Azerbaijan · Baku · 26 Sep | | | | | |
| Bahrain GP · Sepang, Malaysia · 4 Oct | | | | | |

After Baku, a revised Sepang forecast belongs in a **new dated row**. Do not edit today's row. Your partner's strongest question about one signal: _____________________________

## Step 6 · Validation exit record · 14:45–15:00

Use your notebook work to give three short answers before handing in this record.

1. One leakage defect and its repair: _____________________________________________________
2. Two development folds within 2019–2021: ______________________________________________
3. Why 2023–2024 must stay out of tuning: _________________________________________________

**Hand-in check at 15:00:** old records or “not recorded” □ · observed total □ · three criteria □ · two AI problems □ · two separate forecasts with sources □ · three validation answers □ · copy/photo retained □

Sources available as of 23 September: [official calendar](https://www.formula1.com/en/racing/2026), [Italy](https://www.formula1.com/en/results/2026/races/1293/italy/race-result), [Spain](https://www.formula1.com/en/results/2026/races/1294/spain/race-result), [Netherlands](https://www.formula1.com/en/results/2026/races/1292/netherlands/race-result). The local CSV is a small classroom extract; it has no future race results.
