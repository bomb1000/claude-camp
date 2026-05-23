# Claude Camp Week 3 Practice

This folder contains three Week 3 data-processing projects. The work was done in
this existing folder instead of creating a new GitHub repository.

For a clearer visual walkthrough, open `week3_practice_summary.ipynb`. It shows
the three projects, sample outputs, validation behavior, and test status in one
notebook.

## Project 1: CSV Student Data Analyzer

Files:

- `project_1_csv_analyzer.py`
- `students.csv`
- `report.json`

What it does:

- Reads fake student data from `students.csv`
- Counts total students
- Counts students by country
- Calculates the completed bet rate
- Saves the result to `report.json`

Run:

```bash
python3 project_1_csv_analyzer.py
```

## Project 2: JSON Config Editor

Files:

- `project_2_config_editor.py`
- `config.json`

What it does:

- Reads user preferences from `config.json`
- Lets the user update one setting from the command line
- Validates supported settings before saving
- Saves changes back to `config.json`

Run with command-line arguments:

```bash
python3 project_2_config_editor.py theme dark
python3 project_2_config_editor.py font_size 20
```

Run interactively:

```bash
python3 project_2_config_editor.py
```

Validation examples:

- `theme` must be `light` or `dark`
- `language` must be `en`, `zh-TW`, or `zh-CN`
- `font_size` must be between `8` and `32`

## Project 3: String Utilities With Unit Tests

Files:

- `string_utils.py`
- `test_string_utils.py`

Functions:

- `reverse_words(s)`: reverses word order
- `count_vowels(s)`: counts English vowels
- `is_palindrome(s)`: checks whether text is a palindrome

Run tests:

```bash
python3 -m pytest test_string_utils.py
```

If `pytest` is not installed yet:

```bash
python3 -m pip install pytest
```

## Verification

The scripts were checked with:

```bash
python3 -m py_compile project_1_csv_analyzer.py project_2_config_editor.py string_utils.py test_string_utils.py
python3 project_1_csv_analyzer.py
python3 project_2_config_editor.py theme dark
python3 project_2_config_editor.py font_size 40
python3 -m pytest test_string_utils.py
python3 -m json.tool week3_practice_summary.ipynb
```

The pytest check was run in a temporary local virtual environment because this
machine's default Python did not already have `pytest` installed.

## Local Git Branch Workflow

Local branches used for this homework:

- `project-1-csv-analyzer`
- `project-2-json-config-editor`
- `project-3-string-utils-tests`

Each project branch was merged back into `main`. No new remote repository was
created, and nothing was pushed.
