import os
import streamlit.components.v1 as components

_DEV = os.environ.get('STREAMLIT_GOV_UK_COMPONENTS_DEV')

def _component_options(path):
    return{
        "url": "http://localhost:3001",
    } if _DEV else {
        "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), path + "/build")
    }

_gov_uk_checkbox = components.declare_component("gov_uk_checkbox",  **_component_options('frontend_checkbox'))

def gov_uk_checkbox(label, id, key=None, default=False):
    return _gov_uk_checkbox(label=label, id=id, key=key, default=default)


_gov_uk_checkbox_small = components.declare_component("gov_uk_checkbox_small", **_component_options('frontend_checkbox_small'))

def gov_uk_checkbox_small(label, id, key=None, default=False):
    return _gov_uk_checkbox_small(label=label, id=id, key=key, default=default)
