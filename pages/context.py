import streamlit as st
from PIL import Image

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

st.markdown("# Context")

st.markdown("## Airbnb")
st.write('Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.')

st.markdown("## The Portugal case")
image = Image.open('images/graffiti.png')
st.image(image, use_column_width=True)

st.markdown("## Will Spain follow the same path?")