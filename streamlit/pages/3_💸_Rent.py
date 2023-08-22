# Streamlit
import streamlit as st

# Data manipulation
import pandas as pd

# Data visualization
import plotly.express as px

st.set_page_config(layout = 'wide', initial_sidebar_state = 'collapsed', page_title = 'Extras', page_icon = '💸')

# Title
st.markdown('# Rent evolution viz')

# Dataframes creation
df = pd.read_csv(f'../data/airbnb_madrid.csv')
df_rent_price_evol = pd.read_csv('../data/rent_evolution_by_district_madrid.csv')

# Choose a district
district = st.selectbox('Which district data do you want to visualize?', ['Choose an option'] + sorted(df['District'].unique().tolist()))

if district in df['District'].unique().tolist():

    fig = px.line(df_rent_price_evol, x=df_rent_price_evol['Date'], y=df_rent_price_evol[district], markers=True)
    fig.update_xaxes(tickangle = 270)
    st.plotly_chart(fig, use_container_width=True)