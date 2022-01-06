# streamlit-gov-uk-components

A collection of Streamlit components that use or are inspired by the GOV.UK Design System


## Installation

```bash
pip install streamlit-gov-uk-components
```

## Usage

### Checkbox

```python
from streamlit_gov_uk_components import gov_uk_checkbox

checked = gov_uk_checkbox(
    label="Waste from animal carcasses",  # Label shown in browser
    id="waste-from-animal-carcases",      # ID of checkbox in HTML
    key="waste-from-animal-carcases",     # Streamlit component instance key
    default=True,                         # Initially selected: True == selected
)
st.markdown("Selected: %s" % checked)     # Show state in browser if needed
```
