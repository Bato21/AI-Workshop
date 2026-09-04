# Friday runbook · F1 data ecosystem · v1

Friday 4 September 2026, 11:10–13:40. No previous F1 knowledge is required.

## Open the complete folder

Extract the student package into a new folder, preserving its structure. Open the notebook at `unit_I/week_01/W01_Fri_f1_data_ecosystem_v1.ipynb`. Do not download the notebook alone: it uses the helper beside it, the `.iit414w-root` marker and the provided snapshots.

If you already have Thursday's project, copy the new versioned files and `data/samples/w01_fri_v1/` into that project without replacing your own work. The provided package is self-contained for Friday; it does not include your Thursday answers.

## Dependencies

Use your course Python environment, not a random kernel. Python 3.10+ is the existing setup baseline; Python 3.12.4 is the environment tested for this release. The exact observed package versions are recorded in `requirements_w01_fri_v1.txt`.

In a terminal using that environment, if packages are missing, deliberately run:

```text
python -m pip install -r requirements_w01_fri_v1.txt
python -m ipykernel install --user --name iit414w --display-name "Python (IIT414W)"
```

Select that kernel in your notebook editor. These commands change your environment; the notebook does not run them for you. If you cannot install software, ask for help. Do not claim that your own environment works because a partner's does.

For snapshot/synthetic mode, the notebook needs pandas and a working Jupyter/IPython kernel; requests and FastF1 are only needed for the live route. No API token is required or requested by these teaching materials.

## Three explicit modes

In the mode cell, choose:

- `MODE = "live"`: attempts Jolpica and the FastF1 session loader. On failure, it prints the failure category and uses a verified snapshot; if the snapshot also fails, it labels synthetic records clearly.
- `MODE = "snapshot"`: uses the provided source copies and SHA-256 checks. No live API success is implied.
- `MODE = "synthetic"`: generates small invented teaching tables using seed 414. They are not actual Monza data or evidence of API access.

If a live request stalls, interrupt execution, switch to `snapshot`, restart the kernel and run from the beginning. Do not repeatedly restart live downloads. For HTTP 429, stop sending requests. For a certificate error, do not disable TLS validation; use the snapshot and request technical help.

The results and lap table report provenance independently. If one is real and the other synthetic, do not combine them as records of the same race.

## Work and save

1. Read each block before running it. Keep written instructions available while the lecturer helps others.
2. Run in order. Inspect the source label, columns, row counts and computed checks.
3. Add your own explanations and independent check; they are deliberately blank.
4. Run the export cell. Each execution writes a new folder in `outputs/w01_fri_<timestamp>_<id>/` containing results, laps, checks and `run_manifest.json`.
5. After feedback, make one justified correction or document why no correction was needed.
6. Restart the kernel and run all cells. Compare data hashes for unchanged snapshot input; folder names and timestamps will differ. The manifest cannot certify that you personally restarted the kernel.
7. Keep your runbook and dependency file with the code. Document your own changes through Git as part of Lab 0; this notebook does not initialize a repository or create commits.

## If you cannot run Python

Keep the status BLOCKED and record the missing step. Use the readable CSV snapshots and data dictionary with a partner or the lecturer's demonstration. Write your own row definition, check interpretation and next action. This is a learning contingency, not a substitute for demonstrating your own reproducible setup in Lab 0.

## Next steps

The diagnostic closes Friday 4 September at 23:59. Lab 0 is individual, 3% of NP, due Thursday 10 September at 12:30. Read the separate Lab 0 brief. Complete the Friday exit ticket through the actual published course link; no new deadline or bonus percentage is set by this runbook.
