import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox_list

st.subheader("Checkbox list")

selected = gov_uk_checkbox_list(
    # Dictionary of (id: label) pairs
    options=(
        ("waste-from-animal-carcusses", "Waste from animal carcasses"),
        ("waste-from-mines-or-quarries", "Waste from mines or quarries"),
        ("farm-or-agricultural-waste", "Farm or agricultural wastes"),
    ),
    key="waste",
    # Tuple of initially selected IDs
    default=("waste-from-animal-carcusses",),
)
st.markdown(f"Selected: {selected}")
