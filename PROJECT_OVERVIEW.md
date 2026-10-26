# Project overview

## Application architecture

PulmoVision is delivered as a single self-contained HTML document. Its styles, application logic, and substantial embedded visualization data are retained in `index.html`. The page creates a Three.js scene in the visualization viewport and builds the patient-data controls and analytical display in the adjacent panel.

## Source-confirmed interface areas

- Patient-data import from CSV.
- Case selector and four-stage pipeline status display.
- Visualization layers, breathing-rate and opacity controls, and breathing pause control.
- Tumor rendering mode and color selection.
- Virtual bronchoscopy depth navigation and lesion focus/reset controls.
- Diagnostic summary with volume, RECIST diameter, mean density, T category, heuristic malignancy score, and location.
- Gompertz-style growth display with manual alpha/beta controls, intervention selection, treatment timing, and simulated month controls.
- Projected 12-month display, proposed solutions, and comparison area.

These are source-code and interface observations. They do not establish clinical validity or effectiveness.

## External dependency

The page loads Three.js r128 from `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js`. Google Fonts are referenced in the document head. These external resources require network access when not otherwise cached or locally hosted.

## Data flow

The file input and drag/drop handlers call the application's file-reading routine. JSON accepts an array, a `cases` array wrapper, or a single object. CSV uses a basic header-based parser. The imported fields are mapped to internal names and values in `addCase`. The supplied demonstration datasets use the fields accepted by that mapping.

## Repository utilities

The Python generator creates deterministic synthetic CSV/JSON pairs. The validator checks record counts, parsing, schema, numeric bounds, identifier uniqueness, pair equality, and split separation. Unit tests exercise the main dataset invariants.
