# streamlit-gov-uk-components

A collection of Streamlit components that use or are inspired by the GOV.UK Design System


## Installation

```bash
pip install streamlit-gov-uk-components
```

## Usage

### Checkbox ([example](./example_checkbox_small.py))

<img alt="Checkbox example" src="https://github.com/uktrade/streamlit-gov-uk-components/blob/main/example_checkbox.png?raw=true" width="306" height="44">

```python
import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox

selected = gov_uk_checkbox(
    label="Waste from animal carcasses",  # Label shown in browser
    id="waste-from-animal-carcases",      # ID of checkbox in HTML
    key="waste-from-animal-carcases",     # Streamlit component instance key
    default=True,                         # Initially selected?
)
```

### Smaller checkbox ([example](./example_checkbox_small.py))

<img alt="Smaller checkbox example" src="https://github.com/uktrade/streamlit-gov-uk-components/blob/main/example_checkbox_small.png?raw=true" width="342" height="30">

```python
import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox_small

selected = gov_uk_checkbox_small(
    label="HM Revenue and Customs (HMRC)",  # Label shown in browser
    id="hmrc",                              # ID of checkbox in HTML
    key="hmrc",                             # Streamlit component instance key
    default=True,                           # Initially selected?
)
```


## Local development

The examples serve as reasonable mini Streamlit applications that allow development of the components themselves. Two terminal session are typically needed.

One to run Streamlit itself...

```bash
pip install streamlit
STREAMLIT_GOV_UK_COMPONENTS_DEV=True streamlit run example_checkbox.py
```

... and one to run a development server that automatically recompiles and serves the HTML and Javascript of the front end of each component.

```bash
cd streamlit_gov_uk_components/frontend_checkbox
yarn install
./fix.sh
yarn run start
```

## Releasing to PyPI

1. Ensure that each frontend component has been built

   ```bash
   cd streamlit_gov_uk_components/frontend_checkbox
   yarn install
   ./fix.sh
   yarn run build
   ```

2. Ensure that there is a line in `MANIFEST.in` for each frontend component.

3. Bump the version inside `setup.py`

4. Commit with a Conventional Commit message with the bumped version, tag the commit with the bumped version, and push to GitHub.

   ```bash
   git add setup.py
   git commit -m "build(release): v0.0.4"
   git tag v0.0.4
   git push origin main --tags
   ```

5. Build and release to PyPI

   ```
   pip install build twine
   rm -r -f build dist && python -m build && python -m twine upload dist/*
   ```
