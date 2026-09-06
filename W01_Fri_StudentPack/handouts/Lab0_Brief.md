# Lab 0 · Reproducible setup

**Individual · 3% of the Coursework Grade (NP) · 100 rubric points**

**Start with Friday's class work, 4 September 2026. Due Thursday 10 September 2026 at 12:30, at the start of class. All times are Santiago local time.**

## 1. What you will demonstrate

Configure and explain a reproducible working environment: preserve the code and dependencies, run the provided notebooks yourself, and give another person enough information to repeat your checks. This is a setup lab, not a modelling competition.

Use the Thursday setup notebook and Friday data-check notebook as starting points. You are not expected to rewrite the supplied helper or create a new notebook from scratch. Keep the supplied code attribution and add your own outputs and explanations.

No prior Formula 1 knowledge is required. We assess technical evidence, not sports knowledge, visual polish, English grammar, typing speed, or the number of commits or AI prompts. There is no additional oral defence, video, or separate long report.

## 2. What to hand in

Submit **one ZIP package** through the Lab 0 Canvas assignment once it is available. Include the repository link and the submitted commit ID in the README. The lecturer must be able to access the repository; you do not need to make it public. If repository access is blocked, report this before the deadline and include a short Git history export in the ZIP so your work remains inspectable.

The package contains:

1. **Your two executed notebooks:** Thursday setup and Friday data checks, with your own responses and saved outputs.
2. **The files needed to rerun them:** the Friday helper, the `.iit414w-root` marker, required small data files and their source manifest. Preserve the original relative paths. The root marker can be hidden in your file explorer: check that it is included.
3. **An environment file:** `requirements.txt` or `environment.yml`, matching the packages used by your selected route, plus the Python version in the README. Do not include the installed environment itself.
4. **A short README/runbook:** setup commands, kernel selection, notebook order, data mode and source, where outputs are saved, the repository link and submitted commit ID, and the three evidence notes below.
5. **An AI-use header or `PROMPTS.md`:** actual assistance and verification, or a truthful no-use statement. One location is enough; do not duplicate the record.
6. **Your final small evidence outputs:** the Thursday setup evidence and the Friday exported tables, checks and `run_manifest.json`. Keep the final run, not every temporary run. If using repeat-run comparisons, preserve their results in the README or notebook.

Do not upload passwords, access tokens, private information, virtual environments, package installations, `__pycache__`, or large FastF1 caches. Do not include `.git` in the ZIP; the linked repository preserves the history. Inspect the ZIP before submitting it.

Equivalent clear filenames and folder layouts are acceptable. The existing course layout is recommended because the helper already uses it. The ZIP and the submitted commit should represent the same code and written explanations; identify generated output files separately if they are intentionally not tracked by Git.

## 3. Three short evidence notes

Put these in your README or reference existing notebook answers. A few clear sentences or bullets are enough; there is no word-count target.

- **Source:** Which route actually supplied the results and lap tables? State the event and what one row represents in each table. Distinguish source data, a stored copy, and invented teaching data.
- **Check:** Point to one check you ran, its observed result, what it establishes and one thing it does not establish. Reference the actual cell, output file or check name. A warning is not automatically a failed check.
- **Decision and verification:** Explain one setup or execution decision you made, why, and how you checked it. Include a correction after feedback or self-review when one was needed; if no correction was needed, state what you verified. Do not invent a failure or change.

These notes make the existing rubric evidence visible. They are not additional separately weighted criteria.

## 4. Data routes: equal opportunity for full marks

**Live API access is not required for full marks.** You can use the supplied real-data snapshots or an appropriate real-data cache and earn 100/100. No live attempt is required, and successful live access earns no bonus. The same quality standards apply to execution, provenance and explanation on every real-data route.

For the Friday notebook, `MODE = "snapshot"` is a complete assessed route using the provided Monza 2021 data. Include its small source files and manifest. Install the dependencies needed for that route; requests and FastF1 are optional when they are not used. You are not required to match the lecturer's exact package versions if your documented environment works.

`FASTF1_SESSION` means that the FastF1 session loader supplied the table. It does not prove a new network request: FastF1 may use cached data. State that distinction rather than claiming verified API access. Document results and laps separately because they may have different origins.

