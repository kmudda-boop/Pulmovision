# Installation and launch

## Browser requirements

Use a current desktop browser with WebGL enabled. The application is a static HTML page and does not require a backend server for its built-in interface.

## Launch locally

From the repository root:

```bash
python3 -m http.server 8000
```

Open <http://localhost:8000> in the browser. Stop the server with Ctrl+C.

Opening `index.html` directly may work in some browsers, but serving it over HTTP is the recommended method.

## External resources

The supplied HTML references Three.js r128 from `cdnjs.cloudflare.com` and Inter/JetBrains Mono fonts from Google Fonts. Internet access is needed to retrieve those resources. No package manager or JavaScript build step is included.

## Dataset utilities

Python 3.9 or later is recommended. The generator, validator, and tests use only the Python standard library.

```bash
python3 scripts/generate_datasets.py
python3 scripts/validate_datasets.py
python3 -m unittest discover -s tests -v
```
