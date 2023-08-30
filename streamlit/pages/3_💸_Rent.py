# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Data visualization
import plotly.express as px
import plotly.graph_objects as go

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
mean_price_june_2023 = pd.read_csv('../data/mean_price_june_2023.csv')
mean_price_may_2023 = pd.read_csv('../data/mean_price_may_2023.csv')

pal = ['#08566d','#0a657f','#0b7392','#0d82a4','#0e90b6','#0f9ec8','#11addb','#12bbed','#24c1ee','#37c6f0','#49cbf1','#5bd0f2','#6dd5f4','#7fdbf5','#92e0f7','#a4e5f8','#b6eaf9','#c8effb','#dbf5fc','#edfafe','#ffffff']

# Choose a district
#district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

# Kepler map config
with open(f'../data/config_madrid_rent_new.pickle', 'rb') as configuration:
    config = pickle.load(configuration)

# Kepler map geojson
with open(f'../data/neighbourhood_madrid.geojson', 'r') as f:
    geojson = f.read()

#map = KeplerGl(height=400, data={'airbnb_madrid': df[df['District'] == district]}, config=config)
map = KeplerGl(height=400, data={'airbnb_madrid': df}, config=config)
map.add_data(data=geojson, name='neighbourhood_madrid')

#st.markdown(f'#### Airbnbs in {district} district:')
keplergl_static(map)

col1, col2 = st.columns(2)

with col1:

    st.markdown(f'#### Mean price in May 2023:')

    fig1 = px.histogram(mean_price, 
                        x=mean_price_may_2023['District'], 
                        y=mean_price_may_2023['Mean price'],
                        color=mean_price_may_2023['District'],
                        text_auto='.2s', 
                        hover_name=mean_price_may_2023['District'],
                        color_discrete_sequence=pal,
                        category_orders={"District": sorted(mean_price_may_2023['District'].unique().tolist())})
    
    fig1.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig1.update_xaxes(categoryorder = 'total descending')
    #fig1.update_xaxes(tickangle = 270)
    fig1.update_xaxes(title='', visible=False, showticklabels=False)
    fig1.update_yaxes(title='', visible=True, showticklabels=True)
    fig1.update_xaxes(title='District')
    fig1.update_yaxes(title='Euros')
    st.plotly_chart(fig1, use_container_width=True)

with col2:

    st.markdown(f'#### Mean price in June 2023:')

    fig2 = px.histogram(mean_price, 
                        x=mean_price_june_2023['District'], 
                        y=mean_price_june_2023['Mean price'], 
                        color=mean_price_june_2023['District'],
                        text_auto='.2s', 
                        hover_name=mean_price_june_2023['District'],
                        color_discrete_sequence=pal,
                        category_orders={"District": sorted(mean_price_june_2023['District'].unique().tolist())})
    
    fig2.update_traces(textfont_size=12, textangle=0, textposition='outside', cliponaxis=False)
    fig2.update_xaxes(categoryorder = 'total descending')
    #fig2.update_xaxes(tickangle = 270)
    fig2.update_xaxes(title='', visible=False, showticklabels=False)
    fig2.update_yaxes(title='', visible=True, showticklabels=True)
    fig2.update_xaxes(title='District')
    fig2.update_yaxes(title='Euros')
    st.plotly_chart(fig2, use_container_width=True)

options = st.multiselect('Which districts price info wanna viz?:', sorted(df['District'].unique().tolist()))

if options:

    col3, col4 = st.columns(2)

    with col3:

        st.markdown(f'#### Rent price evolution:')
        fig3 = go.Figure()
        for o in options:

            fig3.add_trace(go.Scatter(x=df_rent_price_evol['Date'].unique().tolist(), y=df_rent_price_evol[o], name = o))

        fig3.update_xaxes(tickangle = 270)
        fig3.update_xaxes(title='Date')
        fig3.update_yaxes(title='Euros/m\u00b2')
        fig3.update_layout(hovermode="x unified")
        st.plotly_chart(fig3, use_container_width=True)
    
    with col4:

        st.markdown(f'#### Second-hand home price evolution:')
        fig4 = go.Figure()
        for o in options:

            fig4.add_trace(go.Scatter(x=df_home_price_evol['Date'].unique().tolist(), y=['{:,}'.format(x).replace(',','.') for x in df_home_price_evol[o].tolist()], name = o))
        
        fig4.update_xaxes(tickangle = 270)
        fig4.update_xaxes(title='Date')
        fig4.update_yaxes(title='x1K Euros')
        fig4.update_layout(hovermode="x unified")
        st.plotly_chart(fig4, use_container_width=True)