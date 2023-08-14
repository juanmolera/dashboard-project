# Streamlit
import streamlit as st

# My functions
from src import streamlit_functions as fu

# Data manipulation
import pandas as pd

# Data visualization
import plotly.express as px

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed', page_title = 'Viz', page_icon = '👀')

st.markdown('# Viz')

# Availables cities to choose
cities = ['Madrid', 'Porto', 'Lisbon']

# Chooses a city
city = st.selectbox('Which city do you want to visualize?', ['Choose an option'] + cities)

if city in cities:

    # Pandas
    st.markdown('#### Airbnb data example:')
    df = pd.read_csv(f'../data/kepler/airbnb_{city.lower()}.csv')
    st.table(df.sample(1))

    # District section
    st.markdown(f'#### Airbnbs per district in {city}:')

    # Kepler map
    config = {}
    keplergl_static(fu.kepler_map_viz(df, config))

    # Histogram
    st.plotly_chart(fu.histogram_viz(df, 'District'), use_container_width=True)

    # Chooses a district
    district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))
    
    if district in df['District'].unique().tolist():

        # District information in detail
        st.markdown(f'#### {district} information in detail:')

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown('Total population')
            st.metric(label='', value = 0)

        with col2:

            st.markdown('Population density')
            st.metric(label='', value = 0)

        with col3:

            st.markdown('Total Airbnbs')
            st.metric(label='', value = df[df['District'] == district].value_counts().sum())

        # Neighbourhood
        st.markdown(f'#### Airbnbs in {district} neighbourhoods:')
        
        # Histogram
        st.plotly_chart(fu.histogram_with_filter_viz(df, 'District', 'Neighbourhood', district), use_container_width=True)

        # Chooses a neighbourhood
        neighbourhood = st.selectbox('Which neighbourhood data do you want to visualize?', ['Choose an option'] + sorted(df['Neighbourhood'][df['District'] == district].unique().tolist()))
        
        if neighbourhood in df['Neighbourhood'].unique().tolist():

            # Neighbourhood information in detail
            st.markdown(f'#### {neighbourhood} neighbourhood:')

            col1, col2, col3 = st.columns(3)

            with col1:

                st.markdown('Total population')
                st.metric(label='', value = 0)

            with col2:

                st.markdown('Population density')
                st.metric(label='', value = 0)

            with col3:

                st.markdown('Total Airbnbs')
                st.metric(label='', value = df[df['Neighbourhood'] == neighbourhood].value_counts().sum())