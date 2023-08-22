# Streamlit
import streamlit as st

# My functions
from src import streamlit_functions as lit

# Streamlit page configuration
st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed', page_title = 'Defs', page_icon = '📥')

# Title
st.markdown('# All in defs')

# Availables cities
cities = ['Madrid', 'Porto', 'Lisbon']

# Chooses a city
city = st.selectbox('Which city do you want to visualize?', ['Choose an option'] + cities)

# If a city has been chosen:
if city in cities:

    lit.city_streamlit(city)