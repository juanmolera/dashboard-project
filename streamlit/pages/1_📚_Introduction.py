import streamlit as st
from PIL import Image

st.set_page_config(layout='wide', initial_sidebar_state='collapsed', page_title='Introduction', page_icon='📚')

# CSS access
with open('css/style.css') as f:
    st.markdown(
        f'<style>{f.read()}</style>',
        unsafe_allow_html=True)


st.markdown('# Introduction')

st.write('This is my second project of the Ironhack data analysis bootcamp and it is focused on the comparative analysis between Spain and Portugal regarding the situation of Airbnb rental apartments and how this situation can affect the different districts of the city of Madrid. To achieve this, I obtained data from Airbnb for the cities of Madrid, Porto and Lisbon, data on the population of these cities and data on the evolution of the price of renting and buying second-hand housing in the city of Madrid. All this dataset has been cleaned from Pandas and loaded into a dashboard elaborated from Streamlit. In addition, interactive maps created from Kepler.gl have been added.')

st.markdown('## Motivation')

st.write('This project arises motivated by the recent legislation passed in Portugal, which implements restrictive measures on Airbnb rental apartments and about which it is already speculated whether or not it will be implemented in Spain as well. The main idea of the dashboard is to allow a comparative analysis based on the population data of the cities of Madrid, Porto and Lisbon, in order to detect where the Portuguese cities were at the time when the legislation regulating Airbnb rental apartments appeared and where Madrid is now. The dashboard also allows to analyze the districts of the city of Madrid, where the price of Airbnb is higher, and compare it with the rental and purchase price of second-hand housing to detect the areas of the city that are more profitable from an economic point of view and, therefore, more vulnerable to be exploited by Airbnb rental apartments.')


st.markdown('## Context')

st.markdown('### Airbnb')
st.write('Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.')

st.markdown('### The Portugal case')
st.write('The Portuguese government is making new restrictions on short-term rentals to protect the housing market and ensure that the number of tourist apartments doesn’t increase dramatically. This comes after Prime Minister Antonio Costa said he was worried that Portugal would become a “Disneyland” if more and more people began to rent out their apartments as holiday homes.')
st.write('Portugal has a licensing system for vacation rentals (such as Airbnb) called Alojamento Local. These licenses are granted by the municipal chambers and it is not possible to operate the platforms without them. From March 2023, if the law is passed, no more Airbnb licenses will be granted except in inland towns where they can help revive the economy. Those who already have one will have to pay higher taxes to finance permanent habitation and a review of all licenses will be carried out in 2030.')
st.write('The 16th of february 2023, Portugal Goverment aproved MAIS HABITAÇAO, with the following key points:')
st.markdown(' ##### 1. Increase the offer of properties for housing')
st.markdown('- Convert the use of commercial property or services for use housing')
st.markdown('- Provide properties of the state in regime of CDH')
st.markdown(' ##### 2. Simplify the processes of licensing')
st.markdown('- License with the term of responsability from the designers')
st.markdown('- Delay the interest for breach deadlines of licensing')
st.markdown(' ##### 3. Increase the number of houses in the rental market')
st.markdown('- Reinforce the confidence from landlords: state leases to sublease, guarantee state payment after 3 months default (or charges, or support or empty)')
st.markdown('- Increase the public offer: exemption from gains in real estate sales to the state')
st.markdown('- Promoting affordable rent: financing to municipalities to carry out coercive works, transfer incentive for housing in houses in local accommodation, lease mandatory of houses returns, tax exemption to affordable rental')
st.markdown(' ##### 4. Fight the speculation')
st.markdown('- End of gold visas')
st.markdown('- Guarantee of fair income in new contracts')
st.markdown('##### 5. Protect the families')
st.markdown('- Exemption of gains for amortization of home credit own and from descendants')
st.markdown('- In home credit: obligation of banks offer fixed rate, protection on climbs interest rate')
st.markdown('- In the value of income')

st.markdown('### Will Spain follow the same path?')
image = Image.open('images/graffiti.png')
st.image(image, use_column_width=True)