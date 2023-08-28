# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Data visualization
import plotly.express as px

# Kepler.gl maps
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

# Pepinillo
import pickle

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Extras', page_icon='💸')

# Title
st.markdown('# Rent evolution viz')

# Dataframes creation
df = pd.read_csv(f'../data/airbnb_madrid.csv')
df_rent_price_evol = pd.read_csv('../data/rent_price_evolution_by_district_madrid.csv')
df_home_price_evol = pd.read_csv('../data/second_hand_home_price_evolution_by_district_madrid.csv')
df_reviews_per_month = pd.read_csv('../data/reviews_per_month_airbnb_madrid.csv')
df_may_june = pd.read_csv('../data/reviews_may_june_2023_airbnb.csv')

# Choose a district
district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

if district in df['District'].unique().tolist():

    # Kepler map config
    with open(f'../data/config_madrid_rent.pickle', 'rb') as configuration:
        config = pickle.load(configuration)

    # Kepler map geojson
    with open(f'../data/neighbourhood_madrid.geojson', 'r') as f:
        geojson = f.read()

    map = KeplerGl(height=400, data={'airbnb_madrid': df[df['District'] == district]}, config=config)
    map.add_data(data=geojson, name='neighbourhood_madrid')

    st.markdown(f'#### Airbnbs in {district} district:')
    #keplergl_static(map)

    st.markdown(f'#### Airbnbs reviews in Madrid:')
    fig = px.histogram(df_reviews_per_month, x=df_reviews_per_month['Month'], y=df_reviews_per_month['Airbnb reviews'], text_auto='.2s', color=df_reviews_per_month['Month'])
    fig.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig.update_xaxes(tickangle = 270)
    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f'#### Airbnbs reviews in May 2023')
        fig1 = px.histogram(df_may_june, x=df_may_june['District'][df_may_june['Month'] == 'May 2023'], y=df_may_june['Airbnb reviews'][df_may_june['Month'] == 'May 2023'], text_auto='.2s', color=df_may_june['District'][df_may_june['Month'] == 'May 2023'])
        fig1.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
        fig1.update_xaxes(categoryorder = 'total descending')
        fig1.update_xaxes(tickangle = 270)
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown(f'#### Rent price evolution [euros/m2] in {district}:')
        #fig2 = px.line(df_rent_price_evol, x=df_rent_price_evol['Date'], y=df_rent_price_evol[district], markers=True)
        fig2 = px.line(df_rent_price_evol, x=df_rent_price_evol['Date'], y=df_rent_price_evol[district], markers=True)
        fig2.update_xaxes(tickangle = 270)
        st.plotly_chart(fig2, use_container_width=True)

    with col2:

        st.markdown(f'#### Airbnbs reviews in June 2023')
        fig3 = px.histogram(df_may_june, x=df_may_june['District'][df_may_june['Month'] == 'June 2023'], y=df_may_june['Airbnb reviews'][df_may_june['Month'] == 'June 2023'], text_auto='.2s', color=df_may_june['District'][df_may_june['Month'] == 'June 2023'])
        fig3.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
        fig3.update_xaxes(categoryorder = 'total descending')
        fig3.update_xaxes(tickangle = 270)
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown(f'#### Second hand home price evolution [euros] in {district}:')
        fig4 = px.line(df_home_price_evol, x=df_home_price_evol['Date'], y=df_home_price_evol[district], markers=True)
        fig4.add_scatter(x=df_home_price_evol['Date'], y=df_home_price_evol['Centro'])
        fig4.add_scatter(x=df_home_price_evol['Date'], y=df_home_price_evol['Chamartín'])
        fig4.update_xaxes(tickangle = 270)
        st.plotly_chart(fig4, use_container_width=True)


    

    