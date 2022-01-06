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
st.markdown("Selected: %s" % selected)    # Show state in browser
```

<img alt="Checkbox example" src="https://github.com/uktrade/streamlit-gov-uk-components/blob/main/example_checkbox.png?raw=true" width="315" height="261">
