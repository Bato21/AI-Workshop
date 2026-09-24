# Start here · Thursday 10 September

Open `W02_Thu_decision_eda_prediction_update_v1.ipynb` from the complete extracted folder. Keep your original prediction card beside it. The notebook and this guide work with local files; you do not need live F1 access.

1. Extract the complete ZIP. Do not open the notebook inside the ZIP.
2. Keep `.iit414w-root`, `unit_I/`, `data/` and `requirements_w02_thu_v1.txt` together.
3. Select the Python kernel you used in Week 1. Work on your own copy.
4. Copy the original two-race forecast before opening the result discussion. Leave unavailable values empty.
5. Run cells in order. Pause for the written prompts; empty responses do not cause Run All to fail.
6. Use `MODE = "snapshot"` for the real historical data. A hash error means a source file is missing or changed: restore the original package.
7. Run the final export, then save the notebook. New outputs appear in a unique `outputs/w02_thu_.../` folder. Original and updated predictions are separate fields.

If your existing environment lacks dependencies, use the terminal from the package root. Installation needs internet once; running the class notebook afterwards does not:

```text
python -m pip install -r requirements_w02_thu_v1.txt
python -m ipykernel install --user --name iit414w-w02 --display-name "Python (IIT414W W02)"
python -m notebook
```

The demonstrated setup was Python 3.12.4, pandas 2.3.1, numpy 1.26.4 and matplotlib 3.10.3. Other environments may work but were not all tested. No installation commands execute inside the notebook. FastF1 and requests are not needed.

## If something fails

| Symptom | Action |
|---|---|
| Missing module | Select the correct kernel; install dependencies only if needed |
| Root marker missing | Re-extract the whole ZIP; hidden files must be included |
| Missing or changed CSV | Restore the source snapshot; do not change the hash to bypass the check |
| No internet | Continue normally with snapshot data |
| Historical snapshot unusable | Tell the lecturer, then explicitly use `MODE = "synthetic"` for fictional EDA practice; label all resulting claims accordingly |
| Italy observation missing | Restore its real-data CSV. It is not replaced with invented race results |
| No working Python | Use the prediction handout, the local HTML reading copy and the CSV tables. Write answers separately; this does not certify a working environment |

`IIT414W_W02_Thu_ReadingCopy_v1.html` is an executed demonstration for reading, not an interactive notebook. Its personal responses are blank. Tables and figures are embedded; links to external sources are optional provenance references.

## Data scopes

The historical CSVs cover available qualifying and race-result records for 2019–2021. One row is a driver in one race. The three result rows without qualifying records remain in the analysis. The dataset is not a complete Lab 1 train/calibration/test package.

The four-row Italy 2026 extract and original W01 shared evidence are separate forecasting context. The final target is new Ferrari-minus-McLaren points in Italy plus Spain. No Spain outcome is included. A snapshot proves which data you used; it does not prove a live download or the quality of your reasoning.

Record actual AI assistance and verification, or an honest no-use statement. Do not invent failures, revisions or prompts. Keep the work for Friday; there is no new graded submission attached to this notebook.
