# Project Log

## 2026-05-23

Week 3 homework was completed inside this existing folder, per the user's
request. A new GitHub repository was not created.

Completed:

- Project 1 CSV student data analyzer with sample `students.csv` and generated
  `report.json`
- Project 2 JSON config editor with command-line and interactive update modes
- Project 3 string utility library with pytest coverage for normal, edge, and
  error cases
- README with project descriptions, run commands, test command, and local branch
  workflow notes
- Jupyter Notebook summary at `week3_practice_summary.ipynb` for reviewing all
  three project outputs in one place

Verification:

- `python3 -m py_compile project_1_csv_analyzer.py project_2_config_editor.py string_utils.py test_string_utils.py`
- `python3 project_1_csv_analyzer.py`
- `python3 project_2_config_editor.py theme dark`
- `python3 project_2_config_editor.py font_size 40`
- `/tmp/claude-camp-w03-pytest-venv/bin/python -m pytest test_string_utils.py`
- `python3 -m json.tool week3_practice_summary.ipynb`

Notes:

- The default system Python did not have `pytest`, so pytest was installed only
  in a temporary virtual environment under `/tmp`.
- The work is local only. It has not been pushed to GitHub.
