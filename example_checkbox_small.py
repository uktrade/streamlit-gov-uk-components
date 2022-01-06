import streamlit as st
from streamlit_gov_uk_components import gov_uk_checkbox_small

st.subheader("Smaller checkbox")

selected = gov_uk_checkbox_small("HM Revenue and Customs (HMRC)", "hmrc", default=True)
st.markdown("Selected: %s" % selected)

selected = gov_uk_checkbox_small("Employment Tribunal", "employment-tribunal", default=False)
st.markdown("Selected: %s" % selected)
