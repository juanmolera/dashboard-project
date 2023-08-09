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

st.set_page_config(page_title = 'Viz', page_icon = '👀')

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
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    options2 = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + df_madrid['District'].unique().tolist())
    
    if options2 in df_madrid['District'].unique().tolist():

        col1, col2 = st.columns(2)

        with col1:

            st.markdown('Total population')
            st.line_chart([0, 1, 2, 3, 4])

            st.markdown('Population density')
            st.line_chart([0, 1, 2, 3, 4])

        with col2:

            st.markdown('Square meters')
            st.line_chart([4, 3, 2, 1, 0])

            st.markdown('Total Airbnbs')
            st.line_chart([4, 3, 2, 1, 0])

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Madrid:')
    fig2 = px.histogram(df_madrid, x = df_madrid['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)

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
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Porto:')
    fig2 = px.histogram(df_porto, x = df_porto['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)

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
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    # Neighbourhood
    st.markdown('#### Airbnbs per neighbourhood in Lisbon:')
    fig2 = px.histogram(df_lisbon, x = df_lisbon['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)
