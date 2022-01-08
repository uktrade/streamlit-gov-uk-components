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
    id="where-do-you-live",   # Base of HTML IDs for radios
    key="where-do-you-live",  # Streamlit component instance key
    default="england",        # Initially selected ID
)

st.markdown(f"Selected: {selected}")
