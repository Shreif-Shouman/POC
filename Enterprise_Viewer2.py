import streamlit as st
import streamlit.components.v1 as components

# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
  <img src="https://www.iaea.org/sites/default/files/images/iaea-landing-page-banner.jpg" alt="Banner Image">
</div>
<style>
.banner {
  width: 100%;
  height: 200px;
  overflow: hidden;
}
.banner img {
  width: 100%;
  object-fit: cover;
}
</style>
"""

# Display the banner
st.markdown(custom_html, unsafe_allow_html=True)

# Add the title and text under the title
st.title("Enterprise Search: Learning and Training")
st.write("Created by: BSS Innovation Team")

# Create a layout with two columns
col1, col2 = st.columns(2)

# Use one column for each POC
with col1:
    html_code1 = st.text_area("Google", height=300)
    run_poc1 = st.checkbox("Run POC1")

    if run_poc1:
        st.write("Running POC1...")
        components.html(html_code1, height=500, scrolling=True)

with col2:
    html_code2 = st.text_area("Microsoft", height=300)
    run_poc2 = st.checkbox("Run POC2")

    if run_poc2:
        st.write("Running POC2...")
        components.html(html_code2, height=500, scrolling=True)
