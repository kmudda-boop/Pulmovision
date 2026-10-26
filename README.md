# PulmoVision

PulmoVision is a browser-based thoracic and lung visualization prototype. This repository preserves the supplied single-page application and provides reproducible synthetic case files for exercising its JSON and CSV import workflow.

## Features present in the supplied application

The preserved source includes a Three.js lung visualization, interactive view controls, tumor appearance controls, a virtual bronchoscopy depth control, a four-stage pipeline display, a diagnostic summary, an illustrative Gompertz growth view, intervention selectors, proposed-solution and comparison areas, case-file import, a JSON template download, and a JSON report export.

These are descriptions of interface and source-code functionality, not claims of clinical validity. The pipeline display is a timed interface sequence; it should not be interpreted as a validated clinical processing pipeline.

## Screenshots

No screenshots are included. Add locally captured screenshots here when available.

## Requirements

- A modern desktop browser with WebGL support.
- Python 3.9 or later for dataset generation, validation, and tests (standard library only).
- Internet access for the externally hosted Three.js and Google Fonts resources used by the page. The embedded application data itself is stored in `index.html`.

## Installation and launch

1. Download or clone this repository.
2. Open `index.html` in a modern browser, or serve the directory over HTTP:

   ```bash
   python3 -m http.server 8000
   ```

3. Visit <http://localhost:8000>.

Serving over HTTP is recommended over opening the file directly. The page loads Three.js r128 from `cdnjs.cloudflare.com` and fonts from Google Fonts; those resources require network access unless separately made available.

## Repository structure

```text
PulmoVision/
├── index.html
├── README.md
├── LICENSE
├── .gitignore
├── datasets/
│   ├── README.md
│   ├── patient_cases_trial.csv
│   ├── patient_cases_trial.json
│   ├── patient_cases_test.csv
│   ├── patient_cases_test.json
│   └── data_dictionary.csv
├── docs/
│   ├── INSTALLATION.md
│   ├── DATA_FORMAT.md
│   ├── LIMITATIONS.md
│   ├── VALIDATION_REPORT.md
│   └── PROJECT_OVERVIEW.md
├── scripts/
│   ├── generate_datasets.py
│   └── validate_datasets.py
└── tests/
    └── test_datasets.py
```

## Example datasets

| File pair | Records per file | Purpose |
|---|---:|---|
| `patient_cases_trial.csv` and `.json` | 1,200 | Example import and interface testing |
| `patient_cases_test.csv` and `.json` | 1,200 | Separate example import and interface testing |

The CSV and JSON files in each pair contain the same records in the same order. Trial and test identifiers use separate prefixes and do not overlap. These are synthetic demonstration fixtures generated for software testing; they are not patient records, measurements, or clinical observations.

## Data schema

The app's import code accepts `id` as a fallback for `name`, along with `lobe`, `diameter_mm`, `hu`, `spiculation`, and `fev1_percent`. It also recognizes aliases including `location`, `diameter`, `d`, `mean_hu`, `sp`, and `fev1`. The included files use the direct field names listed above. See [docs/DATA_FORMAT.md](docs/DATA_FORMAT.md) and [datasets/data_dictionary.csv](datasets/data_dictionary.csv).

## Importing example files

1. Launch PulmoVision.
2. In the **Patient data** section, choose **Drop a case file** or click the file area.
3. Select one of the included `.json` or `.csv` files.
4. The application adds imported records to its case selector. Select a case as needed.

The importer accepts a JSON array, an object with a `cases` array, or a single JSON case object. CSV files must have a header row. The supplied CSV fields contain no commas, matching the simple comma-splitting parser in the current source.

## Regenerate and validate datasets

From the repository root:

```bash
python3 scripts/generate_datasets.py
python3 scripts/validate_datasets.py
python3 -m unittest discover -s tests -v
```

Generation uses a fixed seed (`20261026`) and writes 1,200 records to each split in both formats. Running the generator again recreates the same files.

## Tests

The unit tests check minimum row counts, CSV/JSON pair consistency, split identifier separation, and the expected importer-compatible field set. The validator additionally checks parsing, required fields, lobe values, numeric types, documented ranges, and identifier uniqueness. See [docs/VALIDATION_REPORT.md](docs/VALIDATION_REPORT.md) for the recorded run results.

## Limitations and intended use

PulmoVision is a visualization and research-prototype interface, not a medical device or a substitute for professional medical evaluation. Its heuristic score, growth curves, treatment scenarios, proposed solutions, and displayed metrics are illustrative. The synthetic example records exist only to exercise software import and display paths. They cannot establish diagnostic performance, clinical efficacy, treatment benefit, patient outcomes, or scientific conclusions. Do not use these files for patient care, model training intended for clinical use, or clinical inference.

## Contribution guidelines

- Preserve the original application and embedded resources unless a change is necessary and documented.
- Keep sample records synthetic and clearly labeled as demonstration data.
- Update the data dictionary and validation tests when changing the import schema.
- Run the generator, validator, and unit tests before submitting changes.
- Do not add patient-identifying information, credentials, or secrets.

## License

The supplied source did not include a verified license grant. The repository `LICENSE` file records this limitation and does not grant reuse rights. Confirm permissions with the relevant rights holders before redistribution or reuse.
