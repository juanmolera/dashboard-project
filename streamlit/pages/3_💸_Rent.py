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
rent = pd.read_csv('../data/rent.csv')
mean_price = pd.read_csv('../data/mean_price_june_may_2023_airbnb.csv')

# Choose a district
#district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

# Kepler map config
with open(f'../data/config_madrid_rent.pickle', 'rb') as configuration:
    config = pickle.load(configuration)

# Kepler map geojson
with open(f'../data/neighbourhood_madrid.geojson', 'r') as f:
    geojson = f.read()

#map = KeplerGl(height=400, data={'airbnb_madrid': df[df['District'] == district]}, config=config)
#map.add_data(data=geojson, name='neighbourhood_madrid')

#st.markdown(f'#### Airbnbs in {district} district:')
#keplergl_static(map)

col1, col2 = st.columns(2)

with col1:

    st.markdown(f'#### Mean price in May 2023')
    fig1 = px.histogram(mean_price, x=mean_price['District'][mean_price['Month'] == 'May 2023'], y=mean_price['Mean price'][mean_price['Month'] == 'May 2023'], text_auto='.2s', color=mean_price['District'][mean_price['Month'] == 'May 2023'])
    fig1.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig1.update_xaxes(categoryorder = 'total descending')
    fig1.update_xaxes(tickangle = 270)
    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.markdown(f'#### Mean price in June 2023')
    fig2 = px.histogram(mean_price, x=mean_price['District'][mean_price['Month'] == 'June 2023'], y=mean_price['Mean price'][mean_price['Month'] == 'June 2023'], text_auto='.2s', color=mean_price['District'][mean_price['Month'] == 'June 2023'])
    fig2.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig2.update_xaxes(categoryorder = 'total descending')
    fig2.update_xaxes(tickangle = 270)
    st.plotly_chart(fig2, use_container_width=True)

options = st.multiselect('What districts price info wanna viz?', sorted(df['District'].unique().tolist()))

if options:

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(f'#### Rent price evolution [euros/m2]:')
        #fig3 = px.line(df_rent_price_evol, x=df_rent_price_evol['Date'], y=df_rent_price_evol[district], markers=True)
        #fig3 = px.line(rent, x=rent['Date'].unique().tolist(), y=rent['Value'][(rent['District']=='Chamartín') & (rent['District']=='Arganzuela')], markers=True)
        #fig3.update_xaxes(tickangle = 270)

        fig3 = px.line(rent, x=rent['Date'].unique().tolist(), y=rent['Value'][(rent['District']==options[0])], markers=True)

        fig3.update_xaxes(tickangle = 270)

        for o in options[1:]:

            fig3.add_scatter(x=rent['Date'].unique().tolist(), y=rent['Value'][(rent['District']==o)])

        st.plotly_chart(fig3, use_container_width=True)
    
    with col4:

        st.markdown(f'#### Second hand home price evolution [euros]:')
        fig4 = px.line(df_home_price_evol, x=df_home_price_evol['Date'], y=df_home_price_evol['Chamartín'], markers=True)
        fig4.add_scatter(x=df_home_price_evol['Date'], y=df_home_price_evol['Centro'])
        fig4.add_scatter(x=df_home_price_evol['Date'], y=df_home_price_evol['Chamartín'])
        fig4.update_xaxes(tickangle = 270)
        st.plotly_chart(fig4, use_container_width=True)