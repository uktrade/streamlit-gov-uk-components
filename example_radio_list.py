import streamlit as st
from streamlit_gov_uk_components import gov_uk_radio_list

st.subheader("Radio list")

selected = gov_uk_radio_list(
    # Tuple of (ID, label) pairs
    options=(
        ("england", "England"),
        ("scotland", "Scotland"),
        ("wales", "Wales"),
        ("northern-ireland", "Northern Ireland"),
    ),
    # ID of component
    id="where-do-you-live",
    # ID of component
    key="where-do-you-live",
    # Initially selected ID
    default="england",
)

st.markdown(f"Selected: {selected}")
