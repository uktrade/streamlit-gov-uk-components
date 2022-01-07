import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox_small_list

st.subheader("Checkbox list")

selected = gov_uk_checkbox_small_list(
    # Dictionary of (id: label) pairs
    options={
        "hm-revenue-and-customs": "HM Revenue and Customs (HMRC)",
        "employment-tribunal": "Employment Tribunal",
        "ministry-of-defence": "Ministry of Defence",
        "department-for-transport": "Department for Transport",
    },
    key="waste",
    # Dictionary of (id: initially selected) pairs
    default={
        "hm-revenue-and-customs": True,
        "employment-tribunal": False,
        "ministry-of-defence": False,
        "department-for-transport": False,
    },
)
st.markdown("Selected: %s" % selected)
