import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox

st.subheader("Checkbox")

selected_waste_from_animal_carcases = gov_uk_checkbox(
    label="Waste from animal carcasses",
    id="waste-from-animal-carcasses",
    key="waste-from-animal-carcasses",
    default=True,
)
st.markdown("Selected: %s" % selected_waste_from_animal_carcases)

selected_waste_from_mines_or_quarries = gov_uk_checkbox(
    label="Waste from mines or quarries",
    id="waste-from-mines-or-quarries",
    key="waste-from-mines-or-quarries",
    default=False,
)
st.markdown("Selected: %s" % selected_waste_from_mines_or_quarries)
