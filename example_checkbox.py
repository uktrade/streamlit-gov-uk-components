import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox

st.subheader("Checkbox")

selected = gov_uk_checkbox("Waste from animal carcasses", "animal-waste", default=True)
st.markdown("Selected: %s" % selected)

selected = gov_uk_checkbox("Waste from mines or quarries", "mines-waste", default=False)
st.markdown("Selected: %s" % selected)
