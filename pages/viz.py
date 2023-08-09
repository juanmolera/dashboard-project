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

st.markdown('# Viz')

opciones = st.selectbox('¿Which city do you want to visualize?', ['Choose an option'] + ['Madrid', 'Porto', 'Lisbon'])

if opciones == 'Madrid':

    st.markdown('#### Airbnb data example:')
    madrid_df = pd.read_csv('data/kepler/airbnb_madrid.csv')
    madrid_df.reset_index(drop = False, inplace = True)
    st.table(madrid_df.sample(1))

    fig1 = px.histogram(madrid_df, x = madrid_df['District']).update_xaxes(categoryorder = 'total descending')
    st.plotly_chart(fig1)

    pass

elif opciones == 'Porto':

    st.markdown('#### Airbnb data example:')
    df_porto = pd.read_csv('data/kepler/airbnb_porto.csv')
    st.table(df_porto.sample(1))

    pass
    
elif opciones == 'Lisbon':

    st.markdown('#### Airbnb data example:')
    df_lisbon = pd.read_csv('data/kepler/airbnb_lisbon.csv')
    st.table(df_lisbon.sample(1))

    pass
