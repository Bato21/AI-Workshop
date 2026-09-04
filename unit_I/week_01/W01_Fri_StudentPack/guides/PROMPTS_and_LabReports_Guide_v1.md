# AI-use logs and lab reports · T3 2026

This guide explains documentation, not how to generate an entire class notebook. It does not add assessment criteria or replace a published rubric.

## Two different documents

An instructor's **notebook specification** tells an AI what teaching resource to build. Your **PROMPTS.md** records significant AI assistance you actually used while doing permitted work.

## During the first class

Keep your environment checks, record a genuine setup issue if one occurs, and identify your next action. If you use AI, start a short entry using the [template](../templates/PROMPTS_template_v1.md). If you do not use AI, state that honestly. You do not need to manufacture an interaction or write a full lab report during the setup block.

## A useful interaction entry

Record context, the prompt, an output summary, what you accepted, modified and rejected, verification, and limitations. Write “none” with an explanation when appropriate. Quality is not measured by the number of prompts or rejections.

Make verification specific: identify the check and its observed result. “It ran” establishes execution, not correctness. A failed check is useful evidence when accurately documented.

Do not include passwords, API tokens, private student data or confidential material. Record the actual model/version when known, otherwise write “not recorded”. Never fill in a made-up version.

## Lab reports

The [seven-section scaffold](../templates/lab_report_template_v1.md) helps organize a report: problem, data, methodological decisions, experiments, errors, runbook and AI-use summary. Use it when the assessment asks for a report. Mark sections that genuinely do not apply rather than inventing results; Lab 0 is a setup exercise, not an excuse to fabricate model metrics.

Link claims to evidence in your own notebook. A useful result can be negative. A metric alone does not establish value for a decision, and beating a baseline is not sufficient by itself.

## Current conventions

- `RANDOM_SEED = 414`.
- Assessed temporal modelling: train ≤ 2021; calibration 2022; test 2023–2024. Do not use the test set for choosing features, models or thresholds.
- AI is prohibited in the two midterms and the individual oral Applied Control. Follow the specific rules of all other activities.
- Keep local teaching samples labelled as synthetic or as documented snapshots. Do not present them as live API results or as evidence of successful API access.
- The published assessment instructions decide which artifacts, data sources and rubric weights apply. Old March examples are not current policy.

## Before submitting

- Can another person follow the runbook in a clean environment?
- Does the notebook state where its data came from?
- Do reported numbers match executed outputs?
- Are decisions and limitations your own, truthful account?
- Are you submitting through the actual published course link, by the current deadline?
