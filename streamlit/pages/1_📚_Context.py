import streamlit as st
from PIL import Image

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Context', page_icon='📚')

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True)

st.markdown('# Context')

st.markdown('## Airbnb')
st.write('Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.')

st.markdown('## The Portugal case')
st.write('The Portuguese government is making new restrictions on short-term rentals to protect the housing market and ensure that the number of tourist apartments doesn’t increase dramatically. This comes after Prime Minister Antonio Costa said he was worried that Portugal would become a “Disneyland” if more and more people began to rent out their apartments as holiday homes.')
st.write('The 16th of february 2023, Portugal Goverment aproved MAIS HABITAÇAO:')
st.markdown('1. INCREASE THE OFFER OF PROPERTIES FOR HOUSING')
st.markdown('- CONVERT THE USE OF COMMERCIAL PROPERTY OR SERVICES FOR USE HOUSING')
st.markdown('- PROVIDE PROPERTIES OF THE STATE IN REGIME OF CDH')
st.markdown('2. SIMPLIFY THE PROCESSES OF LICENSING')
st.markdown('- LICENSE WITH TERM OF RESPONSIBILITY FROM THE DESIGNERS')
st.markdown('- DELAY INTEREST FOR BREACH DEADLINES OF LICENSING')
st.markdown('3. AUMENTAR O NÚMERO DE CASAS NO MERCADO DE ARRENDAMENTO')
st.markdown('- REINFORCE THE CONFIDENCE FROM LANDLORDS: STATE LEASES TO SUBLEASE, GUARANTEE STATE PAYMENT AFTER 3 MONTHS DEFAULT (OR CHARGES, OR SUPPORT OR EMPTY)')
st.markdown('- INCREASE THE PUBLIC OFFER: EXEMPTION FROM GAINS IN REAL ESTATE SALES TO THE STATE')
st.markdown('- PROMOVER ARRENDAMENTO ACESSÍVEL: FINANCING TO MUNICIPALITIES TO CARRY OUT COERCIVE WORKS, TRANSFER INCENTIVE FOR HOUSING IN HOUSES IN LOCAL ACCOMMODATION, LEASE MANDATORY OF HOUSES RETURNS, TAX EXEMPTION TO AFFORDABLE RENTAL')
st.markdown('4. FIGHT THE SPECULATION')
st.markdown('- END OF GOLD VISAS')
st.markdown('- GUARANTEE OF FAIR INCOME IN NEW CONTRACTS')
st.markdown('5. PROTECT THE FAMILIES')
st.markdown('- EXEMPTION OF GAINS FOR AMORTIZATION OF HOME CREDIT OWN AND FROM DESCENDANTS')
st.markdown('- IN HOME CREDIT: OBLIGATION OF BANKS OFFER FIXED RATE, PROTECTION ON CLIMBS INTEREST RATE')
st.markdown('- IN THE VALUE OF INCOME')


st.markdown('## Will Spain follow the same path?')
image = Image.open('images/graffiti.png')
st.image(image, use_column_width=True)