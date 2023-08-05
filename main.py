import streamlit as st
from PIL import Image


st.set_page_config(page_title="dictadura turistica", page_icon=":house:", layout="wide", initial_sidebar_state="expanded")

st.markdown("# Project 2: Airbnb dashboard")
st.sidebar.markdown("# Main page")

#st.title('Project 2: Airbnb dashboard')
#st.write('Spain vs. Portugal Airbnb situation')

st.markdown("### Spain vs. Portugal Airbnb situation")

with st.sidebar:
    
    st.image('images/atab.jpeg', width=30)
    opcions = ['Home', 'General overview', 'Explore', 'Recomendations', 'About us']
    selected = option_menu("Menu", opcions, 
        icons=['house', 'folder', 'graph-up', 'eye', 'flower2'], menu_icon="cast", default_index=0,
        styles={"nav-link-selected" : {"background-color": "#BD7250"}})


