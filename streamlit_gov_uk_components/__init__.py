import os
import streamlit.components.v1 as components

_DEV = not os.environ.get('DEV')

_gov_uk_checkbox= components.declare_component("gov_uk_components_checkbox",
    **({
        "url": "http://localhost:3001",
    } if _DEV else {
        "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend_checkbox/build")
    })
)

def gov_uk_checkbox(name, key=None):
    return _gov_uk_checkbox(name=name, key=key, default=0)
