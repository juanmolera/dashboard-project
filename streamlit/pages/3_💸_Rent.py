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

# Choose a district
district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

if district in df['District'].unique().tolist():

    # Kepler map config
    with open(f'../data/config_madrid_rent.pickle', 'rb') as configuration:
        config = pickle.load(configuration)

    # Kepler map geojson
    with open(f'../data/neighbourhood_madrid.geojson', 'r') as f:
        geojson = f.read()

    map = KeplerGl(height=400, data={'airbnb_madrid': df[df['District'] == district]}, config=config);
    map.add_data(data=geojson, name='neighbourhood_madrid');

    st.markdown(f'#### Airbnbs in {district} district:')
    keplergl_static(map)

    col1, col2 = st.columns(2)

    # First city:
    with col1:

        st.markdown(f'#### Rent price evolution [euros/m2] in {district}:')
        fig = px.line(df_rent_price_evol, x=df_rent_price_evol['Date'], y=df_rent_price_evol[district], markers=True)
        fig.update_xaxes(tickangle = 270)
        st.plotly_chart(fig, use_container_width=True)

    # Second city:
    with col2:

        st.markdown(f'#### Second hand home price evolution [euros] in {district}:')
        fig = px.line(df_home_price_evol, x=df_home_price_evol['Date'], y=df_home_price_evol[district], markers=True)
        fig.update_xaxes(tickangle = 270)
        st.plotly_chart(fig, use_container_width=True)


    

    