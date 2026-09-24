# Friday 11 September · Three cases

Extract the entire ZIP. Start with [the student casebook](IIT414W_W02_Fri_ThreeCases_Student_v1.html), then open [the notebook](unit_I/week_02/W02_Fri_three_cases_students_v1.ipynb).

The casebook works without Python or internet. All figures are embedded. View B for Case 3 opens only when you choose to reveal it. Record your first judgement before doing so. The Markdown copy and image files are also included.

In the notebook, use your Week 1/Thursday Python environment: pandas, numpy, matplotlib and Jupyter. If imports fail, select the correct kernel. Install from `requirements_w02_fri_v1.txt` only if your environment needs it; installation requires internet once. No packages install and no data downloads occur inside the notebook.

```text
python -m pip install -r requirements_w02_fri_v1.txt
python -m notebook
```

Keep `.iit414w-root`, `unit_I/` and `data/` together. Do not run the notebook inside the ZIP. `MODE="snapshot"` uses the real data. If the source files are missing or altered, restore the ZIP. The explicit `synthetic` mode is a fictional-data contingency: it will produce different numbers and cannot support empirical F1 conclusions. There is no silent fallback.

`YEAR=2021` matches the casebook. Changing it is an optional sensitivity exercise, not the same numerical case. The source contains 2019–2021 development data only. All points are race-result points, excluding separate Sprint scoring. Do not use the cumulative curves as official championship standings.

Case 1 and Case 2 contain open cells for your checks. View B in Case 3 is controlled by `REVEAL_CASE3=False`; record your judgement, change it to `True` and rerun that cell. Run All can complete with personal responses blank. That does not constitute a completed audit.

The last cell saves computed stimulus tables and your response fields in a new `outputs/w02_fri_.../` directory. Save the notebook too, including any audit code and Markdown you added. Keep original judgements and revisions separate. This is formative work, not a new graded submission.
