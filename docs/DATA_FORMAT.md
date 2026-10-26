# Data format and application compatibility

## Import behavior inspected in source

The supplied `index.html` implements `readFile`, `parseCSV`, and `addCase` in its application script.

- A `.csv` file is parsed as comma-separated lines. The first row is lowercased and treated as the header.
- Other accepted files are parsed as JSON. The JSON value may be an array, an object containing a `cases` array, or a single case object.
- Each imported object is converted into the application's internal case representation.
- `id` is accepted as a fallback for `name`; `location` is accepted as a fallback for `lobe`.
- `diameter` and `d` are accepted as aliases for `diameter_mm`; `mean_hu` for `hu`; `sp` for `spiculation`; and `fev1` for `fev1_percent`.

## Included schema

| Field | Type | Constraints in supplied files | Units | Meaning |
|---|---|---|---|---|
| `id` | string | Non-empty; unique within each split | none | Demonstration case identifier; app uses it as display-name fallback |
| `lobe` | string | `RUL`, `RML`, `RLL`, `LUL`, or `LLL` | none | Lung lobe code |
| `diameter_mm` | number | 4.0-70.0 | mm | Illustrative diameter input |
| `hu` | integer | -850 to 120 in generated files; validator permits -1000 to 300 | HU | Illustrative attenuation input |
| `spiculation` | number | 0.00-1.00 | unitless fraction | Illustrative spiculation input |
| `fev1_percent` | number | 35.0-130.0 in generated files; validator permits 0-200 | percent predicted | Illustrative FEV1 input |

The authoritative machine-readable field list is `datasets/data_dictionary.csv`.

## Example JSON record

```json
{
  "id": "PV-TRIAL-0001",
  "lobe": "RLL",
  "diameter_mm": 22.4,
  "hu": -125,
  "spiculation": 0.62,
  "fev1_percent": 86.5
}
```

The exact values above are an illustrative format example, not a patient observation.

## CSV requirements and caveats

The current parser is intentionally simple: it splits each line on commas and trims whitespace. It does not implement full RFC 4180 quoting semantics. Keep included field values free of commas and line breaks. Header matching is lowercased, and all six fields are present in the distributed examples.

## App-side coercion and defaults

The application converts numeric inputs using JavaScript numeric coercion. It clamps diameter to 4-70 mm and spiculation to 0-1. Missing or empty values may fall back to defaults in the app; the repository validator is stricter and rejects missing required fields. The app's `position` field is optional; when omitted, the application derives a default position from the selected lobe. It is not included in the example schema because it is not needed for import compatibility.

## No unsupported extension fields

No extension fields are included. If fields are added later, first inspect the application parser and update the dictionary and tests together.
