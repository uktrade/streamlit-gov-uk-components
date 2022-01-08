import streamlit as st
from streamlit_gov_uk_components import gov_uk_radio_small_list

st.subheader("Smaller radio list")

selected = gov_uk_radio_small_list(
    # Tuple of (ID, label) pairs
    options=(
        ("monthly", "Monthly"),
        ("yearly", "Yearly"),
    ),
    id="filter",        # Base of HTML IDs for radios
    key="filter",       # Streamlit component instance key
    default="monthly",  # Initially selected ID
)

st.markdown(f"Selected: {selected}")
