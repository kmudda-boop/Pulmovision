# Example datasets

This directory contains two synthetic PulmoVision application-testing datasets.

- `patient_cases_trial.csv` and `patient_cases_trial.json`: 1,200 records in each format.
- `patient_cases_test.csv` and `patient_cases_test.json`: 1,200 records in each format.
- `data_dictionary.csv`: field definitions, types, ranges, units, meanings, and importer notes.

Each pair contains equivalent records in the same order. The importer accepts `id`, `lobe`, `diameter_mm`, `hu`, `spiculation`, and `fev1_percent`. To import a file, launch the app and use the Patient data file drop area.
