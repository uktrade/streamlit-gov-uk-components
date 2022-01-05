import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox

st.subheader("Checkbox")

selected = gov_uk_checkbox("Waste from animal carcasses", "waste")
print('selected', selected)
st.markdown("Selected: %s" % selected)
