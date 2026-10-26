# PulmoVision

PulmoVision is a browser-based thoracic and lung visualization application designed to explore lung anatomy, visualize pulmonary nodules, and interact with patient case data.

The project combines a 3D lung visualization interface with case-file importing, diagnostic display elements, and interactive controls.

## Features

- Interactive 3D lung visualization powered by Three.js.
- Lung and pulmonary nodule visualization.
- Tumor appearance and visualization controls.
- Virtual bronchoscopy depth control.
- Interactive view controls.
- Patient case selection and data importing.
- CSV and JSON case-file support.
- Diagnostic summary interface.
- Four-stage processing pipeline display.
- Illustrative Gompertz growth visualization.
- Intervention selection controls.
- Proposed solution and comparison sections.
- JSON template download.
- JSON report export.

## Project Structure

The repository is organized as follows:

```text
PulmoVision/
│
├── code/
│   └── PulmoVision_Final.html
│
├── datasets/
│   ├── README.md
│   ├── data_dictionary.csv
│   ├── patient_cases_test.csv
│   ├── patient_cases_test.json
│   ├── patient_cases_trial.csv
│   └── patient_cases_trial.json
│
├── docs/
│   ├── DATA_FORMAT.md
│   ├── INSTALLATION.md
│   ├── LICENSE
│   ├── LIMITATIONS.md
│   └── PROJECT_OVERVIEW.md
│
└── README.md
```

## Requirements

- A modern web browser such as Google Chrome, Firefox, Safari, or Microsoft Edge.
- WebGL support for 3D visualization.
- An internet connection for externally hosted Three.js and Google Fonts resources.
- Python 3 for running a local development server.

## Installation and Setup

### 1. Download the Repository

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Alternatively, download the repository as a ZIP file from GitHub and extract it to your computer.

### 2. Open the Project Folder

Navigate to the PulmoVision directory:

```bash
cd PulmoVision
```

### 3. Start a Local Server

Run the following command:

```bash
python3 -m http.server 8000
```

### 4. Launch PulmoVision

Open your web browser and visit:

http://localhost:8000/code/PulmoVision_Final.html

The application should now load in your browser.

## Dataset Overview

The `datasets/` directory contains the case files used to test the application's patient data import functionality.

| Dataset | Format | Records |
|---|---|---:|
| Trial cases | CSV | 1,200 |
| Trial cases | JSON | 1,200 |
| Test cases | CSV | 1,200 |
| Test cases | JSON | 1,200 |

The CSV and JSON versions contain corresponding records.

### Available Dataset Files

- `patient_cases_trial.csv`
- `patient_cases_trial.json`
- `patient_cases_test.csv`
- `patient_cases_test.json`
- `data_dictionary.csv`

The data dictionary describes the dataset fields, their meanings, and their expected formats.

## Data Fields

The case files use the following primary fields:

| Field | Description |
|---|---|
| `id` | Unique case identifier |
| `lobe` | Anatomical lung lobe |
| `diameter_mm` | Nodule diameter in millimetres |
| `hu` | Hounsfield unit measurement |
| `spiculation` | Spiculation value |
| `fev1_percent` | FEV1 percentage of predicted value |

### Supported Lung Lobe Values

- RUL — Right Upper Lobe
- RML — Right Middle Lobe
- RLL — Right Lower Lobe
- LUL — Left Upper Lobe
- LLL — Left Lower Lobe

For additional information, refer to:

- [Data Format](docs/DATA_FORMAT.md)
- [Data Dictionary](datasets/data_dictionary.csv)

## Importing Patient Cases

PulmoVision supports importing case files through its patient data interface.

To import a dataset:

1. Launch PulmoVision in your browser.
2. Locate the **Patient Data** section.
3. Select the case-file upload area.
4. Choose a CSV or JSON file from the `datasets/` directory.
5. Select an imported case using the application's case selector.

The application supports JSON arrays, JSON objects containing a `cases` array, individual JSON case objects, and CSV files with a header row.

## Application Overview

The application interface includes several visualization and interaction components:

### 3D Lung Visualization
Provides an interactive representation of lung anatomy and pulmonary nodules.

### Patient Data Interface
Allows users to import and select case files for visualization.

### Diagnostic Summary
Displays case-related information through the application's diagnostic interface.

### Visualization Controls
Provides controls for adjusting views, tumor appearance, and bronchoscopy depth.

### Growth Visualization
Includes an illustrative Gompertz growth model display.

### Intervention Interface
Contains intervention selectors and proposed-solution comparison sections.

## Documentation

Additional project documentation is available in the `docs/` directory.

| Document | Description |
|---|---|
| `INSTALLATION.md` | Installation and application setup |
| `DATA_FORMAT.md` | Dataset structure and supported fields |
| `LIMITATIONS.md` | Current application limitations |
| `PROJECT_OVERVIEW.md` | General project description |
| `LICENSE` | Licensing information |

## Development

When making changes to PulmoVision:

- Preserve the existing application functionality.
- Maintain compatibility with the supported CSV and JSON formats.
- Keep dataset field names consistent with the application import logic.
- Update the data dictionary when dataset fields change.
- Test the application after modifying its source code.
- Keep documentation consistent with the current repository structure.

## License

Refer to the `docs/LICENSE` file for licensing information.

## Project

**PulmoVision**

Thoracic and Lung Visualization Application

