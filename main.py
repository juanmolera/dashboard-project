import streamlit as st
from PIL import Image

st.set_page_config(page_title="tourist dictatorship?", page_icon=":house:", layout="wide", initial_sidebar_state="expanded")

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

st.markdown("# Tourist dictatorship?")

image = Image.open('images/cover2.png')
st.image(image, use_column_width=True)

st.markdown("## Introduction")
st.write('This is my second project of the Ironhack data analytics bootcamp and it is focused on the analysis of the impact of Airbnb over different population parameters in Madrid.')


st.markdown("## Motivation & Objectives")
st.write('- Initial situation, Portugal case heatmap vs. Spain with population data and rental flats numbers')
st.write('- Commuting de barrio según Airbnbs')
st.write('- % Inmigrandes en zonas más pobladas de Airbnb')
st.write('- Incremento en el precio del alquiler (ójala)')