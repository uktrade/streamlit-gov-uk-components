import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox_list

st.subheader("Checkbox list")

selected = gov_uk_checkbox_list(
    # Dictionary of (id: label) pairs
    options={
        "waste-from-animal-carcusses": "Waste from animal carcasses",
        "waste-from-mines-or-quarries": "Waste from mines or quarries",
        "farm-or-agricultural-waste": "Farm or agricultural wastes",
    },
    key="waste",
    # Dictionary of (id,initially selected) pairs
    default={
        "waste-from-animal-carcusses": True,
        "waste-from-mines-or-quarries": False,
        "farm-or-agricultural-waste": False,
    },
)
st.markdown("Selected: %s" % selected)
