# Lab 0 · Assessment rubric

**Individual · 100 points · 3% of NP · Due Thursday 10 September 2026 at 12:30 (Santiago)**

The rubric assesses your own evidence using the four existing criteria. Full marks do not require live API access, additional features, an oral defence or a long report.

## How levels work

For each criterion select the highest anchor whose essential evidence is met, considering that criterion only. Use fixed anchor scores, not interpolated points. Record a brief evidence reference and a next step. Missing optional extensions never reduce the score.

Full achievement = 100% of the criterion; Solid = 80%; Basic = 60%; Limited = 30%; No assessable evidence = 0%. These are criterion anchors, not separate pass/fail rules. Choosing Basic in all four criteria gives 60/100, equivalent to grade 4.0.

## C1 · Environment and dependencies · 30 points

Observed Python/kernel/package checks; dependency file matching the selected route. This criterion assesses the working environment and its specification, not Git organisation or the quality of data explanations.

| Level | Points | Descriptor |
|---|---:|---|
| Full achievement | 30 | The selected kernel runs the required setup and data-loading code. Actual Python and relevant package versions are recorded, and the dependency file specifies a usable environment for that route. No undocumented dependency is needed. Live-only packages are not required for the snapshot route. |
| Solid achievement | 24 | The required code runs in the selected kernel and relevant versions are evidenced. The dependency specification has one minor omission or mismatch that can be resolved from the submitted information without guessing which package or version is needed. |
| Basic achievement | 18 | The student's working kernel and core setup/data checks are evidenced, but the dependency file or version record is incomplete enough that another person must determine missing environment details before recreating it. |
| Limited evidence | 9 | There is genuine evidence of a setup attempt and the specific blocker is identified, but a kernel or required dependency issue prevents the core setup/data checks from running. Alternatively, only a subset of the required environment checks is evidenced. |
| No assessable evidence | 0 | No usable evidence of the student's working environment or a specific setup attempt is provided. Supplied instructions or unsubstantiated success claims alone are not evidence. |

## C2 · Repository hygiene and handoff · 30 points

Repository/commit, file organisation, README entry points and a clean submission package. The number of commits and visual styling are not assessed; technical correctness of the execution procedure is assessed in C3.

| Level | Points | Descriptor |
|---|---:|---|
| Full achievement | 30 | Git records the submitted code and explanations, and the submitted commit is identifiable and accessible or supported by a history export if access is blocked. Required files and the root marker are present in a clear layout. README entry points are easy to locate. The ZIP matches the declared submission and excludes secrets, private information, installed environments and unnecessary caches. |
| Solid achievement | 24 | Git history and the submitted version are identifiable, and all required files are locatable. A minor organisation, naming or packaging inconsistency remains, but it does not obscure the submitted version or omit a runtime file. No sensitive content is included. |
| Basic achievement | 18 | A real Git record and the main files are available, but repository/ZIP correspondence, entry points or file organisation is unclear enough to require clarification. The package is still substantially inspectable and contains no sensitive content. |
| Limited evidence | 9 | Some relevant files can be inspected, but there is no evidenced Git record, the submitted version cannot be identified, or essential handoff files are missing. A folder named 'repo' alone is not version control. A package containing secrets or private information cannot meet the higher anchors and requires prompt private remediation. |
| No assessable evidence | 0 | No inspectable repository or meaningful submission package is available; links and files do not provide access to the work being assessed. |

## C3 · Reproducibility and source evidence · 25 points

Executed notebooks, portable run instructions, saved evidence outputs, source/manifest information and the Source and Check notes. A successful live API connection is neither necessary nor sufficient for full achievement.

