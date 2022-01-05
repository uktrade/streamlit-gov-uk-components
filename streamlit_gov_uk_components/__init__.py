import os
import streamlit.components.v1 as components

_RELEASE = __name__ != '__main__'

_gov_uk_checkbox_func = components.declare_component("gov_uk_components_checkbox",
    **({
        "path": os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend_checkbox/build")
    } if _RELEASE else {
        "url": "http://localhost:3001",
    })
)

def gov_uk_checkbox(name, key=None):
    return _gov_uk_checkbox_func(name=name, key=key, default=0)

if not _RELEASE:
    import streamlit as st

    st.subheader("Component with constant args")

    # Create an instance of our component with a constant `name` arg, and
    # print its output value.
    num_clicks = gov_uk_checkbox("World")
    st.markdown("You've clicked %s times!" % int(num_clicks))

    st.markdown("---")
    st.subheader("Component with variable args")

    # Create a second instance of our component whose `name` arg will vary
    # based on a text_input widget.
    #
    # We use the special "key" argument to assign a fixed identity to this
    # component instance. By default, when a component's arguments change,
    # it is considered a new instance and will be re-mounted on the frontend
    # and lose its current state. In this case, we want to vary the component's
    # "name" argument without having it get recreated.
    name_input = st.text_input("Enter a name", value="Streamlit")
    num_clicks = gov_uk_checkbox(name_input, key="foo")
    st.markdown("You've clicked %s times!" % int(num_clicks))
