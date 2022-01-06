# streamlit-gov-uk-components

A collection of Streamlit components that use or are inspired by the GOV.UK Design System


## Installation

```bash
pip install streamlit-gov-uk-components
```

## Usage

### Checkbox

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

---

<img alt="Checkbox example" src="https://github.com/uktrade/streamlit-gov-uk-components/blob/main/example_checkbox.png?raw=true" width="306" height="44">

---


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
npm install
npm run start
```