| Level | Points | Descriptor |
|---|---:|---|
| Full achievement | 25 | Both notebooks have coherent saved outputs from the student's documented restart/run-all check. The supplied procedure and relative paths permit repetition with the declared environment and real-data source. Seed 414 is used where relevant. Results and laps have truthful separate provenance and row definitions; one actual check is correctly explained with a limitation. Stable evidence is consistent across the reported run/repeat comparison, allowing for timestamps. Required source files and final outputs can be traced. |
| Solid achievement | 20 | The core procedure can be repeated and outputs agree with the declared real-data route. Source labels, seed and actual check interpretation are correct. A minor omission in a row definition, limitation or evidence cross-reference remains, without misleading the reader about the origin or result. |
| Basic achievement | 15 | Own saved outputs establish a coherent core run and identify the real-data origin, but the restart/run-all account, portable procedure or explanation of a check/row unit is incomplete and requires clarification. There is no false claim that a cache proves live access or that invented data are real. |
| Limited evidence | 7.5 | Some own execution/check evidence exists, but a complete repeatable run is not evidenced or a material source, result or row-unit confusion remains. Friday synthetic-only practice, unexplained mixed real/synthetic records or outputs not linked to the submitted code cannot establish the full required real-data run. Credit the verifiable part, not a claim of success. |
| No assessable evidence | 0 | No verifiable own execution or check evidence is provided. Blank outputs, unchanged supplied examples without own run evidence, or statements unsupported by any usable result do not demonstrate reproduction. |

## C4 · AI-use disclosure and verification · 15 points

AI-use header/PROMPTS record plus the Decision and verification note. A truthful no-use route can attain every level, including full marks; no prompt count, paid tool or fabricated rejection is required.

| Level | Points | Descriptor |
|---|---:|---|
| Full achievement | 15 | If AI was used, the record identifies the tool/purpose and meaningful assistance, explains what was accepted or changed and why, and links a verification with an observed result and limit to the student's work. If AI was not used, the record states this honestly and references the student's own decision, reason and verification/limit in the evidence notes. Existing notebook answers may be cross-referenced; no duplicate report is required. |
| Solid achievement | 12 | Use or no use is explicit, a concrete own decision is explained, and verification is linked to an actual output. One minor detail of the assistance description, rationale or limitation is incomplete, but the account remains traceable and specific. |
| Basic achievement | 9 | Use or no use is explicit and the record identifies a specific decision and check, but the rationale, observed verification result or evidence reference is incomplete enough to require clarification. |
| Limited evidence | 4.5 | Use or no use is declared, but the rest is generic or unverified: for example, 'I checked it' without a check/result reference, an unedited template, or a transcript without an explanation of the student's decisions. |
| No assessable evidence | 0 | There is no assessable use/no-use disclosure and no traceable account of the student's decision and verification. Do not infer undisclosed AI use solely from writing style. |

## Fair and consistent scoring

- Assess each criterion independently; do not add global caps or an extra penalty for the same defect. A dependency failure is assessed in C1; C3 is judged on the available reproduction evidence, not an automatic duplicate deduction.
- No full marks for unevidenced execution; no automatic zero for a warning, failed live API request or honest diagnosis.
- Snapshots and real-data caches are eligible for full marks without attempting live access. Grade the declared route, not network availability or matching the lecturer's exact versions.
- No additional oral verification, mandatory video, model training, predictive metrics, F1 trivia, prompt quotas or commit quotas.
- Use the same evidence expectations with concise bullets or notebook annotations; no grammar or presentation-style criterion.
- Treat integrity/security concerns through private course procedures, not automated allegations, AI detectors or undeclared grade sanctions.

## Conversion to the 1–7 grade

For total points P: grade = 1.0 + 3.0 × P / 60 up to 60 points; above 60, grade = 4.0 + 3.0 × (P − 60) / 40.

**0 → 1.0 · 60 → 4.0 · 80 → 5.5 · 100 → 7.0.** The pass threshold is 60 points in total. Keep full precision before any institutional display rounding. The converted Lab 0 grade contributes 3% of NP.

Feedback identifies the evidence supporting each criterion and a next step. Use it to improve the environment/runbook reused in Lab 1; no additional Lab 0 submission is required.
