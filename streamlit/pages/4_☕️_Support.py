# Streamlit
import streamlit as st

from PIL import Image

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Support', page_icon='☕️')

# Title
st.markdown('# Support')

# Coffee
st.markdown('## Hey, give me your [money](https://www.buymeacoffee.com/juanmolera)')
image = Image.open('images/fry-shut-up-and-take-my-money.png')
st.image(image, use_column_width=True)