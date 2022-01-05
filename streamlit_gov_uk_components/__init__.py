import os
import streamlit.components.v1 as components

_DEV = os.environ.get('STREAMLIT_GOV_UK_COMPONENTS_DEV')
_component_options = {
    "url": "http://localhost:3001",
} if _DEV else {
    "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend_checkbox/build")
}

_gov_uk_checkbox= components.declare_component("gov_uk_checkbox", **_component_options)

def gov_uk_checkbox(label, id, key=None, default=False):
    return _gov_uk_checkbox(label=label, id=id, key=key, default=default)
