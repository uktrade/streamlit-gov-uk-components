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


_gov_uk_checkbox_list = components.declare_component("gov_uk_checkbox_list", **_component_options('frontend_checkbox_list'))

def gov_uk_checkbox_list(options, key=None, default=()):
    return tuple(_gov_uk_checkbox_list(options=options, key=key, default=default))


_gov_uk_checkbox_small = components.declare_component("gov_uk_checkbox_small", **_component_options('frontend_checkbox_small'))

def gov_uk_checkbox_small(label, id, key=None, default=False):
    return _gov_uk_checkbox_small(label=label, id=id, key=key, default=default)


_gov_uk_checkbox_small_list = components.declare_component("gov_uk_checkbox_small_list ", **_component_options('frontend_checkbox_small_list'))

def gov_uk_checkbox_small_list(options, key=None, default=()):
    return tuple(_gov_uk_checkbox_small_list(options=options, key=key, default=default))


_gov_uk_radio_list = components.declare_component("gov_uk_radio_list", **_component_options('frontend_radio_list'))

def gov_uk_radio_list(options, id, key=None, default=None):
    return _gov_uk_radio_list(options=options, id=id, key=key, default=default)