The Thursday synthetic seed exercise remains valid setup evidence. Friday's synthetic contingency is for practice: do not label it as actual race data or combine it with real results as though it described the same event. For the assessed Friday real-data evidence, use the supplied snapshots if live access fails. If neither route is usable, document the blocker and contact the lecturer; a partial run can show partial achievement but is not automatically a complete reproducible setup.

Do not disable certificate validation or put credentials into the notebooks to obtain data.

## 5. How to work from Friday to submission

1. Open your complete course folder and select the intended Python kernel. Use the Friday class to identify missing files or dependencies.
2. Run the notebooks in order. Keep the existing seed 414 where randomness is used, and record the actual route taken by each data loader.
3. Finish your own explanations. Reuse the relevant Friday responses; do not add a second report.
4. Apply useful feedback or a correction found during self-review. Record the decision and its verification briefly.
5. Restart the kernel and run all cells in each notebook, in the documented order. Save the resulting outputs. Compare stable outputs when repeating an unchanged snapshot run; timestamps and newly generated output-folder names are expected to differ. A manifest alone does not prove that you restarted the kernel.
6. Commit your code and explanations in Git. Check the repository access and that the ZIP contains the required files, including the root marker and data.
7. Use the self-checklist and submit the ZIP. Keep a copy of what you submitted.

If a dependency or path prevents execution, keep the error visible, describe what you tried and ask for help before the deadline. An honest diagnosis can earn credit where it meets a rubric descriptor; it is not a substitute for all execution evidence. Do not replace missing outputs with someone else's results or manually turn a failed check into PASS.

## 6. How it is assessed

| Criterion | Maximum points |
|---|---:|
| C1 · Environment and dependencies | 30 |
| C2 · Repository hygiene and handoff | 30 |
| C3 · Reproducibility and source evidence | 25 |
| C4 · AI-use disclosure and verification | 15 |
| Total | 100 |

The accompanying rubric defines five achievement levels for each criterion. Full achievement means that the required evidence is complete, coherent and usable; it does not require extra features.

There is no automatic overall-zero rule for a failed API request, one technical error, or a low score in a single criterion. Each criterion is assessed on its own evidence. Missing execution evidence cannot be awarded full credit merely because the files are present. Academic integrity issues follow the course procedures, not an AI detector or an automatic rubric penalty.

### Points to grade

Let `P` be the total rubric points out of 100:

- For `0 <= P <= 60`: `grade = 1.0 + 3.0 * P / 60`.
- For `60 < P <= 100`: `grade = 4.0 + 3.0 * (P - 60) / 40`.

Examples: **0 points = 1.0; 60 = 4.0; 80 = 5.5; 100 = 7.0.** The 60% threshold refers to the total score; there is no separate pass threshold per criterion. Preserve the full score before applying any institutional display-rounding rule. The resulting Lab 0 grade contributes 3% of NP.

## 7. AI, help and accessibility

AI assistance is permitted and optional. Record the tool, purpose, a prompt or faithful summary, what you used or changed, and a verification linked to your own evidence. State unknown model versions honestly. Record only meaningful assistance, not every keystroke. You do not need to invent rejected suggestions or use a paid tool.

If you did not use AI, say so. Point to your own decision and verification in the evidence notes; this route can receive full marks for C4. Reusing the lecturer's supplied code is not the same as personally using an AI tool; keep its attribution.

You may receive explanations and technical help, but run and describe your own work. Write in English; concise bullets or notebook annotations are acceptable instead of continuous prose. There is no timed individual verification. Contact the lecturer privately if an instruction, format or access barrier needs clarification; agreed support measures are handled individually without changing the learning criteria.

## 8. Feedback and related tasks

Feedback is scheduled through Canvas within five days of the deadline, as stated in the Academic Schedule. Use it to correct your environment or runbook before building on them in Lab 1; no additional Lab 0 resubmission or grade change is created by that feedback step.

The Pre-Course Diagnostic is a separate prerequisite for Lab 0 and is due Friday 4 September at 23:59. It does not add points to this rubric. The exit ticket is also separate. If the Lab 0 task or diagnostic access route is unavailable, tell the lecturer; you can still begin with these instructions and the supplied class files.
