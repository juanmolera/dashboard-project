import streamlit as st
from PIL import Image

st.set_page_config(page_title="tourist dictatorship?", page_icon=":house:", layout="wide", initial_sidebar_state="expanded")

st.markdown("# Tourist dictatorship?")

image = Image.open('images/cover2.png')
st.image(image, use_column_width=True)





