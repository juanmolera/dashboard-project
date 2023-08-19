# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Random
import random

# My functions
from src import streamlit_functions as lit

# Streamlit page configuration
st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed', page_title = 'Comparative', page_icon = '👯‍♀️')

# Title
st.markdown('# Comparative viz')

# Availables cities to choose
cities = ['Madrid', 'Porto', 'Lisbon']

# Chooses a city
city = st.selectbox('Which city do you want to visualize?', ['Choose an option'] + cities)

# If a city has been chosen:
if city in cities:

    # Checks if you want to compare 2 cities
    comparative = st.selectbox(f'Do you want to compare {city} with another city?', ['Choose an option'] + ['Yes', 'No'])

    if comparative == 'Yes':

        #cities = cities.remove(city)
        
        second_city = st.selectbox(f'With which city do you want to compare {city}?', ['Choose an option'] + cities)

        if second_city in cities:

            random_city_df_to_show = random.choice([city, second_city])

            # Pandas
            st.markdown('#### Airbnb data example:')
            df = pd.read_csv(f'../data/kepler/airbnb_{random_city_df_to_show.lower()}.csv')
            st.table(df.sample(1))

            col1, col2 = st.columns(2)

            # First city:
            with col1:

                lit.city_streamlit(city)

            # Second city:
            with col2:

                lit.city_streamlit(second_city)

    if comparative == 'No':

        # Pandas
        st.markdown('#### Airbnb data example:')
        df = pd.read_csv(f'../data/kepler/airbnb_{city.lower()}.csv')
        st.table(df.sample(1))

        lit.city_streamlit(city)