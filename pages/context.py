import streamlit as st
from PIL import Image

st.markdown("# Context")

st.markdown("## The Portugal Case")
image = Image.open('images/graffiti.png')
st.image(image, use_column_width=True)

st.markdown("## Will Spain follow the same path?")