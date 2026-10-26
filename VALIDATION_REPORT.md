# Validation report

Validation was executed while preparing this repository on 2026-10-26.

## Dataset validation

Command:

```bash
python3 scripts/validate_datasets.py
```

Exit code: 0

```text
PASS: CSV and JSON parse successfully.
PASS: trial pair contains 1200 matching records.
PASS: test pair contains 1200 matching records.
PASS: required fields, types, ranges, and lobe values are valid.
PASS: identifiers are unique and trial/test IDs do not overlap.
PASS: CSV/JSON records match record-for-record.
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 718, in _warm_feature_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 509, in _warm_drawing_and_image_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/generated/interface/models.py", line 32861, in bring_to_front
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/remote.py", line 764, in __call__
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/client.py", line 175, in call
artifact_tool.rpc.client.RemoteError: Element ordering requires an owning element collection.
```

## Automated unit tests

Command:

```bash
python3 -m unittest discover -s tests -v
```

Exit code: 0

```text
Spreadsheet runtime warmup failed during python startup
Traceback (most recent call last):
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/patches/warm_spreadsheet_runtime_on_startup.py", line 26, in warm_spreadsheet_runtime_on_startup
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 785, in warm_spreadsheet_runtime
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 718, in _warm_feature_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/spreadsheet_warmup.py", line 509, in _warm_drawing_and_image_flows
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/generated/interface/models.py", line 32861, in bring_to_front
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/remote.py", line 764, in __call__
  File "/tmp/tmp.QlpUkOUI9D/artifact_tool_v2-2.8.66/artifact_tool/rpc/client.py", line 175, in call
artifact_tool.rpc.client.RemoteError: Element ordering requires an owning element collection.
test_schema_fields_are_importer_compatible (test_datasets.DatasetValidationTests.test_schema_fields_are_importer_compatible) ... ok
test_test_pair_has_at_least_1000_matching_rows (test_datasets.DatasetValidationTests.test_test_pair_has_at_least_1000_matching_rows) ... ok
test_trial_and_test_ids_are_disjoint (test_datasets.DatasetValidationTests.test_trial_and_test_ids_are_disjoint) ... ok
test_trial_pair_has_at_least_1000_matching_rows (test_datasets.DatasetValidationTests.test_trial_pair_has_at_least_1000_matching_rows) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.092s

OK
```

## JavaScript syntax check

The three inline JavaScript blocks in the preserved HTML were extracted and checked with Node.js 22 using `node --check`. All three syntax checks exited successfully. This is a syntax check only, not a browser-based interaction test.

## Checks covered

- CSV and JSON syntax parsing.
- At least 1,000 records in each file.
- Required field names and field sets.
- CSV/JSON equality record-for-record and in the same order.
- Unique, non-empty identifiers within each split.
- No identifier overlap between trial and test.
- Valid lobe codes and numeric values.
- Numeric ranges for diameter, attenuation, spiculation, and FEV1.
- Unit tests for minimum counts, pair consistency, split separation, and importer-compatible schema.

## Application compatibility review

The original uploaded HTML was copied byte-for-byte to `index.html`. Its import code was inspected. The example files use the direct field names read by `addCase`: `id`, `lobe`, `diameter_mm`, `hu`, `spiculation`, and `fev1_percent`. The app's JSON/CSV parsing behavior and aliases are described in `DATA_FORMAT.md`.

## Checks not performed

- No automated browser-based end-to-end interaction test was run.
- No clinical validation, clinical-data provenance review, or medical-device assessment was performed.
- No offline/CDN-independent launch test was performed.
- No independent legal review of copyright or third-party asset licensing was performed.

The dataset and unit-test results above are command output, not estimates. The source HTML was preserved without application-code edits.
