# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.set_page_config(layout="wide", initial_sidebar_state="collapsed", page_title='Viz', page_icon="👀")

st.markdown('# Viz')

options = st.selectbox('Which city do you want to visualize?', ['Choose an option'] + ['Madrid', 'Porto', 'Lisbon'])

# Madrid
if options == 'Madrid':

    # Pandas
    st.markdown('#### Airbnb data example:')
    df_madrid = pd.read_csv('../data/kepler/airbnb_madrid.csv')
    st.table(df_madrid.sample(1))

    # District
    st.markdown('#### Airbnbs per district in Madrid:')
    fig1 = px.histogram(df_madrid, x = df_madrid['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle = 90)
    st.plotly_chart(fig1, use_container_width=True)

    options2 = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + df_madrid['District'].unique().tolist())
    
    if options2 in df_madrid['District'].unique().tolist():

        st.markdown(f'#### {options2} district:')

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown('Total population')
            st.metric(label='', value = 0)

        with col2:

            st.markdown('Population density')
            st.metric(label='', value = 0)

        with col3:

            st.markdown('Total Airbnbs')
            st.metric(label='', value = df_madrid[df_madrid['District'] == options2].value_counts().sum())

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Madrid:')
    fig2 = px.histogram(df_madrid, x = df_madrid['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2, use_container_width=True)

    options3 = st.selectbox('Which neighbourhood data do you want to visualize?', ['Choose an option'] + df_madrid['Neighbourhood'].unique().tolist())
    
    if options3 in df_madrid['Neighbourhood'].unique().tolist():

        col1, col2, col3 = st.columns(3)

        with col1:

            st.markdown('Total population')
            st.metric(label='', value = 0)

        with col2:

            st.markdown('Population density')
            st.metric(label='', value = 0)

        with col3:

            st.markdown('Total Airbnbs')
            st.metric(label='', value = df_madrid[df_madrid['Neighbourhood'] == options3].value_counts().sum())

# Porto
elif options == 'Porto':

    # Pandas
    st.markdown('#### Airbnb data example:')
    df_porto = pd.read_csv('../data/kepler/airbnb_porto.csv')
    st.table(df_porto.sample(1))

    # District
    st.markdown('#### Airbnbs per district in Porto:')
    fig1 = px.histogram(df_porto, x = df_porto['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle = 90)
    st.plotly_chart(fig1, use_container_width=True)

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Porto:')
    fig2 = px.histogram(df_porto, x = df_porto['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2, use_container_width=True)

# Lisbon
elif options == 'Lisbon':

    # Pandas
    st.markdown('#### Airbnb data example:')
    df_lisbon = pd.read_csv('../data/kepler/airbnb_lisbon.csv')
    st.table(df_lisbon.sample(1))

    # District
    st.markdown('#### Airbnbs per district in Lisbon:')
    fig1 = px.histogram(df_lisbon, x = df_lisbon['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle = 90)
    st.plotly_chart(fig1, use_container_width=True)

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Lisbon:')
    fig2 = px.histogram(df_lisbon, x = df_lisbon['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2, use_container_width=True)
