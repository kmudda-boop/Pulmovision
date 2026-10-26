# Limitations and intended use

PulmoVision is a visualization and research-prototype application. It is not a medical device, diagnostic service, treatment planner, or substitute for evaluation by qualified healthcare professionals.


## Illustrative calculations and interface outputs

The source displays a heuristic malignancy score, a Gompertz-style growth visualization, treatment/intervention scenarios, a diagnostic summary, and proposed solutions. The interface itself describes the malignancy score as a demo heuristic and the regression/growth parameters as illustrative. They must not be interpreted as diagnostic accuracy, prognosis, treatment response, efficacy, or evidence of patient benefit.

The four-stage pipeline indicator is a timed progression in the interface code. Its animation alone does not establish that an independently validated clinical computation has been performed.

## Appropriate use

Use the included files to test file import, case selection, visualization controls, and repository data tooling. 

## Technical limitations

- Three.js and web fonts are loaded from external CDNs; offline use requires those resources to be available locally and the HTML references to be updated deliberately.
- The CSV importer uses basic comma splitting rather than a standards-complete CSV parser.
- Browser rendering quality depends on WebGL support and device capabilities.
- The repository does not include an automated end-to-end browser test or clinical validation study.
