# dashboard-project

![tourist dictatorship?](/streamlit/images/cover2.png)

# Introduction

This is my second project of the Ironhack data analysis bootcamp and it is focused on the comparative analysis between Spain and Portugal regarding the situation of Airbnb rental apartments and how this situation can affect the different districts of the city of Madrid. To achieve this, I obtained data from Airbnb for the cities of Madrid, Porto and Lisbon, data on the population of these cities and data on the evolution of the price of renting and buying second-hand housing in the city of Madrid. All this dataset has been cleaned from Pandas and loaded into a dashboard elaborated from Streamlit. In addition, interactive maps created from Kepler.gl have been added.

## Motivation

This project arises motivated by the recent legislation passed in Portugal, which implements restrictive measures on Airbnb rental apartments and about which it is already speculated whether or not it will be implemented in Spain as well. The main idea of the dashboard is to allow a comparative analysis based on the population data of the cities of Madrid, Porto and Lisbon, in order to detect where the Portuguese cities were at the time when the legislation regulating Airbnb rental apartments appeared and where Madrid is now. The dashboard also allows to analyze the districts of the city of Madrid, where the price of Airbnb is higher, and compare it with the rental and purchase price of second-hand housing to detect the areas of the city that are more profitable from an economic point of view and, therefore, more vulnerable to be exploited by Airbnb rental apartments.

## Context

### Airbnb

Airbnb, Inc. is an American San Francisco-based company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. The company is credited with revolutionizing the tourism industry, while also having been the subject of intense criticism by residents of tourism hotspot cities like Barcelona and Venice for enabling an unaffordable increase in home rents, and for a lack of regulation.

### The Portugal case

The Portuguese government is making new restrictions on short-term rentals to protect the housing market and ensure that the number of tourist apartments doesn’t increase dramatically. This comes after Prime Minister Antonio Costa said he was worried that Portugal would become a “Disneyland” if more and more people began to rent out their apartments as holiday homes.

The 16th of february 2023, Portugal Goverment aproved MAIS HABITAÇAO, with the following key points:




### Information sources:
- [Inside Airbnb](http://insideairbnb.com/get-the-data/) (Madrid, Porto, Lisbon)
- [Ayuntamiento de Madrid](https://www.madrid.es/portales/munimadrid/es/Inicio/El-Ayuntamiento/Estadistica/Distritos-en-cifras/?vgnextfmt=default&vgnextchannel=27002d05cb71b310VgnVCM1000000b205a0aRCRD) (Madrid)
- [INE portugal](https://censos.ine.pt/xportal/xmain?xpgid=censos21_main&xpid=CENSOS21&xlang=pt) (Porto & Lisbon)

### Tools
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://docs.streamlit.io/)
- [Kepler](https://kepler.gl/)