import os
import streamlit.components.v1 as components

_DEV = os.environ.get('GOV_UK_COMPONENTS_DEV')
_component_options = {
    "url": "http://localhost:3001",
} if GOV_UK_COMPONENTS_DEV else {
    "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend_checkbox/build")
}

_gov_uk_checkbox= components.declare_component("gov_uk_components_checkbox", **_component_options)

def gov_uk_checkbox(name, key=None):
    return _gov_uk_checkbox(name=name, key=key, default=0)
