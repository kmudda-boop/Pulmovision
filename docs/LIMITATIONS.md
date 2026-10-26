# Limitations and intended use

PulmoVision is a visualization and research-prototype application. It is not a medical device, diagnostic service, treatment planner, or substitute for evaluation by qualified healthcare professionals.

## Synthetic example records

The trial and test files are generated synthetic software fixtures. They are not actual patient observations, measurements, chart abstractions, clinical-trial data, or registry data. Plausible-looking numeric formats do not establish clinical provenance or validity.

## Illustrative calculations and interface outputs

The source displays a heuristic malignancy score, a Gompertz-style growth visualization, treatment/intervention scenarios, a diagnostic summary, and proposed solutions. The interface itself describes the malignancy score as a demo heuristic and the regression/growth parameters as illustrative. These outputs have not been clinically validated by this repository. They must not be interpreted as diagnostic accuracy, prognosis, treatment response, efficacy, or evidence of patient benefit.

The four-stage pipeline indicator is a timed progression in the interface code. Its animation alone does not establish that an independently validated clinical computation has been performed.

## Appropriate use

Use the included files to test file import, case selection, visualization controls, and repository data tooling. Do not use the files or outputs for patient care, clinical decision-making, scientific inference, clinical model training, or claims about treatment outcomes.

## Technical limitations

- Three.js and web fonts are loaded from external CDNs; offline use requires those resources to be available locally and the HTML references to be updated deliberately.
- The CSV importer uses basic comma splitting rather than a standards-complete CSV parser.
- Browser rendering quality depends on WebGL support and device capabilities.
- The repository does not include an automated end-to-end browser test or clinical validation study.
