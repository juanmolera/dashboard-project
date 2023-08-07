import streamlit as st
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl
import pandas as pd

st.markdown("# Testing kepler-streamlit")

st.write("This is a kepler.gl map in streamlit")

df = pd.read_csv('data/kepler/mad_kepler.csv')
map_1 = KeplerGl()
map_1.add_data(data=df, name='data_1')


