# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# My functions
from src import viz_functions as viz

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

def city_streamlit(city):
    '''
    Creates the streamlit page for the chosen city
    '''

    # Pandas
    st.markdown('#### Airbnb data example:')
    df = pd.read_csv(f'../data/kepler/airbnb_{city.lower()}.csv')
    st.table(df.sample(1))

    # District section
    st.markdown(f'#### Airbnbs per district in {city}:')

    # Kepler map
    config = {}
    keplergl_static(viz.kepler_map_viz(df, config))

    # Districts histogram
    st.plotly_chart(viz.histogram_viz(df, 'District'), use_container_width=True)

    # Choose a district
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

        # Neighbourhood section
        st.markdown(f'#### Airbnbs in {district} neighbourhoods:')

        # Neighbourhoods histogram
        st.plotly_chart(viz.histogram_with_filter_viz(df, 'District', 'Neighbourhood', district), use_container_width=True)

        # Choose a neighbourhood
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