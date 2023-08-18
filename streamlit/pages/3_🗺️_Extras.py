# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Data visualization
import plotly.express as px

st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed', page_title = 'Extras', page_icon = '🗺️')


df = pd.read_csv('../data/kepler/airbnb_madrid.csv')