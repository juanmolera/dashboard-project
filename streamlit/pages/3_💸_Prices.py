# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# My functions
from src import viz_functions as viz

# Data visualization
import plotly.express as px
import plotly.graph_objects as go

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

# Pepinillo
import pickle

# Streamlit page configuration
st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Prices', page_icon='💸')

# Title
st.markdown('# Airbnb, rental and second-hand home prices in Madrid')

# Dataframes creation
df_airbnb_madrid = pd.read_csv('../data/airbnb_madrid.csv')
df_mean_price = pd.read_csv('../data/mean_price_may_june_2023_airbnb.csv')
df_mean_price_may_2023 = pd.read_csv('../data/mean_price_may_2023.csv')
df_mean_price_june_2023 = pd.read_csv('../data/mean_price_june_2023.csv')
df_rent_price_evol = pd.read_csv('../data/rent_price_evolution_by_district_madrid.csv')
df_home_price_evol = pd.read_csv('../data/second_hand_home_price_evolution_by_district_madrid.csv')
blues = pd.read_csv('../data/blues.csv')

# Kepler map config
with open('../data/config_madrid_rent2.pickle', 'rb') as configuration:
    config = pickle.load(configuration)

# Kepler map geojson
with open('../data/neighbourhood_madrid.geojson', 'r') as f:
    geojson = f.read()

#map = KeplerGl(height=400, data={'airbnb_madrid': df[df['District'] == district]}, config=config)
map = KeplerGl(height=400, data={'airbnb_madrid': df_airbnb_madrid}, config=config)
map.add_data(data=geojson, name='neighbourhood_madrid')

st.markdown('#### Airbnb mean price per density in Madrid:')
keplergl_static(map)

col1, col2 = st.columns(2)

with col1:

    st.markdown('#### Airbnb mean price per district in May 2023:')
    fig1 = px.histogram(df_mean_price, 
                        x=df_mean_price_may_2023['District'], 
                        y=df_mean_price_may_2023['Mean price'],
                        color=df_mean_price_may_2023['District'],
                        text_auto='.2s', 
                        hover_name=df_mean_price_may_2023['District'],
                        color_discrete_sequence=blues['Code'].tolist(),
                        category_orders={"District": sorted(df_mean_price_may_2023['District'].unique().tolist())})
    
    fig1.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(title='', visible=False, showticklabels=False)
    fig1.update_yaxes(title='', visible=True, showticklabels=True)
    fig1.update_xaxes(title='District')
    fig1.update_yaxes(title='Euros')
    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.markdown('#### Airbnb mean price per district in June 2023:')
    fig2 = px.histogram(df_mean_price, 
                        x=df_mean_price_june_2023['District'], 
                        y=df_mean_price_june_2023['Mean price'], 
                        color=df_mean_price_june_2023['District'],
                        text_auto='.2s', 
                        hover_name=df_mean_price_june_2023['District'],
                        color_discrete_sequence=blues['Code'].tolist(),
                        category_orders={"District": sorted(df_mean_price_june_2023['District'].unique().tolist())})
    
    fig2.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(title='', visible=False, showticklabels=False)
    fig2.update_yaxes(title='', visible=True, showticklabels=True)
    fig2.update_xaxes(title='District')
    fig2.update_yaxes(title='Euros')
    st.plotly_chart(fig2, use_container_width=True)

options = st.multiselect('From which districts would you like to visualize the information on the evolution of rental and purchase prices of second-hand homes?', sorted(df_airbnb_madrid['District'].unique().tolist()))

if options:

    col3, col4 = st.columns(2)

    with col3:

        st.markdown('#### Rent price evolution:')
        fig3 = go.Figure()
        for o in options:

            fig3.add_trace(go.Scatter(x=df_rent_price_evol['Date'].unique().tolist(), y=df_rent_price_evol[o], name = o))

        fig3.update_xaxes(tickangle = 270)
        fig3.update_xaxes(title='Date')
        fig3.update_yaxes(title='Euros/m\u00b2')
        fig3.update_layout(hovermode="x unified")
        st.plotly_chart(fig3, use_container_width=True)
    
    with col4:

        st.markdown('#### Second-hand home price evolution:')
        fig4 = go.Figure()
        for o in options:

            fig4.add_trace(go.Scatter(x=df_home_price_evol['Date'].unique().tolist(), y=['{:,}'.format(x).replace(',','.') for x in df_home_price_evol[o].tolist()], name = o))
        
        fig4.update_xaxes(tickangle = 270)
        fig4.update_xaxes(title='Date')
        fig4.update_yaxes(title='Thousands of Euros')
        fig4.update_layout(hovermode="x unified")
        st.plotly_chart(fig4, use_container_width=True)