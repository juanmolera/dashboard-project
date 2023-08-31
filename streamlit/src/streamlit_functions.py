# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# My functions
from src import viz_functions as viz

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

# Pepinillo
import pickle

def city_streamlit(city):
    '''
    Creates the streamlit page for the chosen city
    '''

    # Dataframes creation
    df = pd.read_csv(f'../data/airbnb_{city.lower()}.csv')

    # Total population, population density by district
    population = pd.read_csv('../data/population_and_density_by_district.csv')

    # District section
    st.markdown(f'#### Airbnbs heatmap per district in {city}:')

    # Kepler map config
    with open(f'../data/config_{city.lower()}_airbnb.pickle', 'rb') as configuration:
        config = pickle.load(configuration)

    # Kepler map geojson
    with open(f'../data/neighbourhood_{city}.geojson', 'r') as f:
        geojson = f.read()

    # Kepler map
    #keplergl_static(viz.kepler_map_viz(city.lower(), df, geojson, config))

    # District section
    st.markdown(f'#### Total airbnbs per district in {city}:')

    # Districts histogram
    st.plotly_chart(viz.histogram_viz(df, 'District'), use_container_width=True)

    # Choose a district
    district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

    if district in df['District'].unique().tolist():

        # District information in detail
        st.markdown(f'#### {district} district information:')

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown('Total population')
            st.metric(label='habitants', value=population['Population'][population['District'] == district].values[0])

        with col2:

            st.markdown('Population density')
            st.metric(label='habitants/km\u00b2', value=population['Density'][population['District'] == district].values[0])

        with col3:

            st.markdown('Total Airbnbs')
            st.metric(label='units', value='{:,}'.format(df[df['District'] == district].value_counts().sum()).replace(',','.'))

        # Neighbourhood section
        st.markdown(f'#### Total airbnbs per neighbourhood in {district} district:')

        # Neighbourhoods histogram
        st.plotly_chart(viz.histogram_with_filter_viz(df, 'District', 'Neighbourhood', district), use_container_width=True)

        '''
        # Choose a neighbourhood
        neighbourhood = st.selectbox('Which neighbourhood data do you want to visualize?', ['Choose an option'] + sorted(df['Neighbourhood'][df['District'] == district].unique().tolist()))

        if neighbourhood in df['Neighbourhood'].unique().tolist():

            # Neighbourhood information in detail
            st.markdown(f'#### {neighbourhood} neighbourhood information:')

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
        '''