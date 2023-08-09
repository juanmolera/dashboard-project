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

if options == 'Madrid':

    st.markdown('#### Airbnb data example:')
    df_madrid = pd.read_csv('../data/kepler/airbnb_madrid.csv')
    st.table(df_madrid.sample(1))

    st.markdown('#### Airbnbs per district in Madrid:')
    fig1 = px.histogram(df_madrid, x = df_madrid['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    options2 = st.selectbox('Which district population data do you want to visualize?', ['Choose an option'] + df_madrid['District'].unique().tolist())

    st.markdown('#### Airbnbs per neighbourhood in Madrid:')
    fig2 = px.histogram(df_madrid, x = df_madrid['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)

elif options == 'Porto':

    st.markdown('#### Airbnb data example:')
    df_porto = pd.read_csv('../data/kepler/airbnb_porto.csv')
    st.table(df_porto.sample(1))

    st.markdown('#### Airbnbs per district in Porto:')
    fig1 = px.histogram(df_porto, x = df_porto['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    st.markdown('#### Airbnbs per neighbourhood in Porto:')
    fig2 = px.histogram(df_porto, x = df_porto['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)
    
elif options == 'Lisbon':

    st.markdown('#### Airbnb data example:')
    df_lisbon = pd.read_csv('../data/kepler/airbnb_lisbon.csv')
    st.table(df_lisbon.sample(1))

    st.markdown('#### Airbnbs per district in Lisbon:')
    fig1 = px.histogram(df_lisbon, x = df_lisbon['District'])
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle=90)
    st.plotly_chart(fig1)

    st.markdown('#### Airbnbs per neighbourhood in Lisbon:')
    fig2 = px.histogram(df_lisbon, x = df_lisbon['Neighbourhood'])
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 90)
    st.plotly_chart(fig2)
