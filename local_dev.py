import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox

st.subheader("Component with constant args")

num_clicks = gov_uk_checkbox("World")
st.markdown("You've clicked %s times!" % int(num_clicks))

st.markdown("---")
st.subheader("Component with variable args")

name_input = st.text_input("Enter a name", value="Streamlit")
num_clicks = gov_uk_checkbox(name_input, key="foo")
st.markdown("You've clicked %s times!" % int(num_clicks))
