import streamlit as st
import streamlit.components.v1 as components
from typing import List, Any
import pandas as pd
import ssl
from googlesearch import search
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import random
from scipy.stats import poisson
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la
from itertools import product
from scipy import stats
import altair as alt
import time
import urllib
import wikipedia
import unicodedata

st.title('Predictor de Partidos de Fútbol - Clubes y Selecciones Nacionales')
ssl._create_default_https_context = ssl._create_unverified_context


spi_global_rankings = pd.read_csv("https://projects.fivethirtyeight.com/soccer-api/club/spi_global_rankings.csv")
spi_global_rankings.columns = ['rank', 'prev_rank', 'name', 'league', 'off', 'defe', 'spi']
print(spi_global_rankings)


spi_global_rankings_intl = pd.read_csv(
    "https://projects.fivethirtyeight.com/soccer-api/international/spi_global_rankings_intl.csv")
spi_global_rankings_intl.columns = ['rank', 'name', 'confed', 'off', 'defe', 'spi']
print(spi_global_rankings_intl)

# Extract necessary columns

spi_clubs = spi_global_rankings[['rank','name', 'off', 'defe', 'spi']]
spi_national_teams = spi_global_rankings_intl[['rank', 'name', 'off', 'defe', 'spi']]

# Concatenate data frames to create spi data frame.

spi_frames = [spi_clubs, spi_national_teams]

spi = pd.concat(spi_frames)
spi.sort_values(by=['spi'], ascending=False, inplace=True)
spi=spi.reset_index(drop=True)

latest_iteration0= st.empty()
bar0 = st.progress(0)

for i in range(100):
    latest_iteration0.markdown(f'Actualizando la base de datos con la información más reciente. Porcentaje completado {i+1}')
    bar0.progress(i+1)
    time.sleep(0.1)

st.markdown("Podés simular partidos navegando bajo la tabla")

@st.cache
def load_data():
    return spi

df_pf=load_data()

Equipo_casa = df_pf['name']

Equipo_visita = df_pf['name']

# CSS to inject contained in a string
hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)

# Display an interactive table
st.dataframe(spi)

st.subheader('Simular partido\nSeleccioná equipos')
st.markdown("Es posible elegir/retirar los\nequipos aunque ya hayan iniciado\nprocesos anteriores o subsecuentes,\ny aunque la pantalla esté gris")

params={
    'equipo_casa' : st.selectbox('Equipo de casa', Equipo_casa),
    'equipo_visita' : st.selectbox('Equipo de visita', Equipo_visita)
}


if st.button("Aceptar equipos"):
    equipo_casa_input = params['equipo_casa']
    equipo_visita_input = params['equipo_visita']
else:
    equipo_casa_input = "Ninguno"
    equipo_visita_input = "Ninguno"

if st.button("Retirar selección"):
    equipo_casa_input = "Ninguno"
    equipo_visita_input = "Ninguno"
else:
    equipo_casa_input = params['equipo_casa']
    equipo_visita_input = params['equipo_visita']

st.markdown("Has registrado el siguiente equipo en casa: " + equipo_casa_input)
st.markdown("Has registrado el siguiente equipo de visita: " + equipo_visita_input)

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.markdown(f'Reuniendo índices ofensivos y defensivos por equipo seleccionado. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

latest_iteration2 = st.empty()
bar2 = st.progress(0)

for i in range(100):
    latest_iteration2.markdown(f'Recogiendo logos de los equipos. Porcentaje completado {i+1}')
    bar2.progress(i+1)
    time.sleep(0.1)
    
def equipo_casa_input_():

    if equipo_casa_input == 'Afghanistan': return 'File:Flag_of_Afghanistan.svg'
    elif equipo_casa_input == 'Albania': return 'File:Flag_of_Albania.svg'
    elif equipo_casa_input == 'Algeria': return 'File:Flag_of_Algeria.svg'
    elif equipo_casa_input == 'Samoa': return 'File:Flag_of_American_Samoa.svg'
    elif equipo_casa_input == 'Andorra': return 'File:Flag_of_Andorra.svg'
    elif equipo_casa_input == 'Angola': return 'File:Flag_of_Angola.svg'
    elif equipo_casa_input == 'Anguilla': return 'File:Flag_of_Anguilla.svg'
    elif equipo_casa_input == 'Antigua and Barbuda': return 'File:Flag_of_Antigua_and_Barbuda.svg'
    elif equipo_casa_input == 'Argentina': return 'File:Flag_of_Argentina.svg'
    elif equipo_casa_input == 'Armenia': return 'File:Flag_of_Armenia.svg'
    elif equipo_casa_input == 'Aruba': return 'File:Flag_of_Aruba.svg'
    elif equipo_casa_input == 'Australia': return 'File:Flag_of_Australia.svg'
    elif equipo_casa_input == 'Austria': return 'File:Flag_of_Austria.svg'
    elif equipo_casa_input == 'Azerbaijan': return 'File:Flag_of_Azerbaijan.svg'
    elif equipo_casa_input == 'Bahamas': return 'File:Flag_of_Bahamas.svg'
    elif equipo_casa_input == 'Bahrain': return 'File:Flag_of_Bahrain.svg'
    elif equipo_casa_input == 'Bangladesh': return 'File:Flag_of_Bangladesh.svg'
    elif equipo_casa_input == 'Barbados': return 'File:Flag_of_Barbados.svg'
    elif equipo_casa_input == 'Basque Country': return 'File:Flag_of_the_Basque_Country.svg'
    elif equipo_casa_input == 'Belarus': return 'File:Flag_of_Belarus.svg'
    elif equipo_casa_input == 'Belgium': return 'File:Flag_of_Belgium.svg'
    elif equipo_casa_input == 'Belize': return 'File:Flag_of_Belize.svg'
    elif equipo_casa_input == 'Benin': return 'File:Flag_of_Benin.svg'
    elif equipo_casa_input == 'Bermuda': return 'File:Flag_of_Bermuda.svg'
    elif equipo_casa_input == 'Bhutan': return 'File:Flag_of_Bhutan.svg'
    elif equipo_casa_input == 'Bolivia': return 'File:Flag_of_Bolivia.svg'
    elif equipo_casa_input == 'Bonaire': return 'File:Flag_of_Bonaire.svg'
    elif equipo_casa_input == 'Bosnia and Herzegovina': return 'File:Flag_of_Bosnia_and_Herzegovina.svg'
    elif equipo_casa_input == 'Botswana': return 'File:Flag_of_Botswana.svg'
    elif equipo_casa_input == 'Brazil': return 'File:Flag_of_Brazil.svg'
    elif equipo_casa_input == 'British Virgin Islands': return 'File:Flag_of_British_Virgin_Islands.svg'
    elif equipo_casa_input == 'Brunei': return 'File:Flag_of_Brunei.svg'
    elif equipo_casa_input == 'Bulgaria': return 'File:Flag_of_Bulgaria.svg'
    elif equipo_casa_input == 'Burkina Faso': return 'File:Flag_of_Burkina_Faso.svg'
    elif equipo_casa_input == 'Burundi': return 'File:Flag_of_Burundi.svg'
    elif equipo_casa_input == 'Cambodia': return 'File:Flag_of_Cambodia.svg'
    elif equipo_casa_input == 'Cameroon': return 'File:Flag_of_Cameroon.svg'
    elif equipo_casa_input == 'Canada': return 'File:Flag_of_Canada.svg'
    elif equipo_casa_input == 'Cape Verde Islands': return 'File:Flag_of_Cape_Verde.svg'
    elif equipo_casa_input == 'Cayman Islands': return 'File:Flag_of_Cayman_Islands.svg'
    elif equipo_casa_input == 'Central African Republic': return 'File:Flag_of_Central_African_Republic.svg'
    elif equipo_casa_input == 'Chad': return 'File:Flag_of_Chad.svg'
    elif equipo_casa_input == 'Chile': return 'File:Flag_of_Chile.svg'
    elif equipo_casa_input == 'China PR': return "File:Flag_of_the_People's_Republic_of_China.svg"
    elif equipo_casa_input == 'Chinese Taipei': return 'File:Flag_of_the_Republic_of_China.svg'
    elif equipo_casa_input == 'Colombia': return 'File:Flag_of_Colombia.svg'
    elif equipo_casa_input == 'Comoros': return 'File:Flag_of_Comoros.svg'
    elif equipo_casa_input == 'Congo': return 'File:Flag_of_Congo.svg'
    elif equipo_casa_input == 'Congo DR': return 'File:Flag_of_the_Democratic_Republic_of_the_Congo.svg'
    elif equipo_casa_input == 'Cook Islands': return 'File:Flag_of_Cook_Islands.svg'
    elif equipo_casa_input == 'Costa Rica': return 'File:Flag_of_Costa_Rica.svg'
    elif equipo_casa_input == 'Croatia': return 'File:Flag_of_Croatia.svg'
    elif equipo_casa_input == 'Cuba': return 'File:Flag_of_Cuba.svg'
    elif equipo_casa_input == 'Curacao': return 'File:Flag_of_Curaçao.svg'
    elif equipo_casa_input == 'Cyprus': return 'File:Flag_of_Cyprus.svg'
    elif equipo_casa_input == 'Czech Republic': return 'File:Flag_of_Czech_Republic.svg'
    elif equipo_casa_input == 'Denmark': return 'File:Flag_of_Denmark.svg'
    elif equipo_casa_input == 'Djibouti': return 'File:Flag_of_Djibouti.svg'
    elif equipo_casa_input == 'Dominica': return 'File:Flag_of_Dominica.svg'
    elif equipo_casa_input == 'Dominican Republic': return 'File:Flag_of_Dominican_Republic.svg'
    elif equipo_casa_input == 'Ecuador': return 'File:Flag_of_Ecuador.svg'
    elif equipo_casa_input == 'Egypt': return 'File:Flag_of_Egypt.svg'
    elif equipo_casa_input == 'El Salvador': return 'File:Flag_of_El_Salvador.svg'
    elif equipo_casa_input == 'England': return 'File:Flag_of_England.svg'
    elif equipo_casa_input == 'Equatorial Guinea': return 'File:Flag_of_Equatorial_Guinea.svg'
    elif equipo_casa_input == 'Eritrea': return 'File:Flag_of_Eritrea.svg'
    elif equipo_casa_input == 'Estonia': return 'File:Flag_of_Estonia.svg'
    elif equipo_casa_input == 'Ethiopia': return 'File:Flag_of_Ethiopia.svg'
    elif equipo_casa_input == 'Faroe Islands': return 'File:Flag_of_Faroe_Islands.svg'
    elif equipo_casa_input == 'Fiji': return 'File:Flag_of_Fiji.svg'
    elif equipo_casa_input == 'Finland': return 'File:Flag_of_Finland.svg'
    elif equipo_casa_input == 'France': return 'File:Flag_of_France.svg'
    elif equipo_casa_input == 'French Guiana': return 'File:Flag_of_French_Guiana.svg'
    elif equipo_casa_input == 'Gabon': return 'File:Flag_of_Gabon.svg'
    elif equipo_casa_input == 'Gambia': return 'File:Flag_of_Gambia.svg'
    elif equipo_casa_input == 'Georgia': return 'File:Flag_of_Georgia.svg'
    elif equipo_casa_input == 'Germany': return 'File:Flag_of_Germany.svg'
    elif equipo_casa_input == 'Ghana': return 'File:Flag_of_Ghana.svg'
    elif equipo_casa_input == 'Gibraltar': return 'File:Flag_of_Gibraltar.svg'
    elif equipo_casa_input == 'Greece': return 'File:Flag_of_Greece.svg'
    elif equipo_casa_input == 'Grenada': return 'File:Flag_of_Grenada.svg'
    elif equipo_casa_input == 'Guadeloupe': return 'File:Flag_of_Guadeloupe_(local)_variant.svg'
    elif equipo_casa_input == 'Guam': return 'File:Flag_of_Guam.svg'
    elif equipo_casa_input == 'Guatemala': return 'File:Flag_of_Guatemala.svg'
    elif equipo_casa_input == 'Guinea': return 'File:Flag_of_Guinea.svg'
    elif equipo_casa_input == 'Guinea-Bissau': return 'File:Flag_of_Guinea-Bissau.svg'
    elif equipo_casa_input == 'Guyana': return 'File:Flag_of_Guyana.svg'
    elif equipo_casa_input == 'Haiti': return 'File:Flag_of_Haiti.svg'
    elif equipo_casa_input == 'Honduras': return 'File:Flag_of_Honduras.svg'
    elif equipo_casa_input == 'Hong Kong': return 'File:Flag_of_Hong_Kong.svg'
    elif equipo_casa_input == 'Hungary': return 'File:Flag_of_Hungary.svg'
    elif equipo_casa_input == 'Iceland': return 'File:Flag_of_Iceland.svg'
    elif equipo_casa_input == 'India': return 'File:Flag_of_India.svg'
    elif equipo_casa_input == 'Indonesia': return 'File:Flag_of_Indonesia.svg'
    elif equipo_casa_input == 'Iran': return 'File:Flag_of_Iran.svg'
    elif equipo_casa_input == 'Iraq': return 'File:Flag_of_Iraq.svg'
    elif equipo_casa_input == 'Israel': return 'File:Flag_of_Israel.svg'
    elif equipo_casa_input == 'Italy': return 'File:Flag_of_Italy.svg'
    elif equipo_casa_input == 'Ivory Coast': return 'File:Flag_of_Ivory_Coast.svg'
    elif equipo_casa_input == 'Jamaica': return 'File:Flag_of_Jamaica.svg'
    elif equipo_casa_input == 'Japan': return 'File:Flag_of_Japan.svg'
    elif equipo_casa_input == 'Jordan': return 'File:Flag_of_Jordan.svg'
    elif equipo_casa_input == 'Kazakhstan': return 'File:Flag_of_Kazakhstan.svg'
    elif equipo_casa_input == 'Kenya': return 'File:Flag_of_Kenya.svg'
    elif equipo_casa_input == 'Kosovo': return 'File:Flag_of_Kosovo.svg'
    elif equipo_casa_input == 'Kuwait': return 'File:Flag_of_Kuwait.svg'
    elif equipo_casa_input == 'Kyrgyzstan': return 'File:Flag_of_Kyrgyzstan.svg'
    elif equipo_casa_input == 'Laos': return 'File:Flag_of_Laos.svg'
    elif equipo_casa_input == 'Latvia': return 'File:Flag_of_Latvia.svg'
    elif equipo_casa_input == 'Lebanon': return 'File:Flag_of_Lebanon.svg'
    elif equipo_casa_input == 'Lesotho': return 'File:Flag_of_Lesotho.svg'
    elif equipo_casa_input == 'Liberia': return 'File:Flag_of_Liberia.svg'
    elif equipo_casa_input == 'Libya': return 'File:Flag_of_Libya.svg'
    elif equipo_casa_input == 'Liechtenstein': return 'File:Flag_of_Liechtenstein.svg'
    elif equipo_casa_input == 'Lithuania': return 'File:Flag_of_Lithuania.svg'
    elif equipo_casa_input == 'Luxembourg': return 'File:Flag_of_Luxembourg.svg'
    elif equipo_casa_input == 'Macau': return 'File:Flag_of_Macau.svg'
    elif equipo_casa_input == 'Madagascar': return 'File:Flag_of_Madagascar.svg'
    elif equipo_casa_input == 'Malawi': return 'File:Flag_of_Malawi.svg'
    elif equipo_casa_input == 'Malaysia': return 'File:Flag_of_Malaysia.svg'
    elif equipo_casa_input == 'Maldives': return 'File:Flag_of_Maldives.svg'
    elif equipo_casa_input == 'Mali': return 'File:Flag_of_Mali.svg'
    elif equipo_casa_input == 'Malta': return 'File:Flag_of_Malta.svg'
    elif equipo_casa_input == 'Martinique': return 'File:Flag_of_Martinique.svg'
    elif equipo_casa_input == 'Mauritania': return 'File:Flag_of_Mauritania.svg'
    elif equipo_casa_input == 'Mauritius': return 'File:Flag_of_Mauritius.svg'
    elif equipo_casa_input == 'Mexico': return 'File:Flag_of_Mexico.svg'
    elif equipo_casa_input == 'Moldova': return 'File:Flag_of_Moldova.svg'
    elif equipo_casa_input == 'Mongolia': return 'File:Flag_of_Mongolia.svg'
    elif equipo_casa_input == 'Montenegro': return 'File:Flag_of_Montenegro.svg'
    elif equipo_casa_input == 'Montserrat': return 'File:Flag_of_Montserrat.svg'
    elif equipo_casa_input == 'Morocco': return 'File:Flag_of_Morocco.svg'
    elif equipo_casa_input == 'Mozambique': return 'File:Flag_of_Mozambique.svg'
    elif equipo_casa_input == 'Myanmar': return 'File:Flag_of_Myanmar.svg'
    elif equipo_casa_input == 'Namibia': return 'File:Flag_of_Namibia.svg'
    elif equipo_casa_input == 'Nepal': return 'File:Flag_of_Nepal.svg'
    elif equipo_casa_input == 'Netherlands': return 'File:Flag_of_Netherlands.svg'
    elif equipo_casa_input == 'New Caledonia': return 'File:Flag_of_New_Caledonia.svg'
    elif equipo_casa_input == 'New Zealand': return 'File:Flag_of_New_Zealand.svg'
    elif equipo_casa_input == 'Nicaragua': return 'File:Flag_of_Nicaragua.svg'
    elif equipo_casa_input == 'Niger': return 'File:Flag_of_Niger.svg'
    elif equipo_casa_input == 'Nigeria': return 'File:Flag_of_Nigeria.svg'
    elif equipo_casa_input == 'North Korea': return 'File:Flag_of_North_Korea.svg'
    elif equipo_casa_input == 'North Macedonia': return 'File:Flag_of_North_Macedonia.svg'
    elif equipo_casa_input == 'Northern Ireland': return 'File:Flag_of_Northern_Ireland.svg'
    elif equipo_casa_input == 'Northern Mariana Islands': return 'File:Flag_of_Northern_Mariana_Islands.svg'
    elif equipo_casa_input == 'Norway': return 'File:Flag_of_Norway.svg'
    elif equipo_casa_input == 'Oman': return 'File:Flag_of_Oman.svg'
    elif equipo_casa_input == 'Pakistan': return 'File:Flag_of_Pakistan.svg'
    elif equipo_casa_input == 'Palestine': return 'File:Flag_of_Palestine.svg'
    elif equipo_casa_input == 'Panama': return 'File:Flag_of_Panama.svg'
    elif equipo_casa_input == 'Papua New Guinea': return 'File:Flag_of_Papua_New_Guinea.svg'
    elif equipo_casa_input == 'Paraguay': return 'File:Flag_of_Paraguay.svg'
    elif equipo_casa_input == 'Peru': return 'File:Flag_of_Peru.svg'
    elif equipo_casa_input == 'Philippines': return 'File:Flag_of_Philippines.svg'
    elif equipo_casa_input == 'Poland': return 'File:Flag_of_Poland.svg'
    elif equipo_casa_input == 'Portugal': return 'File:Flag_of_Portugal.svg'
    elif equipo_casa_input == 'Puerto Rico': return 'File:Flag_of_Puerto_Rico.svg'
    elif equipo_casa_input == 'Qatar': return 'File:Flag_of_Qatar.svg'
    elif equipo_casa_input == 'Rep of Ireland': return 'File:Flag_of_Ireland.svg'
    elif equipo_casa_input == 'Romania': return 'File:Flag_of_Romania.svg'
    elif equipo_casa_input == 'Russia': return 'File:Flag_of_Russia.svg'
    elif equipo_casa_input == 'Rwanda': return 'File:Flag_of_Rwanda.svg'
    elif equipo_casa_input == 'San Marino': return 'File:Flag_of_San_Marino.svg'
    elif equipo_casa_input == 'Sao Tome and Principe': return 'File:Flag_of_Sao_Tome_and_Principe.svg'
    elif equipo_casa_input == 'Saudi Arabia': return 'File:Flag_of_Saudi_Arabia.svg'
    elif equipo_casa_input == 'Scotland': return 'File:Flag_of_Scotland.svg'
    elif equipo_casa_input == 'Senegal': return 'File:Flag_of_Senegal.svg'
    elif equipo_casa_input == 'Serbia': return 'File:Flag_of_Serbia.svg'
    elif equipo_casa_input == 'Seychelles': return 'File:Flag_of_Seychelles.svg'
    elif equipo_casa_input == 'Sierra Leone': return 'File:Flag_of_Sierra_Leone.svg'
    elif equipo_casa_input == 'Singapore': return 'File:Flag_of_Singapore.svg'
    elif equipo_casa_input == 'Sint Maarten': return 'File:Flag_of_Sint_Maarten.svg'
    elif equipo_casa_input == 'Slovakia': return 'File:Flag_of_Slovakia.svg'
    elif equipo_casa_input == 'Slovenia': return 'File:Flag_of_Slovenia.svg'
    elif equipo_casa_input == 'Solomon Islands': return 'File:Flag_of_Solomon_Islands.svg'
    elif equipo_casa_input == 'Somalia': return 'File:Flag_of_Somalia.svg'
    elif equipo_casa_input == 'South Africa': return 'File:Flag_of_South_Africa.svg'
    elif equipo_casa_input == 'South Korea': return 'File:Flag_of_South_Korea.svg'
    elif equipo_casa_input == 'South Sudan': return 'File:Flag_of_South_Sudan.svg'
    elif equipo_casa_input == 'Spain': return 'File:Flag_of_Spain.svg'
    elif equipo_casa_input == 'Sri Lanka': return 'File:Flag_of_Sri_Lanka.svg'
    elif equipo_casa_input == 'St. Kitts and Nevis': return 'File:Flag_of_Saint_Kitts_and_Nevis.svg'
    elif equipo_casa_input == 'St. Lucia': return 'File:Flag_of_Saint_Lucia.svg'
    elif equipo_casa_input == 'St. Martin': return 'File:Saint-Martin_Flag.svg'
    elif equipo_casa_input == 'St. Vincent and the Grenadines': return 'File:Flag_of_Saint_Vincent_and_the_Grenadines.svg'
    elif equipo_casa_input == 'Sudan': return 'File:Flag_of_Sudan.svg'
    elif equipo_casa_input == 'Suriname': return 'File:Flag_of_Suriname.svg'
    elif equipo_casa_input == 'Swaziland': return 'File:Flag_of_Eswatini.svg'
    elif equipo_casa_input == 'Sweden': return 'File:Flag_of_Sweden.svg'
    elif equipo_casa_input == 'Switzerland': return 'File:Flag_of_Switzerland.svg'
    elif equipo_casa_input == 'Syria': return 'File:Flag_of_Syria.svg'
    elif equipo_casa_input == 'Tahiti': return 'File:Flag_of_Tahiti.svg'
    elif equipo_casa_input == 'Tajikistan': return 'File:Flag_of_Tajikistan.svg'
    elif equipo_casa_input == 'Tanzania': return 'File:Flag_of_Tanzania.svg'
    elif equipo_casa_input == 'Thailand': return 'File:Flag_of_Thailand.svg'
    elif equipo_casa_input == 'Timor-Leste': return 'File:Flag_of_East_Timor.svg'
    elif equipo_casa_input == 'Togo': return 'File:Flag_of_Togo.svg'
    elif equipo_casa_input == 'Tonga': return 'File:Flag_of_Tonga.svg'
    elif equipo_casa_input == 'Trinidad and Tobago': return 'File:Flag_of_Trinidad_and_Tobago.svg'
    elif equipo_casa_input == 'Tunisia': return 'File:Flag_of_Tunisia.svg'
    elif equipo_casa_input == 'Turkey': return 'File:Flag_of_Turkey.svg'
    elif equipo_casa_input == 'Turkmenistan': return 'File:Flag_of_Turkmenistan.svg'
    elif equipo_casa_input == 'Turks and Caicos Islands': return 'File:Flag_of_Turks_and_Caicos_Islands.svg'
    elif equipo_casa_input == 'Tuvalu': return 'File:Flag_of_Tuvalu.svg'
    elif equipo_casa_input == 'Uganda': return 'File:Flag_of_Uganda.svg'
    elif equipo_casa_input == 'Ukraine': return 'File:Flag_of_Ukraine.svg'
    elif equipo_casa_input == 'United Arab Emirates': return 'File:Flag_of_United_Arab_Emirates.svg'
    elif equipo_casa_input == 'Uruguay': return 'File:Flag_of_Uruguay.svg'
    elif equipo_casa_input == 'US Virgin Islands': return 'File:Flag_of_the_United_States_Virgin_Islands.svg'
    elif equipo_casa_input == 'USA': return 'File:Flag_of_the_United_States.svg'
    elif equipo_casa_input == 'Uzbekistan': return 'File:Flag_of_Uzbekistan.svg'
    elif equipo_casa_input == 'Vanuatu': return 'File:Flag_of_Vanuatu.svg'
    elif equipo_casa_input == 'Venezuela': return 'File:Flag_of_Venezuela.svg'
    elif equipo_casa_input == 'Vietnam': return 'File:Flag_of_Vietnam.svg'
    elif equipo_casa_input == 'Wales': return 'File:Flag_of_Wales.svg'
    elif equipo_casa_input == 'Yemen': return 'File:Flag_of_Yemen.svg'
    elif equipo_casa_input == 'Zambia': return 'File:Flag_of_Zambia.svg'
    elif equipo_casa_input == 'Zanzibar': return 'File:Flag_of_Zanzibar.svg'
    elif equipo_casa_input == 'Zimbabwe': return 'File:Flag_of_Zimbabwe.svg'
    elif equipo_casa_input == 'Manchester City': return 'Manchester City'
    elif equipo_casa_input == 'Paris Saint-Germain': return 'Paris Saint-Germain'
    elif equipo_casa_input == 'Liverpool': return 'Liverpool'
    elif equipo_casa_input == 'Barcelona': return 'Barcelona'
    elif equipo_casa_input == 'Real Madrid': return 'Real Madrid'
    elif equipo_casa_input == 'Ajax': return 'Ajax'
    elif equipo_casa_input == 'Tottenham Hotspur': return 'Tottenham Hotspur'
    elif equipo_casa_input == 'FC Salzburg': return 'Salzburg FC'
    elif equipo_casa_input == 'Chelsea': return 'Chelsea'
    elif equipo_casa_input == 'Arsenal': return 'Arsenal'
    elif equipo_casa_input == 'Internazionale': return 'Football Club Internazionale Milano'
    elif equipo_casa_input == 'Atletico Madrid': return 'Atletico Madrid'
    elif equipo_casa_input == 'FC Porto': return 'Porto FC'
    elif equipo_casa_input == 'Napoli': return 'Napoli'
    elif equipo_casa_input == 'Borussia Dortmund': return 'Borussia Dortmund'
    elif equipo_casa_input == 'Villarreal': return 'Villarreal'
    elif equipo_casa_input == 'AC Milan': return 'Milan AC'
    elif equipo_casa_input == 'RB Leipzig': return 'Leipzig RB'
    elif equipo_casa_input == 'Sporting CP': return 'Sporting CP'
    elif equipo_casa_input == 'Benfica': return 'Benfica'
    elif equipo_casa_input == 'Brighton and Hove Albion': return 'Brighton and Hove'
    elif equipo_casa_input == 'Celtic': return 'Celtic'
    elif equipo_casa_input == 'PSV': return 'Eindhoven PSV'
    elif equipo_casa_input == 'Zenit St Petersburg': return 'Zenit St Petersburg'
    elif equipo_casa_input == 'Manchester United': return 'Manchester United'
    elif equipo_casa_input == 'Real Sociedad': return 'Real Sociedad'
    elif equipo_casa_input == 'Athletic Bilbao': return 'Athletic Bilbao'
    elif equipo_casa_input == 'Bayer Leverkusen': return 'Bayer Leverkusen'
    elif equipo_casa_input == 'Lyon': return 'Lyon'
    elif equipo_casa_input == 'Newcastle': return 'Newcastle'
    elif equipo_casa_input == 'Atalanta': return 'Atalanta'
    elif equipo_casa_input == 'Stade Rennes': return 'Stade Rennes'
    elif equipo_casa_input == 'Marseille': return 'Marseille'
    elif equipo_casa_input == 'AS Roma': return 'Roma AS'
    elif equipo_casa_input == 'Feyenoord': return 'Feyenoord'
    elif equipo_casa_input == 'Real Betis': return 'Real Betis'
    elif equipo_casa_input == 'West Ham United': return 'West Ham United'
    elif equipo_casa_input == '1. FC Union Berlin': return 'Union FC 1'
    elif equipo_casa_input == 'SC Freiburg': return 'Freiburg SC'
    elif equipo_casa_input == 'Aston Villa': return 'Aston Villa'
    elif equipo_casa_input == 'Crystal Palace': return 'Crystal Palace'
    elif equipo_casa_input == 'Valencia': return 'Valencia'
    elif equipo_casa_input == 'Borussia Monchengladbach': return 'Borussia Monchengladbach'
    elif equipo_casa_input == 'Club Brugge': return 'Club Brugge'
    elif equipo_casa_input == 'Juventus': return 'Juventus'
    elif equipo_casa_input == 'Lazio': return 'Lazio'
    elif equipo_casa_input == 'Brentford': return 'Brentford'
    elif equipo_casa_input == 'AS Monaco': return 'Monaco AS'
    elif equipo_casa_input == 'Celta Vigo': return 'Celta Vigo'
    elif equipo_casa_input == 'Flamengo': return 'Flamengo'
    elif equipo_casa_input == 'TSG Hoffenheim': return 'Hoffenheim TSG'
    elif equipo_casa_input == 'FC Cologne': return 'Cologne FC'
    elif equipo_casa_input == 'Lille': return 'Lille'
    elif equipo_casa_input == 'Rangers': return 'Rangers'
    elif equipo_casa_input == 'Eintracht Frankfurt': return 'Eintracht Frankfurt'
    elif equipo_casa_input == 'Lens': return 'Lens'
    elif equipo_casa_input == 'Osasuna': return 'Osasuna'
    elif equipo_casa_input == 'Mainz': return 'Mainz'
    elif equipo_casa_input == 'Sevilla FC': return 'Sevilla FC'
    elif equipo_casa_input == 'Braga': return 'Braga'
    elif equipo_casa_input == 'Wolverhampton': return 'Wolverhampton'
    elif equipo_casa_input == 'Leicester City': return 'Leicester City'
    elif equipo_casa_input == 'Fiorentina': return 'Fiorentina'
    elif equipo_casa_input == 'VfB Stuttgart': return 'Stuttgart VfB'
    elif equipo_casa_input == 'VfL Wolfsburg': return 'Wolfsburg VfL'
    elif equipo_casa_input == 'Strasbourg': return 'Strasbourg'
    elif equipo_casa_input == 'Fenerbahce': return 'Fenerbahce'
    elif equipo_casa_input == 'AZ': return 'Alkmaar AZ'
    elif equipo_casa_input == 'FC Twente': return 'Twente FC'
    elif equipo_casa_input == 'Slavia Prague': return 'Slavia Prague'
    elif equipo_casa_input == 'Leeds United': return 'Leeds United'
    elif equipo_casa_input == 'Monterrey': return 'Monterrey'
    elif equipo_casa_input == 'Nice': return 'Nice'
    elif equipo_casa_input == 'Southampton': return 'Southampton'
    elif equipo_casa_input == 'Club América': return 'America AmÃ©rica'
    elif equipo_casa_input == 'Everton': return 'Everton'
    elif equipo_casa_input == 'Dinamo Zagreb': return 'Dinamo Zagreb'
    elif equipo_casa_input == 'Torino': return 'Torino'
    elif equipo_casa_input == 'Palmeiras': return 'Palmeiras'
    elif equipo_casa_input == 'Genk': return 'Genk'
    elif equipo_casa_input == 'Udinese': return 'Udinese'
    elif equipo_casa_input == 'Young Boys': return 'Young Boys'
    elif equipo_casa_input == 'Rayo Vallecano': return 'Rayo Vallecano'
    elif equipo_casa_input == 'Atletico Mineiro': return 'Atletico Mineiro'
    elif equipo_casa_input == 'Werder Bremen': return 'Werder Bremen'
    elif equipo_casa_input == 'Internacional': return 'Internacional'
    elif equipo_casa_input == 'Shakhtar Donetsk': return 'Shakhtar Donetsk'
    elif equipo_casa_input == 'Fulham': return 'Fulham'
    elif equipo_casa_input == 'Hertha Berlin': return 'Hertha Berlin'
    elif equipo_casa_input == 'Espanyol': return 'Espanyol'
    elif equipo_casa_input == 'Getafe': return 'Getafe'
    elif equipo_casa_input == 'Girona FC': return 'Girona FC'
    elif equipo_casa_input == 'Norwich City': return 'Norwich City'
    elif equipo_casa_input == 'Philadelphia Union': return 'Philadelphia Union'
    elif equipo_casa_input == 'Sassuolo': return 'Sassuolo'
    elif equipo_casa_input == 'Almeria': return 'Almeria'
    elif equipo_casa_input == 'Slovácko': return 'Slovacko'
    elif equipo_casa_input == 'Verona': return 'Verona'
    elif equipo_casa_input == 'São Paolo': return 'Sao Paulo'
    elif equipo_casa_input == 'Nantes': return 'Nantes'
    elif equipo_casa_input == 'Schalke 04': return 'Schalke 4'
    elif equipo_casa_input == 'Fluminense': return 'Fluminense'
    elif equipo_casa_input == 'Tigres UANL': return 'Tigres UANL'
    elif equipo_casa_input == 'Mallorca': return 'Mallorca'
    elif equipo_casa_input == 'Pachuca': return 'Pachuca'
    elif equipo_casa_input == 'CSKA Moscow': return 'Moscow CSKA'
    elif equipo_casa_input == 'Steaua Bucuresti': return 'Steaua Bucuresti'
    elif equipo_casa_input == 'Olympiacos': return 'Olympiacos'
    elif equipo_casa_input == 'Sheffield United': return 'Sheffield United'
    elif equipo_casa_input == 'River Plate': return 'River Plate'
    elif equipo_casa_input == 'Red Star Belgrade': return 'Red Star Belgrade'
    elif equipo_casa_input == 'Real Valladolid': return 'Real Valladolid'
    elif equipo_casa_input == 'Reims': return 'Reims'
    elif equipo_casa_input == 'Trabzonspor': return 'Trabzonspor'
    elif equipo_casa_input == 'FC Augsburg': return 'Augsburg FC'
    elif equipo_casa_input == 'Spartak Moscow': return 'Spartak Moscow'
    elif equipo_casa_input == 'FC Utrecht': return 'Utrecht FC'
    elif equipo_casa_input == 'Anderlecht': return 'Anderlecht'
    elif equipo_casa_input == 'Antwerp': return 'Antwerp'
    elif equipo_casa_input == 'West Bromwich Albion': return 'West Bromwich Albion'
    elif equipo_casa_input == 'VfL Bochum': return 'Bochum VfL'
    elif equipo_casa_input == 'Cadiz': return 'Cadiz'
    elif equipo_casa_input == 'Corinthians': return 'Corinthians'
    elif equipo_casa_input == 'Ferencvaros': return 'Ferencvaros'
    elif equipo_casa_input == 'SC Dnipro-1': return 'Dnipro-1 SC'
    elif equipo_casa_input == 'Lorient': return 'Lorient'
    elif equipo_casa_input == 'Molde': return 'Molde'
    elif equipo_casa_input == 'Istanbul Basaksehir': return 'Istanbul Basaksehir'
    elif equipo_casa_input == 'Bodo/Glimt': return 'Bodo/Glimt'
    elif equipo_casa_input == 'Bragantino': return 'Bragantino'
    elif equipo_casa_input == 'Dynamo Kiev': return 'Dynamo Kiev'
    elif equipo_casa_input == 'Nottingham Forest': return 'Nottingham Forest'
    elif equipo_casa_input == 'Watford': return 'Watford'
    elif equipo_casa_input == 'Bologna': return 'Bologna'
    elif equipo_casa_input == 'Los Angeles FC': return 'Los Angeles FC'
    elif equipo_casa_input == 'Viktoria Plzen': return 'Viktoria Plzen'
    elif equipo_casa_input == 'AFC Bournemouth': return 'Bournemouth AFC'
    elif equipo_casa_input == 'KAA Gent': return 'Gent KAA'
    elif equipo_casa_input == 'FC Sheriff Tiraspol': return 'Sheriff Tiraspol FC'
    elif equipo_casa_input == 'Elche': return 'Elche'
    elif equipo_casa_input == 'FC Copenhagen': return 'Copenhagen FC'
    elif equipo_casa_input == 'Kawasaki Frontale': return 'Kawasaki Frontale'
    elif equipo_casa_input == 'Montpellier': return 'Montpellier'
    elif equipo_casa_input == 'SK Sturm Graz': return 'Sturm Graz FK'
    elif equipo_casa_input == 'Besiktas': return 'Besiktas'
    elif equipo_casa_input == 'Troyes': return 'Troyes'
    elif equipo_casa_input == 'Toulouse': return 'Toulouse'
    elif equipo_casa_input == 'Burnley': return 'Burnley'
    elif equipo_casa_input == 'Yokohama F. Marinos': return 'Yokohama F. Marinos'
    elif equipo_casa_input == 'Vitesse': return 'Vitesse'
    elif equipo_casa_input == 'Sampdoria': return 'Sampdoria'
    elif equipo_casa_input == 'Guimaraes': return 'Guimaraes'
    elif equipo_casa_input == 'Gil Vicente': return 'Gil Vicente'
    elif equipo_casa_input == 'Lecce': return 'Lecce'
    elif equipo_casa_input == 'Brest': return 'Brest'
    elif equipo_casa_input == 'Angers': return 'Angers'
    elif equipo_casa_input == 'FC Krasnodar': return 'Krasnodar FC'
    elif equipo_casa_input == 'Santos': return 'Santos'
    elif equipo_casa_input == 'Galatasaray': return 'Galatasaray'
    elif equipo_casa_input == 'Ceará': return 'Ceara Sporting Club'
    elif equipo_casa_input == 'Dinamo Moscow': return 'Dinamo Moscow'
    elif equipo_casa_input == 'Guadalajara': return 'Guadalajara'
    elif equipo_casa_input == 'FC Midtjylland': return 'Midtjylland FC'
    elif equipo_casa_input == 'Levante': return 'Levante'
    elif equipo_casa_input == 'AC Ajaccio': return 'Ajaccio AC'
    elif equipo_casa_input == 'FK Partizan Belgrade': return 'Partizan Belgrade FK'
    elif equipo_casa_input == 'LASK Linz': return 'Linz LASK'
    elif equipo_casa_input == 'Fortaleza': return 'Fortaleza'
    elif equipo_casa_input == 'Santos Laguna': return 'Santos Laguna'
    elif equipo_casa_input == 'Union Saint Gilloise': return 'Union Saint Gilloise'
    elif equipo_casa_input == 'Atlético Paranaense': return 'Atletico Paranaense'
    elif equipo_casa_input == 'Urawa Red Diamonds': return 'Urawa Red Diamonds'
    elif equipo_casa_input == 'Clermont Foot': return 'Clermont Foot'
    elif equipo_casa_input == 'Sochi': return 'Sochi'
    elif equipo_casa_input == 'Cremonese': return 'Cremonese'
    elif equipo_casa_input == 'Empoli': return 'Empoli'
    elif equipo_casa_input == 'Heerenveen': return 'Heerenveen'
    elif equipo_casa_input == 'New York City FC': return 'New York City'
    elif equipo_casa_input == 'Middlesbrough': return 'Middlesbrough'
    elif equipo_casa_input == 'Konyaspor': return 'Konyaspor'
    elif equipo_casa_input == 'Salernitana': return 'Salernitana'
    elif equipo_casa_input == 'Lech Poznan': return 'Lech Poznan'
    elif equipo_casa_input == 'Auxerre': return 'Auxerre'
    elif equipo_casa_input == 'NEC': return 'NEC'
    elif equipo_casa_input == 'Montreal Impact': return 'Montreal Impact'
    elif equipo_casa_input == 'América Mineiro': return 'America Futebol Clube MG'
    elif equipo_casa_input == 'Portimonense': return 'Portimonense'
    elif equipo_casa_input == 'Monza': return 'Monza'
    elif equipo_casa_input == 'Famalicao': return 'Famalicao'
    elif equipo_casa_input == 'Rostov': return 'Rostov'
    elif equipo_casa_input == "Hapoel Be'er': return 'Hapoel Be'er"
    elif equipo_casa_input == 'Basel': return 'Basel'
    elif equipo_casa_input == 'Spezia': return 'Spezia'
    elif equipo_casa_input == 'St Etienne': return 'Etienne'
    elif equipo_casa_input == 'Chaves': return 'Chaves'
    elif equipo_casa_input == 'Vizela': return 'Vizela'
    elif equipo_casa_input == 'Cuiaba': return 'Cuiaba'
    elif equipo_casa_input == 'Rosenborg': return 'Rosenborg'
    elif equipo_casa_input == 'León': return 'Leon'
    elif equipo_casa_input == 'Boca Juniors': return 'Boca Juniors'
    elif equipo_casa_input == 'Apollon Limassol': return 'Apollon Limassol'
    elif equipo_casa_input == 'Estoril Praia': return 'Estoril Praia'
    elif equipo_casa_input == 'Cagliari': return 'Cagliari'
    elif equipo_casa_input == 'St Gallen': return 'Gallen'
    elif equipo_casa_input == 'Bordeaux': return 'Bordeaux'
    elif equipo_casa_input == 'Hamburg SV': return 'Hamburg SV'
    elif equipo_casa_input == 'Metz': return 'Metz'
    elif equipo_casa_input == 'Santa Clara': return 'Santa Clara'
    elif equipo_casa_input == 'Botafogo': return 'Botafogo'
    elif equipo_casa_input == 'PAOK Salonika': return 'Salonika PAOK'
    elif equipo_casa_input == 'Puebla': return 'Puebla'
    elif equipo_casa_input == 'Maccabi Haifa': return 'Maccabi Haifa'
    elif equipo_casa_input == 'Granada': return 'Granada'
    elif equipo_casa_input == 'Boavista': return 'Boavista'
    elif equipo_casa_input == 'New York Red Bulls': return 'New York Red Bulls'
    elif equipo_casa_input == 'FK Austria Vienna': return 'Austria Vienna FK'
    elif equipo_casa_input == 'Rio Ave': return 'Rio Ave'
    elif equipo_casa_input == 'Nashville SC': return 'Nashville SC'
    elif equipo_casa_input == 'Adana Demirspor': return 'Adana Demirspor'
    elif equipo_casa_input == 'Panathinaikos': return 'Panathinaikos'
    elif equipo_casa_input == 'Sparta': return 'Sparta'
    elif equipo_casa_input == 'Los Angeles Galaxy': return 'Los Angeles Galaxy'
    elif equipo_casa_input == 'Atlas': return 'Atlas'
    elif equipo_casa_input == 'Silkeborg': return 'Silkeborg'
    elif equipo_casa_input == 'FC Groningen': return 'Groningen FC'
    elif equipo_casa_input == 'RKC': return 'Waalwijk RKC'
    elif equipo_casa_input == 'Cruz Azul': return 'Cruz Azul'
    elif equipo_casa_input == 'Parma': return 'Parma'
    elif equipo_casa_input == 'Sochaux': return 'Sochaux'
    elif equipo_casa_input == 'Casa Pia': return 'Casa Pia'
    elif equipo_casa_input == 'Rapid Vienna': return 'Rapid Vienna'
    elif equipo_casa_input == 'Atlanta United FC': return 'Atlanta United FC'
    elif equipo_casa_input == 'Sporting de Charleroi': return 'Sporting de Charleroi'
    elif equipo_casa_input == 'Lokomotiv Moscow': return 'Lokomotiv Moscow'
    elif equipo_casa_input == 'AEK Athens': return 'AEK Athens'
    elif equipo_casa_input == 'Millwall': return 'Millwall'
    elif equipo_casa_input == 'Randers FC': return 'Randers FC'
    elif equipo_casa_input == 'Huracán': return 'Huracan'
    elif equipo_casa_input == 'Luton Town': return 'Luton Town'
    elif equipo_casa_input == 'Preston North End': return 'Preston North End'
    elif equipo_casa_input == 'Austin FC': return 'Austin FC'
    elif equipo_casa_input == 'Toluca': return 'Toluca'
    elif equipo_casa_input == 'Sanfrecce Hiroshima': return 'Sanfrecce Hiroshima'
    elif equipo_casa_input == 'Emmen': return 'Emmen'
    elif equipo_casa_input == 'FK Qarabag': return 'Qarabag FK'
    elif equipo_casa_input == 'Stoke City': return 'Stoke City'
    elif equipo_casa_input == 'Pumas Unam': return 'Pumas Unam'
    elif equipo_casa_input == 'Velez Sarsfield': return 'Velez Sarsfield'
    elif equipo_casa_input == 'AEK Larnaca': return 'Larnaca AEK'
    elif equipo_casa_input == 'Alanyaspor': return 'Alanyaspor'
    elif equipo_casa_input == 'FC Nordsjaelland': return 'Nordsjaelland FC'
    elif equipo_casa_input == 'Genoa': return 'Genoa'
    elif equipo_casa_input == 'Go Ahead Eagles': return 'Go Ahead Eagles'
    elif equipo_casa_input == 'Bristol City': return 'Bristol City'
    elif equipo_casa_input == 'Antalyaspor': return 'Antalyaspor'
    elif equipo_casa_input == 'Wolfsberger AC': return 'Wolfsberger AC'
    elif equipo_casa_input == 'Seattle Sounders FC': return 'Seattle Sounders FC'
    elif equipo_casa_input == 'Racing Club': return 'Racing Club'
    elif equipo_casa_input == 'St. Truidense': return 'Truidense'
    elif equipo_casa_input == 'Cerezo Osaka': return 'Cerezo Osaka'
    elif equipo_casa_input == 'Valerenga': return 'Valerenga'
    elif equipo_casa_input == 'Queens Park Rangers': return 'Queens Park Rangers'
    elif equipo_casa_input == 'Coventry City': return 'Coventry City'
    elif equipo_casa_input == 'CFR 1907 Cluj': return 'Cluj 1907 CFR'
    elif equipo_casa_input == 'Cambuur Leeuwarden': return 'Cambuur Leeuwarden'
    elif equipo_casa_input == 'Aberdeen': return 'Aberdeen'
    elif equipo_casa_input == 'Necaxa': return 'Necaxa'
    elif equipo_casa_input == 'Caen': return 'Caen'
    elif equipo_casa_input == 'Estudiantes': return 'Estudiantes'
    elif equipo_casa_input == 'Columbus Crew': return 'Columbus Crew'
    elif equipo_casa_input == 'Kashima Antlers': return 'Kashima Antlers'
    elif equipo_casa_input == 'FC Dallas': return 'Dallas FC'
    elif equipo_casa_input == 'Terek Grozny': return 'Terek Grozny'
    elif equipo_casa_input == 'Orlando City SC': return 'Orlando City SC'
    elif equipo_casa_input == 'Djurgardens IF': return 'Djurgardens IF'
    elif equipo_casa_input == 'Tijuana': return 'Tijuana'
    elif equipo_casa_input == 'Atlético Goianiense': return 'Atletico Goianiense'
    elif equipo_casa_input == 'Talleres de Córdoba': return 'Talleres de Cordoba'
    elif equipo_casa_input == 'Tigre': return 'Tigre'
    elif equipo_casa_input == 'Gazisehir Gaziantep': return 'Gazisehir Gaziantep'
    elif equipo_casa_input == 'Kasimpasa': return 'Kasimpasa'
    elif equipo_casa_input == 'Swansea City': return 'Swansea City'
    elif equipo_casa_input == 'Argentinos Juniors': return 'Argentinos Juniors'
    elif equipo_casa_input == 'Brondby': return 'Brondby'
    elif equipo_casa_input == 'Krylia Sovetov': return 'Krylia Sovetov'
    elif equipo_casa_input == 'New England Revolution': return 'New England Revolution'
    elif equipo_casa_input == 'FC Volendam': return 'Volendam FC'
    elif equipo_casa_input == 'Maritimo': return 'Maritimo'
    elif equipo_casa_input == 'SV Darmstadt 98': return 'Darmstadt SV 98'
    elif equipo_casa_input == 'Hammarby': return 'Hammarby'
    elif equipo_casa_input == 'Ludogorets': return 'Ludogorets'
    elif equipo_casa_input == 'Portland Timbers': return 'Portland Timbers'
    elif equipo_casa_input == 'Goiás': return 'Goias'
    elif equipo_casa_input == 'San Lorenzo': return 'San Lorenzo'
    elif equipo_casa_input == 'FC Cincinnati': return 'Cincinnati FC'
    elif equipo_casa_input == 'Lillestrom': return 'Lillestrom'
    elif equipo_casa_input == 'FC Arouca': return 'Arouca FC'
    elif equipo_casa_input == 'Cardiff City': return 'Cardiff City'
    elif equipo_casa_input == 'Blackburn': return 'Blackburn'
    elif equipo_casa_input == 'CA Independiente': return 'Independiente CA'
    elif equipo_casa_input == 'Minnesota United FC': return 'Minnesota United FC'
    elif equipo_casa_input == 'Excelsior': return 'Excelsior'
    elif equipo_casa_input == 'OH Leuven': return 'Leuven OH'
    elif equipo_casa_input == 'Eibar': return 'Eibar'
    elif equipo_casa_input == 'Alavés': return 'Alaves'
    elif equipo_casa_input == 'Hearts': return 'Hearts'
    elif equipo_casa_input == 'Real Salt Lake': return 'Real Salt Lake'
    elif equipo_casa_input == 'Coritiba': return 'Coritiba'
    elif equipo_casa_input == 'KV Mechelen': return 'Mechelen KV'
    elif equipo_casa_input == 'Blackpool': return 'Blackpool'
    elif equipo_casa_input == 'Chicago Fire': return 'Chicago Fire'
    elif equipo_casa_input == 'FC Zurich': return 'Zurich FC'
    elif equipo_casa_input == 'BK Hacken': return 'Hacken BK'
    elif equipo_casa_input == 'Pacos Ferreira': return 'Pacos Ferreira'
    elif equipo_casa_input == 'Brescia': return 'Brescia'
    elif equipo_casa_input == 'Viborg': return 'Viborg'
    elif equipo_casa_input == 'Sheffield Wednesday': return 'Sheffield Wednesday'
    elif equipo_casa_input == 'Sunderland': return 'Sunderland'
    elif equipo_casa_input == 'SC Paderborn': return 'Paderborn SC'
    elif equipo_casa_input == 'Fortuna Düssseldorf': return 'Fortuna Dusseldorf'
    elif equipo_casa_input == 'Las Palmas': return 'Las Palmas'
    elif equipo_casa_input == 'Benevento': return 'Benevento'
    elif equipo_casa_input == 'Ipswich Town': return 'Ipswich Town'
    elif equipo_casa_input == 'Frosinone': return 'Frosinone'
    elif equipo_casa_input == 'Standard Liege': return 'Standard Liege'
    elif equipo_casa_input == 'Fortuna Sittard': return 'Fortuna Sittard'
    elif equipo_casa_input == 'Querétaro': return 'Queretaro'
    elif equipo_casa_input == 'FC Luzern': return 'Luzern FC'
    elif equipo_casa_input == 'Colorado Rapids': return 'Colorado Rapids'
    elif equipo_casa_input == 'Huddersfield Town': return 'Huddersfield Town'
    elif equipo_casa_input == 'Avaí': return 'Avai'
    elif equipo_casa_input == 'Hibernian': return 'Hibernian'
    elif equipo_casa_input == 'Slovan Bratislava': return 'Slovan Bratislava'
    elif equipo_casa_input == 'FC St. Pauli': return 'St Pauli FC'
    elif equipo_casa_input == 'FC Juárez': return 'Juarez FC'
    elif equipo_casa_input == 'Sporting Kansas City': return 'Sporting Kansas City'
    elif equipo_casa_input == 'Gimnasia La Plata': return 'Gimnasia La Plata'
    elif equipo_casa_input == "Newell's Old Boys': return 'Newell's Old Boys"
    elif equipo_casa_input == 'Kayserispor': return 'Kayserispor'
    elif equipo_casa_input == 'Aris Salonika': return 'Aris Salonika'
    elif equipo_casa_input == 'Paris FC': return 'Paris FC'
    elif equipo_casa_input == 'FK Nizhny Novgorod': return 'Nizhny Novgorod FK'
    elif equipo_casa_input == 'Mamelodi Sundowns': return 'Mamelodi Sundowns'
    elif equipo_casa_input == 'Union Santa Fe': return 'Union Santa Fe'
    elif equipo_casa_input == 'Toronto FC': return 'Toronto FC'
    elif equipo_casa_input == 'Hull City': return 'Hull City'
    elif equipo_casa_input == 'Viking FK': return 'Viking FK'
    elif equipo_casa_input == 'Derby County': return 'Derby County'
    elif equipo_casa_input == 'Real Oviedo': return 'Real Oviedo'
    elif equipo_casa_input == 'AaB': return 'Fodbold AaB'
    elif equipo_casa_input == 'Omonia Nicosia': return 'Omonia Nicosia'
    elif equipo_casa_input == 'Guingamp': return 'Guingamp'
    elif equipo_casa_input == 'Le Havre': return 'Havre Le'
    elif equipo_casa_input == 'Juventude': return 'Juventude'
    elif equipo_casa_input == 'Defensa y Justicia': return 'Defensa y Justicia'
    elif equipo_casa_input == 'Wigan': return 'Wigan'
    elif equipo_casa_input == 'Real Zaragoza': return 'Real Zaragoza'
    elif equipo_casa_input == 'F.B.C Unione Venezia': return 'Venezia Unione Venezia F.B.C.'
    elif equipo_casa_input == 'Lanus': return 'Lanus'
    elif equipo_casa_input == 'Arminia Bielefeld': return 'Arminia Bielefeld'
    elif equipo_casa_input == 'Servette': return 'Servette'
    elif equipo_casa_input == 'Malmo FF': return 'Malmo FF'
    elif equipo_casa_input == 'Fatih Karagümrük': return 'Fatih Karagümrük'
    elif equipo_casa_input == 'IFK Goteborg': return 'Goteborg IFK'
    elif equipo_casa_input == 'IF Elfsborg': return 'Elfsborg IF'
    elif equipo_casa_input == 'Mazatlán FC': return 'Mazatlan FC'
    elif equipo_casa_input == 'Sagan Tosu': return 'Sagan Tosu'
    elif equipo_casa_input == 'FC Tokyo': return 'Tokyo FC'
    elif equipo_casa_input == 'SD Huesca': return 'Huesca SD'
    elif equipo_casa_input == 'KVC Westerlo': return 'Westerlo KVC'
    elif equipo_casa_input == 'Rosario Central': return 'Rosario Central'
    elif equipo_casa_input == 'Reading': return 'Reading'
    elif equipo_casa_input == 'Karlsruher SC': return 'Karlsruher SC'
    elif equipo_casa_input == 'Atlético San Luis': return 'Atletico San Luis'
    elif equipo_casa_input == 'Amiens': return 'Amiens'
    elif equipo_casa_input == 'SK Austria Klagenfurt': return 'Austria SK Klagenfurt'
    elif equipo_casa_input == 'Inter Miami CF': return 'Inter Miami CF'
    elif equipo_casa_input == 'Austria Lustenau': return 'Austria Lustenau'
    elif equipo_casa_input == 'AGF Aarhus': return 'Aarhus AGF'
    elif equipo_casa_input == 'WSG Swarovski Wattens': return 'Swarovski Wattens WSG'
    elif equipo_casa_input == 'Cercle Brugge': return 'Cercle Brugge'
    elif equipo_casa_input == 'Sivasspor': return 'Sivasspor'
    elif equipo_casa_input == 'Sporting Gijón': return 'Sporting Gijón'
    elif equipo_casa_input == 'Nagoya Grampus Eight': return 'Nagoya Grampus Eight'
    elif equipo_casa_input == 'Birmingham': return 'Birmingham'
    elif equipo_casa_input == 'Godoy Cruz': return 'Godoy Cruz'
    elif equipo_casa_input == 'Livingston': return 'Livingston'
    elif equipo_casa_input == 'Dijon FCO': return 'Dijon FCO'
    elif equipo_casa_input == 'FC Lugano': return 'Lugano FC'
    elif equipo_casa_input == 'FC Cartagena': return 'Cartagena FC'
    elif equipo_casa_input == 'Rigas Futbola Skola': return 'Rigas Futbola Skola'
    elif equipo_casa_input == 'Banfield': return 'Banfield'
    elif equipo_casa_input == '1. FC Heidenheim 1846': return 'Heidenheim FC 1. 1846'
    elif equipo_casa_input == 'Rotherham United': return 'Rotherham United'
    elif equipo_casa_input == 'Platense': return 'Platense'
    elif equipo_casa_input == 'Hatayspor': return 'Hatayspor'
    elif equipo_casa_input == 'FC Sion': return 'Sion FC'
    elif equipo_casa_input == 'Hartberg': return 'Hartberg'
    elif equipo_casa_input == 'Central Córdoba Santiago del Estero': return 'Central Cordoba Santiago del Estero'
    elif equipo_casa_input == 'Grasshoppers Zürich': return 'Grasshoppers Zurich'
    elif equipo_casa_input == 'Stromsgodset': return 'Stromsgodset'
    elif equipo_casa_input == 'Ballkani': return 'Ballkani'
    elif equipo_casa_input == 'FC Khimki': return 'Khimki FC'
    elif equipo_casa_input == 'AIK': return 'Fotboll AIK'
    elif equipo_casa_input == 'Leganes': return 'Leganes'
    elif equipo_casa_input == 'Motherwell': return 'Motherwell'
    elif equipo_casa_input == 'Vancouver Whitecaps': return 'Vancouver Whitecaps'
    elif equipo_casa_input == 'Colon Santa Fe': return 'Colon Santa Fe'
    elif equipo_casa_input == 'Charlotte FC': return 'Charlotte FC'
    elif equipo_casa_input == 'Ascoli': return 'Ascoli'
    elif equipo_casa_input == 'San Jose Earthquakes': return 'San Jose Earthquakes'
    elif equipo_casa_input == 'Vissel Kobe': return 'Vissel Kobe'
    elif equipo_casa_input == 'Tenerife': return 'Tenerife'
    elif equipo_casa_input == 'Sarmiento': return 'Sarmiento'
    elif equipo_casa_input == 'Zalgiris Vilnius': return 'Zalgiris Vilnius'
    elif equipo_casa_input == 'Patronato': return 'Patronato'
    elif equipo_casa_input == 'Cittadella': return 'Cittadella'
    elif equipo_casa_input == 'Atlético Tucumán': return 'Atletico Tucuman'
    elif equipo_casa_input == 'Portsmouth': return 'Portsmouth'
    elif equipo_casa_input == 'KV Oostende': return 'Oostende KV'
    elif equipo_casa_input == 'KV Kortrijk': return 'Kortrijk KV'
    elif equipo_casa_input == 'Barnsley': return 'Barnsley'
    elif equipo_casa_input == '1. FC Nürnberg': return 'Nurnberg FC 1.'
    elif equipo_casa_input == 'DC United': return 'D.C. United'
    elif equipo_casa_input == 'Shimizu S-Pulse': return 'Shimizu S-Pulse'
    elif equipo_casa_input == 'Spal': return 'Spal'
    elif equipo_casa_input == 'Odense BK': return 'Odense BK'
    elif equipo_casa_input == 'Arsenal Sarandi': return 'Arsenal Sarandi'
    elif equipo_casa_input == 'Fakel Voronezh': return 'Fakel Voronezh'
    elif equipo_casa_input == 'Hannover 96': return 'Hannover 96'
    elif equipo_casa_input == 'Nimes': return 'Nimes'
    elif equipo_casa_input == 'Ross County': return 'Ross County'
    elif equipo_casa_input == 'Houston Dynamo': return 'Houston Dynamo'
    elif equipo_casa_input == 'Ternana': return 'Ternana'
    elif equipo_casa_input == 'Haugesund': return 'Haugesund'
    elif equipo_casa_input == 'SV Ried': return 'Ried SV'
    elif equipo_casa_input == 'Reggina': return 'Reggina'
    elif equipo_casa_input == 'Pisa': return 'Pisa'
    elif equipo_casa_input == 'Giresunspor': return 'Giresunspor'
    elif equipo_casa_input == 'Holstein Kiel': return 'Holstein Kiel'
    elif equipo_casa_input == 'Bari': return 'Bari'
    elif equipo_casa_input == 'Ural Sverdlovsk Oblast': return 'Ural Sverdlovsk Oblast'
    elif equipo_casa_input == 'Sarpsborg': return 'Sarpsborg'
    elif equipo_casa_input == 'Barracas Central': return 'Barracas Central'
    elif equipo_casa_input == 'Kashiwa Reysol': return 'Kashiwa Reysol'
    elif equipo_casa_input == 'SpVgg Greuther FÃ¼rth': return 'SpVgg Greuther FÃ¼rth'
    elif equipo_casa_input == 'Melbourne City': return 'Melbourne City'
    elif equipo_casa_input == 'Kilmarnock': return 'Kilmarnock'
    elif equipo_casa_input == 'Gazovik Orenburg': return 'Gazovik Orenburg'
    elif equipo_casa_input == 'AC Horsens': return 'Horsens AC'
    elif equipo_casa_input == 'Ankaragucu': return 'Ankaragucu'
    elif equipo_casa_input == 'St Mirren': return 'Mirren'
    elif equipo_casa_input == 'Tromso': return 'Tromso'
    elif equipo_casa_input == 'Volos NFC': return 'Volos NFC'
    elif equipo_casa_input == 'SD Ponferradina': return 'Ponferradina SD'
    elif equipo_casa_input == 'Valenciennes': return 'Valenciennes'
    elif equipo_casa_input == 'Burgos': return 'Burgos'
    elif equipo_casa_input == 'Perugia': return 'Perugia'
    elif equipo_casa_input == 'SV Zulte Waregem': return 'Zulte SV Waregem'
    elif equipo_casa_input == 'Tampa Bay Rowdies': return 'Tampa Bay Rowdies'
    elif equipo_casa_input == 'Umraniyespor': return 'Umraniyespor'
    elif equipo_casa_input == 'St Johnstone': return 'Johnstone'
    elif equipo_casa_input == 'Kalmar FF': return 'Kalmar FF'
    elif equipo_casa_input == 'Villarreal B': return 'Villarreal B'
    elif equipo_casa_input == 'Peterborough United': return 'Peterborough United'
    elif equipo_casa_input == 'Consadole Sapporo': return 'Consadole Sapporo'
    elif equipo_casa_input == 'Mirandes': return 'Mirandes'
    elif equipo_casa_input == 'Atromitos': return 'Atromitos'
    elif equipo_casa_input == 'UD Ibiza': return 'Ibiza UD'
    elif equipo_casa_input == 'Bastia': return 'Bastia'
    elif equipo_casa_input == 'IFK Norrkoping': return 'Norrkoping IFK'
    elif equipo_casa_input == 'Louisville City FC': return 'Louisville City FC'
    elif equipo_casa_input == 'Bolton': return 'Bolton'
    elif equipo_casa_input == 'Dundee Utd': return 'Dundee Utd'
    elif equipo_casa_input == 'MÃ¡laga': return 'Malaga'
    elif equipo_casa_input == 'Guangzhou Evergrande': return 'Guangzhou Evergrande'
    elif equipo_casa_input == 'HJK Helsinki': return 'Helsinki HJK'
    elif equipo_casa_input == 'Albacete': return 'Albacete'
    elif equipo_casa_input == 'Cashpoint SC Rheindorf Altach': return 'Cashpoint SC Rheindorf'
    elif equipo_casa_input == 'Odd BK': return 'Odd BK'
    elif equipo_casa_input == 'Grenoble': return 'Grenoble'
    elif equipo_casa_input == 'Eupen': return 'Eupen'
    elif equipo_casa_input == 'Ionikos FC': return 'Ionikos FC'
    elif equipo_casa_input == 'Milton Keynes Dons': return 'Milton Keynes Dons'
    elif equipo_casa_input == 'Wycombe Wanderers': return 'Wycombe Wanderers'
    elif equipo_casa_input == 'FC Vaduz': return 'Vaduz FC'
    elif equipo_casa_input == 'Lyngby': return 'Lyngby'
    elif equipo_casa_input == 'Kyoto Purple Sanga': return 'Kyoto Purple Sanga'
    elif equipo_casa_input == 'Asteras Tripolis': return 'Asteras Tripolis'
    elif equipo_casa_input == 'Como': return 'Como'
    elif equipo_casa_input == 'Istanbulspor': return 'Istanbulspor'
    elif equipo_casa_input == 'Panetolikos': return 'Panetolikos'
    elif equipo_casa_input == 'Hansa Rostock': return 'Hansa Rostock'
    elif equipo_casa_input == 'FC Andorra': return 'Andorra FC'
    elif equipo_casa_input == 'Avispa Fukuoka': return 'Avispa Fukuoka'
    elif equipo_casa_input == 'Shonan Bellmare': return 'Shonan Bellmare'
    elif equipo_casa_input == 'Racing Santander': return 'Racing Santander'
    elif equipo_casa_input == 'Plymouth Argyle': return 'Plymouth Argyle'
    elif equipo_casa_input == 'Lugo': return 'Lugo'
    elif equipo_casa_input == 'Modena': return 'Modena'
    elif equipo_casa_input == 'Torpedo Moskow': return 'Torpedo Moskow'
    elif equipo_casa_input == 'San Diego Loyal SC': return 'San Diego Loyal'
    elif equipo_casa_input == 'Aalesund': return 'Aalesund'
    elif equipo_casa_input == 'Sydney FC': return 'Sydney FC'
    elif equipo_casa_input == 'Oxford United': return 'Oxford United'
    elif equipo_casa_input == 'Annecy': return 'Annecy'
    elif equipo_casa_input == 'Hamarkamaratene': return 'Hamarkamaratene'
    elif equipo_casa_input == 'Pau': return 'Pau'
    elif equipo_casa_input == 'Aldosivi': return 'Aldosivi'
    elif equipo_casa_input == 'Palermo': return 'Palermo'
    elif equipo_casa_input == 'Laval': return 'Laval'
    elif equipo_casa_input == 'Melbourne Victory': return 'Melbourne Victory'
    elif equipo_casa_input == 'Beijing Guoan': return 'Beijing Guoan'
    elif equipo_casa_input == 'Kristiansund BK': return 'Kristiansund BK'
    elif equipo_casa_input == 'Gamba Osaka': return 'Gamba Osaka'
    elif equipo_casa_input == 'Giannina': return 'Giannina'
    elif equipo_casa_input == 'San Antonio FC': return 'San Antonio FC'
    elif equipo_casa_input == 'Birmingham Legion FC': return 'Birmingham Legion FC'
    elif equipo_casa_input == 'Niort': return 'Niort'
    elif equipo_casa_input == 'Mjallby': return 'Mjallby'
    elif equipo_casa_input == 'Jahn Regensburg': return 'Jahn Regensburg'
    elif equipo_casa_input == 'Cosenza': return 'Cosenza'
    elif equipo_casa_input == 'Shanghai SIPG': return 'Shanghai SIPG'
    elif equipo_casa_input == 'SV Sandhausen': return 'Sandhausen SV'
    elif equipo_casa_input == 'RFC Seraing': return 'Seraing RFC'
    elif equipo_casa_input == 'Charlton Athletic': return 'Charlton Athletic'
    elif equipo_casa_input == 'Rodez': return 'Rodez'
    elif equipo_casa_input == 'OFI Crete': return 'Crete OFI'
    elif equipo_casa_input == 'Sudtirol': return 'Sudtirol'
    elif equipo_casa_input == '1. FC Kaiserslautern': return 'Kaiserlautern FC 1.'
    elif equipo_casa_input == 'Salford City': return 'Salford City'
    elif equipo_casa_input == 'Orlando Pirates': return 'Orlando Pirates'
    elif equipo_casa_input == 'US Quevilly': return 'Quevilly US'
    elif equipo_casa_input == 'Sandefjord': return 'Sandefjord'
    elif equipo_casa_input == 'Levadiakos': return 'Levadiakos'
    elif equipo_casa_input == 'Rio Grande Valley FC Toros': return 'Rio Grande Valley'
    elif equipo_casa_input == 'Pittsburgh Riverhounds': return 'Pittsburgh Riverhounds'
    elif equipo_casa_input == 'Pyunik Yerevan': return 'Pyunik Yerevan'
    elif equipo_casa_input == 'Memphis 901 FC': return 'Memphis 901 FC'
    elif equipo_casa_input == 'Western Sydney FC': return 'Western Sydney FC'
    elif equipo_casa_input == 'Western United': return 'Western United'
    elif equipo_casa_input == 'Adelaide United': return 'Adelaide United'
    elif equipo_casa_input == 'IK Sirius': return 'Sirius IK'
    elif equipo_casa_input == 'Central Coast Mariners': return 'Central Coast Mariners'
    elif equipo_casa_input == 'Sacramento Republic FC': return 'Sacramento Republic FC'
    elif equipo_casa_input == 'Kaizer Chiefs': return 'Kaizer Chiefs'
    elif equipo_casa_input == 'SuperSport United': return 'SuperSport United'
    elif equipo_casa_input == 'Newcastle Jets': return 'Newcastle Jets'
    elif equipo_casa_input == 'Shrewsbury Town': return 'Shrewsbury Town'
    elif equipo_casa_input == 'Shamrock Rovers': return 'Shamrock Rovers'
    elif equipo_casa_input == 'Eintracht Braunschweig': return 'Eintracht Braunschweig'
    elif equipo_casa_input == 'Oakland Roots': return 'Oakland Roots'
    elif equipo_casa_input == 'Miami FC': return 'Miami FC'
    elif equipo_casa_input == 'New Mexico United': return 'New Mexico United'
    elif equipo_casa_input == 'Colorado Springs Switchbacks FC': return 'Colorado Springs Switchbacks'
    elif equipo_casa_input == '1. FC Magdeburg': return 'Magdeburg FC 1.'
    elif equipo_casa_input == 'IFK Värnamo': return 'Varnamo IFK'
    elif equipo_casa_input == 'Lincoln City': return 'Lincoln City'
    elif equipo_casa_input == 'Jubilo Iwata': return 'Jubilo Iwata'
    elif equipo_casa_input == 'Shandong Luneng': return 'Shandong Luneng'
    elif equipo_casa_input == 'Jiangsu Suning FC': return 'Jiangsu Suning FC'
    elif equipo_casa_input == 'Black Aces': return 'Black Aces'
    elif equipo_casa_input == 'Mansfield Town': return 'Mansfield Town'
    elif equipo_casa_input == 'Fleetwood Town': return 'Fleetwood Town'
    elif equipo_casa_input == 'Exeter City': return 'Exeter City'
    elif equipo_casa_input == 'Lamia': return 'Lamia'
    elif equipo_casa_input == 'Winterthur': return 'Winterthur'
    elif equipo_casa_input == 'Cambridge United': return 'Cambridge United'
    elif equipo_casa_input == 'Varbergs BoIS FC': return 'Varbergs BoIS FC'
    elif equipo_casa_input == 'Brisbane Roar': return 'Brisbane Roar'
    elif equipo_casa_input == 'El Paso Locomotive FC': return 'El Paso Locomotive'
    elif equipo_casa_input == 'Cheltenham Town': return 'Cheltenham Town'
    elif equipo_casa_input == 'Leyton Orient': return 'Leyton Orient'
    elif equipo_casa_input == 'Doncaster Rovers': return 'Doncaster Rovers'
    elif equipo_casa_input == 'Bristol Rovers': return 'Bristol Rovers'
    elif equipo_casa_input == 'Macarthur FC': return 'Macarthur FC'
    elif equipo_casa_input == 'Stellenbosch FC': return 'Stellenbosch FC'
    elif equipo_casa_input == 'Accrington Stanley': return 'Accrington Stanley'
    elif equipo_casa_input == 'Arizona United': return 'Arizona United'
    elif equipo_casa_input == 'Northampton Town': return 'Northampton Town'
    elif equipo_casa_input == 'Detroit City FC': return 'Detroit City FC'
    elif equipo_casa_input == 'Swindon Town': return 'Swindon Town'
    elif equipo_casa_input == 'Port Vale': return 'Port Vale'
    elif equipo_casa_input == 'Orange County SC': return 'Orange County SC'
    elif equipo_casa_input == 'AmaZulu': return 'AmaZulu'
    elif equipo_casa_input == 'Golden Arrows': return 'Golden Arrows'
    elif equipo_casa_input == 'Degerfors IF': return 'Degerfors IF'
    elif equipo_casa_input == 'Colchester United': return 'Colchester United'
    elif equipo_casa_input == 'Forest Green Rovers': return 'Forest Green Rovers'
    elif equipo_casa_input == 'Tulsa Roughnecks': return 'Tulsa Roughnecks'
    elif equipo_casa_input == 'Wellington Phoenix': return 'Wellington Phoenix'
    elif equipo_casa_input == 'FK Jerv': return 'Jerv FK'
    elif equipo_casa_input == 'Royal AM': return 'Royal AM'
    elif equipo_casa_input == 'Burton Albion': return 'Burton Albion'
    elif equipo_casa_input == 'LA Galaxy II': return 'Galaxy LA II'
    elif equipo_casa_input == 'Moroka Swallows': return 'Moroka Swallows'
    elif equipo_casa_input == 'Hartford Athletic': return 'Hartford Athletic'
    elif equipo_casa_input == 'Charleston Battery': return 'Charleston Battery'
    elif equipo_casa_input == 'Helsingborgs IF': return 'Helsingborgs IF'
    elif equipo_casa_input == 'Tianjin Teda': return 'Tianjin Teda'
    elif equipo_casa_input == 'Tranmere Rovers': return 'Tranmere Rovers'
    elif equipo_casa_input == 'Monterey Bay': return 'Monterey Bay'
    elif equipo_casa_input == 'Morecambe': return 'Morecambe'
    elif equipo_casa_input == 'Sekhukhune United': return 'Sekhukhune United'
    elif equipo_casa_input == 'Shanghai Greenland': return 'Shanghai Greenland'
    elif equipo_casa_input == 'Richards Bay': return 'Richards Bay'
    elif equipo_casa_input == 'Chippa United': return 'Chippa United'
    elif equipo_casa_input == 'Bradford City': return 'Bradford City'
    elif equipo_casa_input == 'Newport County': return 'Newport County'
    elif equipo_casa_input == 'Sutton United': return 'Sutton United'
    elif equipo_casa_input == 'TS Galaxy': return 'Galaxy TS'
    elif equipo_casa_input == 'Stevenage': return 'Stevenage'
    elif equipo_casa_input == 'Crewe Alexandra': return 'Crewe Alexandra'
    elif equipo_casa_input == 'Hebei China Fortune FC': return 'Hebei China Fortune'
    elif equipo_casa_input == 'Tshakhuma Tsha Madzivhandila': return 'Tshakhuma Tsha Madzivhandila'
    elif equipo_casa_input == 'Maritzburg Utd': return 'Maritzburg Utd'
    elif equipo_casa_input == 'Henan Jianye': return 'Henan Jianye'
    elif equipo_casa_input == 'AFC Wimbledon': return 'Wimbledon AFC'
    elif equipo_casa_input == 'Indy Eleven': return 'Indy Eleven'
    elif equipo_casa_input == 'Dalian Aerbin': return 'Dalian Aerbin'
    elif equipo_casa_input == 'Guangzhou RF': return 'Guangzhou RF'
    elif equipo_casa_input == 'Perth Glory': return 'Perth Glory'
    elif equipo_casa_input == 'Wuhan Zall': return 'Wuhan Zall'
    elif equipo_casa_input == 'Stockport County': return 'Stockport County'
    elif equipo_casa_input == 'GIF Sundsvall': return 'Sundsvall GIF'
    elif equipo_casa_input == 'Barrow': return 'Barrow'
    elif equipo_casa_input == 'Gillingham': return 'Gillingham'
    elif equipo_casa_input == 'Grimsby Town': return 'Grimsby Town'
    elif equipo_casa_input == 'Rochdale': return 'Rochdale'
    elif equipo_casa_input == 'Tianjin Quanujian': return 'Tianjin Quanujian'
    elif equipo_casa_input == 'Shenzhen FC': return 'Shenzhen FC'
    elif equipo_casa_input == 'Crawley Town': return 'Crawley Town'
    elif equipo_casa_input == 'Chongqing Lifan': return 'Chongqing Lifan'
    elif equipo_casa_input == 'Las Vegas Lights FC': return 'Vegas Las Lights'
    elif equipo_casa_input == 'Walsall': return 'Walsall'
    elif equipo_casa_input == 'Loudoun United FC': return 'Loudoun United FC'
    elif equipo_casa_input == 'Harrogate Town': return 'Harrogate Town'
    elif equipo_casa_input == 'Carlisle United': return 'Carlisle United'
    elif equipo_casa_input == 'Atlanta United 2': return 'Atlanta United 2'
    elif equipo_casa_input == 'Hartlepool': return 'Hartlepool'
    elif equipo_casa_input == 'Guizhou Renhe': return 'Guizhou Renhe'
    elif equipo_casa_input == 'New York Red Bulls II': return 'New York Red'
    else:
        return equipo_casa_input
    
def equipo_visita_input_():

    if equipo_visita_input == 'Afghanistan': return 'File:Flag_of_Afghanistan.svg'
    elif equipo_visita_input == 'Albania': return 'File:Flag_of_Albania.svg'
    elif equipo_visita_input == 'Algeria': return 'File:Flag_of_Algeria.svg'
    elif equipo_visita_input == 'Samoa': return 'File:Flag_of_American_Samoa.svg'
    elif equipo_visita_input == 'Andorra': return 'File:Flag_of_Andorra.svg'
    elif equipo_visita_input == 'Angola': return 'File:Flag_of_Angola.svg'
    elif equipo_visita_input == 'Anguilla': return 'File:Flag_of_Anguilla.svg'
    elif equipo_visita_input == 'Antigua and Barbuda': return 'File:Flag_of_Antigua_and_Barbuda.svg'
    elif equipo_visita_input == 'Argentina': return 'File:Flag_of_Argentina.svg'
    elif equipo_visita_input == 'Armenia': return 'File:Flag_of_Armenia.svg'
    elif equipo_visita_input == 'Aruba': return 'File:Flag_of_Aruba.svg'
    elif equipo_visita_input == 'Australia': return 'File:Flag_of_Australia.svg'
    elif equipo_visita_input == 'Austria': return 'File:Flag_of_Austria.svg'
    elif equipo_visita_input == 'Azerbaijan': return 'File:Flag_of_Azerbaijan.svg'
    elif equipo_visita_input == 'Bahamas': return 'File:Flag_of_Bahamas.svg'
    elif equipo_visita_input == 'Bahrain': return 'File:Flag_of_Bahrain.svg'
    elif equipo_visita_input == 'Bangladesh': return 'File:Flag_of_Bangladesh.svg'
    elif equipo_visita_input == 'Barbados': return 'File:Flag_of_Barbados.svg'
    elif equipo_visita_input == 'Basque Country': return 'File:Flag_of_the_Basque_Country.svg'
    elif equipo_visita_input == 'Belarus': return 'File:Flag_of_Belarus.svg'
    elif equipo_visita_input == 'Belgium': return 'File:Flag_of_Belgium.svg'
    elif equipo_visita_input == 'Belize': return 'File:Flag_of_Belize.svg'
    elif equipo_visita_input == 'Benin': return 'File:Flag_of_Benin.svg'
    elif equipo_visita_input == 'Bermuda': return 'File:Flag_of_Bermuda.svg'
    elif equipo_visita_input == 'Bhutan': return 'File:Flag_of_Bhutan.svg'
    elif equipo_visita_input == 'Bolivia': return 'File:Flag_of_Bolivia.svg'
    elif equipo_visita_input == 'Bonaire': return 'File:Flag_of_Bonaire.svg'
    elif equipo_visita_input == 'Bosnia and Herzegovina': return 'File:Flag_of_Bosnia_and_Herzegovina.svg'
    elif equipo_visita_input == 'Botswana': return 'File:Flag_of_Botswana.svg'
    elif equipo_visita_input == 'Brazil': return 'File:Flag_of_Brazil.svg'
    elif equipo_visita_input == 'British Virgin Islands': return 'File:Flag_of_British_Virgin_Islands.svg'
    elif equipo_visita_input == 'Brunei': return 'File:Flag_of_Brunei.svg'
    elif equipo_visita_input == 'Bulgaria': return 'File:Flag_of_Bulgaria.svg'
    elif equipo_visita_input == 'Burkina Faso': return 'File:Flag_of_Burkina_Faso.svg'
    elif equipo_visita_input == 'Burundi': return 'File:Flag_of_Burundi.svg'
    elif equipo_visita_input == 'Cambodia': return 'File:Flag_of_Cambodia.svg'
    elif equipo_visita_input == 'Cameroon': return 'File:Flag_of_Cameroon.svg'
    elif equipo_visita_input == 'Canada': return 'File:Flag_of_Canada.svg'
    elif equipo_visita_input == 'Cape Verde Islands': return 'File:Flag_of_Cape_Verde.svg'
    elif equipo_visita_input == 'Cayman Islands': return 'File:Flag_of_Cayman_Islands.svg'
    elif equipo_visita_input == 'Central African Republic': return 'File:Flag_of_Central_African_Republic.svg'
    elif equipo_visita_input == 'Chad': return 'File:Flag_of_Chad.svg'
    elif equipo_visita_input == 'Chile': return 'File:Flag_of_Chile.svg'
    elif equipo_visita_input == 'China PR': return "File:Flag_of_the_People's_Republic_of_China.svg"
    elif equipo_visita_input == 'Chinese Taipei': return 'File:Flag_of_the_Republic_of_China.svg'
    elif equipo_visita_input == 'Colombia': return 'File:Flag_of_Colombia.svg'
    elif equipo_visita_input == 'Comoros': return 'File:Flag_of_Comoros.svg'
    elif equipo_visita_input == 'Congo': return 'File:Flag_of_Congo.svg'
    elif equipo_visita_input == 'Congo DR': return 'File:Flag_of_the_Democratic_Republic_of_the_Congo.svg'
    elif equipo_visita_input == 'Cook Islands': return 'File:Flag_of_Cook_Islands.svg'
    elif equipo_visita_input == 'Costa Rica': return 'File:Flag_of_Costa_Rica.svg'
    elif equipo_visita_input == 'Croatia': return 'File:Flag_of_Croatia.svg'
    elif equipo_visita_input == 'Cuba': return 'File:Flag_of_Cuba.svg'
    elif equipo_visita_input == 'Curacao': return 'File:Flag_of_Curaçao.svg'
    elif equipo_visita_input == 'Cyprus': return 'File:Flag_of_Cyprus.svg'
    elif equipo_visita_input == 'Czech Republic': return 'File:Flag_of_Czech_Republic.svg'
    elif equipo_visita_input == 'Denmark': return 'File:Flag_of_Denmark.svg'
    elif equipo_visita_input == 'Djibouti': return 'File:Flag_of_Djibouti.svg'
    elif equipo_visita_input == 'Dominica': return 'File:Flag_of_Dominica.svg'
    elif equipo_visita_input == 'Dominican Republic': return 'File:Flag_of_Dominican_Republic.svg'
    elif equipo_visita_input == 'Ecuador': return 'File:Flag_of_Ecuador.svg'
    elif equipo_visita_input == 'Egypt': return 'File:Flag_of_Egypt.svg'
    elif equipo_visita_input == 'El Salvador': return 'File:Flag_of_El_Salvador.svg'
    elif equipo_visita_input == 'England': return 'File:Flag_of_England.svg'
    elif equipo_visita_input == 'Equatorial Guinea': return 'File:Flag_of_Equatorial_Guinea.svg'
    elif equipo_visita_input == 'Eritrea': return 'File:Flag_of_Eritrea.svg'
    elif equipo_visita_input == 'Estonia': return 'File:Flag_of_Estonia.svg'
    elif equipo_visita_input == 'Ethiopia': return 'File:Flag_of_Ethiopia.svg'
    elif equipo_visita_input == 'Faroe Islands': return 'File:Flag_of_Faroe_Islands.svg'
    elif equipo_visita_input == 'Fiji': return 'File:Flag_of_Fiji.svg'
    elif equipo_visita_input == 'Finland': return 'File:Flag_of_Finland.svg'
    elif equipo_visita_input == 'France': return 'File:Flag_of_France.svg'
    elif equipo_visita_input == 'French Guiana': return 'File:Flag_of_French_Guiana.svg'
    elif equipo_visita_input == 'Gabon': return 'File:Flag_of_Gabon.svg'
    elif equipo_visita_input == 'Gambia': return 'File:Flag_of_Gambia.svg'
    elif equipo_visita_input == 'Georgia': return 'File:Flag_of_Georgia.svg'
    elif equipo_visita_input == 'Germany': return 'File:Flag_of_Germany.svg'
    elif equipo_visita_input == 'Ghana': return 'File:Flag_of_Ghana.svg'
    elif equipo_visita_input == 'Gibraltar': return 'File:Flag_of_Gibraltar.svg'
    elif equipo_visita_input == 'Greece': return 'File:Flag_of_Greece.svg'
    elif equipo_visita_input == 'Grenada': return 'File:Flag_of_Grenada.svg'
    elif equipo_visita_input == 'Guadeloupe': return 'File:Flag_of_Guadeloupe_(local)_variant.svg'
    elif equipo_visita_input == 'Guam': return 'File:Flag_of_Guam.svg'
    elif equipo_visita_input == 'Guatemala': return 'File:Flag_of_Guatemala.svg'
    elif equipo_visita_input == 'Guinea': return 'File:Flag_of_Guinea.svg'
    elif equipo_visita_input == 'Guinea-Bissau': return 'File:Flag_of_Guinea-Bissau.svg'
    elif equipo_visita_input == 'Guyana': return 'File:Flag_of_Guyana.svg'
    elif equipo_visita_input == 'Haiti': return 'File:Flag_of_Haiti.svg'
    elif equipo_visita_input == 'Honduras': return 'File:Flag_of_Honduras.svg'
    elif equipo_visita_input == 'Hong Kong': return 'File:Flag_of_Hong_Kong.svg'
    elif equipo_visita_input == 'Hungary': return 'File:Flag_of_Hungary.svg'
    elif equipo_visita_input == 'Iceland': return 'File:Flag_of_Iceland.svg'
    elif equipo_visita_input == 'India': return 'File:Flag_of_India.svg'
    elif equipo_visita_input == 'Indonesia': return 'File:Flag_of_Indonesia.svg'
    elif equipo_visita_input == 'Iran': return 'File:Flag_of_Iran.svg'
    elif equipo_visita_input == 'Iraq': return 'File:Flag_of_Iraq.svg'
    elif equipo_visita_input == 'Israel': return 'File:Flag_of_Israel.svg'
    elif equipo_visita_input == 'Italy': return 'File:Flag_of_Italy.svg'
    elif equipo_visita_input == 'Ivory Coast': return 'File:Flag_of_Ivory_Coast.svg'
    elif equipo_visita_input == 'Jamaica': return 'File:Flag_of_Jamaica.svg'
    elif equipo_visita_input == 'Japan': return 'File:Flag_of_Japan.svg'
    elif equipo_visita_input == 'Jordan': return 'File:Flag_of_Jordan.svg'
    elif equipo_visita_input == 'Kazakhstan': return 'File:Flag_of_Kazakhstan.svg'
    elif equipo_visita_input == 'Kenya': return 'File:Flag_of_Kenya.svg'
    elif equipo_visita_input == 'Kosovo': return 'File:Flag_of_Kosovo.svg'
    elif equipo_visita_input == 'Kuwait': return 'File:Flag_of_Kuwait.svg'
    elif equipo_visita_input == 'Kyrgyzstan': return 'File:Flag_of_Kyrgyzstan.svg'
    elif equipo_visita_input == 'Laos': return 'File:Flag_of_Laos.svg'
    elif equipo_visita_input == 'Latvia': return 'File:Flag_of_Latvia.svg'
    elif equipo_visita_input == 'Lebanon': return 'File:Flag_of_Lebanon.svg'
    elif equipo_visita_input == 'Lesotho': return 'File:Flag_of_Lesotho.svg'
    elif equipo_visita_input == 'Liberia': return 'File:Flag_of_Liberia.svg'
    elif equipo_visita_input == 'Libya': return 'File:Flag_of_Libya.svg'
    elif equipo_visita_input == 'Liechtenstein': return 'File:Flag_of_Liechtenstein.svg'
    elif equipo_visita_input == 'Lithuania': return 'File:Flag_of_Lithuania.svg'
    elif equipo_visita_input == 'Luxembourg': return 'File:Flag_of_Luxembourg.svg'
    elif equipo_visita_input == 'Macau': return 'File:Flag_of_Macau.svg'
    elif equipo_visita_input == 'Madagascar': return 'File:Flag_of_Madagascar.svg'
    elif equipo_visita_input == 'Malawi': return 'File:Flag_of_Malawi.svg'
    elif equipo_visita_input == 'Malaysia': return 'File:Flag_of_Malaysia.svg'
    elif equipo_visita_input == 'Maldives': return 'File:Flag_of_Maldives.svg'
    elif equipo_visita_input == 'Mali': return 'File:Flag_of_Mali.svg'
    elif equipo_visita_input == 'Malta': return 'File:Flag_of_Malta.svg'
    elif equipo_visita_input == 'Martinique': return 'File:Flag_of_Martinique.svg'
    elif equipo_visita_input == 'Mauritania': return 'File:Flag_of_Mauritania.svg'
    elif equipo_visita_input == 'Mauritius': return 'File:Flag_of_Mauritius.svg'
    elif equipo_visita_input == 'Mexico': return 'File:Flag_of_Mexico.svg'
    elif equipo_visita_input == 'Moldova': return 'File:Flag_of_Moldova.svg'
    elif equipo_visita_input == 'Mongolia': return 'File:Flag_of_Mongolia.svg'
    elif equipo_visita_input == 'Montenegro': return 'File:Flag_of_Montenegro.svg'
    elif equipo_visita_input == 'Montserrat': return 'File:Flag_of_Montserrat.svg'
    elif equipo_visita_input == 'Morocco': return 'File:Flag_of_Morocco.svg'
    elif equipo_visita_input == 'Mozambique': return 'File:Flag_of_Mozambique.svg'
    elif equipo_visita_input == 'Myanmar': return 'File:Flag_of_Myanmar.svg'
    elif equipo_visita_input == 'Namibia': return 'File:Flag_of_Namibia.svg'
    elif equipo_visita_input == 'Nepal': return 'File:Flag_of_Nepal.svg'
    elif equipo_visita_input == 'Netherlands': return 'File:Flag_of_Netherlands.svg'
    elif equipo_visita_input == 'New Caledonia': return 'File:Flag_of_New_Caledonia.svg'
    elif equipo_visita_input == 'New Zealand': return 'File:Flag_of_New_Zealand.svg'
    elif equipo_visita_input == 'Nicaragua': return 'File:Flag_of_Nicaragua.svg'
    elif equipo_visita_input == 'Niger': return 'File:Flag_of_Niger.svg'
    elif equipo_visita_input == 'Nigeria': return 'File:Flag_of_Nigeria.svg'
    elif equipo_visita_input == 'North Korea': return 'File:Flag_of_North_Korea.svg'
    elif equipo_visita_input == 'North Macedonia': return 'File:Flag_of_North_Macedonia.svg'
    elif equipo_visita_input == 'Northern Ireland': return 'File:Flag_of_Northern_Ireland.svg'
    elif equipo_visita_input == 'Northern Mariana Islands': return 'File:Flag_of_Northern_Mariana_Islands.svg'
    elif equipo_visita_input == 'Norway': return 'File:Flag_of_Norway.svg'
    elif equipo_visita_input == 'Oman': return 'File:Flag_of_Oman.svg'
    elif equipo_visita_input == 'Pakistan': return 'File:Flag_of_Pakistan.svg'
    elif equipo_visita_input == 'Palestine': return 'File:Flag_of_Palestine.svg'
    elif equipo_visita_input == 'Panama': return 'File:Flag_of_Panama.svg'
    elif equipo_visita_input == 'Papua New Guinea': return 'File:Flag_of_Papua_New_Guinea.svg'
    elif equipo_visita_input == 'Paraguay': return 'File:Flag_of_Paraguay.svg'
    elif equipo_visita_input == 'Peru': return 'File:Flag_of_Peru.svg'
    elif equipo_visita_input == 'Philippines': return 'File:Flag_of_Philippines.svg'
    elif equipo_visita_input == 'Poland': return 'File:Flag_of_Poland.svg'
    elif equipo_visita_input == 'Portugal': return 'File:Flag_of_Portugal.svg'
    elif equipo_visita_input == 'Puerto Rico': return 'File:Flag_of_Puerto_Rico.svg'
    elif equipo_visita_input == 'Qatar': return 'File:Flag_of_Qatar.svg'
    elif equipo_visita_input == 'Rep of Ireland': return 'File:Flag_of_Ireland.svg'
    elif equipo_visita_input == 'Romania': return 'File:Flag_of_Romania.svg'
    elif equipo_visita_input == 'Russia': return 'File:Flag_of_Russia.svg'
    elif equipo_visita_input == 'Rwanda': return 'File:Flag_of_Rwanda.svg'
    elif equipo_visita_input == 'San Marino': return 'File:Flag_of_San_Marino.svg'
    elif equipo_visita_input == 'Sao Tome and Principe': return 'File:Flag_of_Sao_Tome_and_Principe.svg'
    elif equipo_visita_input == 'Saudi Arabia': return 'File:Flag_of_Saudi_Arabia.svg'
    elif equipo_visita_input == 'Scotland': return 'File:Flag_of_Scotland.svg'
    elif equipo_visita_input == 'Senegal': return 'File:Flag_of_Senegal.svg'
    elif equipo_visita_input == 'Serbia': return 'File:Flag_of_Serbia.svg'
    elif equipo_visita_input == 'Seychelles': return 'File:Flag_of_Seychelles.svg'
    elif equipo_visita_input == 'Sierra Leone': return 'File:Flag_of_Sierra_Leone.svg'
    elif equipo_visita_input == 'Singapore': return 'File:Flag_of_Singapore.svg'
    elif equipo_visita_input == 'Sint Maarten': return 'File:Flag_of_Sint_Maarten.svg'
    elif equipo_visita_input == 'Slovakia': return 'File:Flag_of_Slovakia.svg'
    elif equipo_visita_input == 'Slovenia': return 'File:Flag_of_Slovenia.svg'
    elif equipo_visita_input == 'Solomon Islands': return 'File:Flag_of_Solomon_Islands.svg'
    elif equipo_visita_input == 'Somalia': return 'File:Flag_of_Somalia.svg'
    elif equipo_visita_input == 'South Africa': return 'File:Flag_of_South_Africa.svg'
    elif equipo_visita_input == 'South Korea': return 'File:Flag_of_South_Korea.svg'
    elif equipo_visita_input == 'South Sudan': return 'File:Flag_of_South_Sudan.svg'
    elif equipo_visita_input == 'Spain': return 'File:Flag_of_Spain.svg'
    elif equipo_visita_input == 'Sri Lanka': return 'File:Flag_of_Sri_Lanka.svg'
    elif equipo_visita_input == 'St. Kitts and Nevis': return 'File:Flag_of_Saint_Kitts_and_Nevis.svg'
    elif equipo_visita_input == 'St. Lucia': return 'File:Flag_of_Saint_Lucia.svg'
    elif equipo_visita_input == 'St. Martin': return 'File:Saint-Martin_Flag.svg'
    elif equipo_visita_input == 'St. Vincent and the Grenadines': return 'File:Flag_of_Saint_Vincent_and_the_Grenadines.svg'
    elif equipo_visita_input == 'Sudan': return 'File:Flag_of_Sudan.svg'
    elif equipo_visita_input == 'Suriname': return 'File:Flag_of_Suriname.svg'
    elif equipo_visita_input == 'Swaziland': return 'File:Flag_of_Eswatini.svg'
    elif equipo_visita_input == 'Sweden': return 'File:Flag_of_Sweden.svg'
    elif equipo_visita_input == 'Switzerland': return 'File:Flag_of_Switzerland.svg'
    elif equipo_visita_input == 'Syria': return 'File:Flag_of_Syria.svg'
    elif equipo_visita_input == 'Tahiti': return 'File:Flag_of_Tahiti.svg'
    elif equipo_visita_input == 'Tajikistan': return 'File:Flag_of_Tajikistan.svg'
    elif equipo_visita_input == 'Tanzania': return 'File:Flag_of_Tanzania.svg'
    elif equipo_visita_input == 'Thailand': return 'File:Flag_of_Thailand.svg'
    elif equipo_visita_input == 'Timor-Leste': return 'File:Flag_of_East_Timor.svg'
    elif equipo_visita_input == 'Togo': return 'File:Flag_of_Togo.svg'
    elif equipo_visita_input == 'Tonga': return 'File:Flag_of_Tonga.svg'
    elif equipo_visita_input == 'Trinidad and Tobago': return 'File:Flag_of_Trinidad_and_Tobago.svg'
    elif equipo_visita_input == 'Tunisia': return 'File:Flag_of_Tunisia.svg'
    elif equipo_visita_input == 'Turkey': return 'File:Flag_of_Turkey.svg'
    elif equipo_visita_input == 'Turkmenistan': return 'File:Flag_of_Turkmenistan.svg'
    elif equipo_visita_input == 'Turks and Caicos Islands': return 'File:Flag_of_Turks_and_Caicos_Islands.svg'
    elif equipo_visita_input == 'Tuvalu': return 'File:Flag_of_Tuvalu.svg'
    elif equipo_visita_input == 'Uganda': return 'File:Flag_of_Uganda.svg'
    elif equipo_visita_input == 'Ukraine': return 'File:Flag_of_Ukraine.svg'
    elif equipo_visita_input == 'United Arab Emirates': return 'File:Flag_of_United_Arab_Emirates.svg'
    elif equipo_visita_input == 'Uruguay': return 'File:Flag_of_Uruguay.svg'
    elif equipo_visita_input == 'US Virgin Islands': return 'File:Flag_of_the_United_States_Virgin_Islands.svg'
    elif equipo_visita_input == 'USA': return 'File:Flag_of_the_United_States.svg'
    elif equipo_visita_input == 'Uzbekistan': return 'File:Flag_of_Uzbekistan.svg'
    elif equipo_visita_input == 'Vanuatu': return 'File:Flag_of_Vanuatu.svg'
    elif equipo_visita_input == 'Venezuela': return 'File:Flag_of_Venezuela.svg'
    elif equipo_visita_input == 'Vietnam': return 'File:Flag_of_Vietnam.svg'
    elif equipo_visita_input == 'Wales': return 'File:Flag_of_Wales.svg'
    elif equipo_visita_input == 'Yemen': return 'File:Flag_of_Yemen.svg'
    elif equipo_visita_input == 'Zambia': return 'File:Flag_of_Zambia.svg'
    elif equipo_visita_input == 'Zanzibar': return 'File:Flag_of_Zanzibar.svg'
    elif equipo_visita_input == 'Zimbabwe': return 'File:Flag_of_Zimbabwe.svg'
    else:
        return equipo_visita_input

def club_logo_home():
    try:
        from wikipedia import search
    except ImportError:
        print('No module named google found')

    query =  wikipedia.search(str(equipo_casa_input)+" "+str("football club"))

    print(query)

    var_a_ = []

    for i in query:
        j=i.replace(" ","_")
        var_a_.append(j)
    print(str(var_a_))

    var_a = []

    for b in var_a_:
        a="https://en.wikipedia.org/wiki/"+str(b)
        j=urllib.parse.quote(a,safe=':/.%')
        var_a.append(j)
    print (var_a)

    var_a_unquote = []

    for b in var_a_:
        a="https://en.wikipedia.org/wiki/"+str(b)
        var_a_unquote.append(a)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen
    import unidecode

    my_string_=str(equipo_casa_input)
    first_word_coded = ''
    for character in my_string_:
        if character != '/' and character !=' ' and character !='-':
            first_word_coded = first_word_coded + character
        else:
            break

    first_word_=unidecode.unidecode(first_word_coded)

    var_a_unidecoded = []

    for i in var_a_unquote:
        j=unidecode.unidecode(i)
        var_a_unidecoded.append(j)

    if len(var_a)==0:
        html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")
    else:
        try:
            index_a = [idx for idx, s in enumerate(var_a_unidecoded) if str(first_word_) in s][0]
            try:
                html_page = urlopen(str(var_a[index_a]))
            except OSError as e:
                html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")
        except IndexError:
            html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")

    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    logo_list: List[Any] = [k for k in images if "https" and "logo" or "badge" or "crest" or "FC" or "CF" or "CD" in k]

    unquoted_logo_list=[]

    for i in logo_list:
        j=urllib.parse.unquote(i)
        unquoted_logo_list.append(j)

    unaccented_logo_list=[]

    for i in unquoted_logo_list:
        j=unidecode.unidecode(i)
        unaccented_logo_list.append(j)

    my_string=str(equipo_casa_input)
    first_word = ''
    for character in my_string:
        if character != '/' and character !=' ' and character !='-':
            first_word = first_word + character
        else:
            break

    unaccented_first_word = unidecode.unidecode(first_word)

    try:
        index = [idx for idx, s in enumerate(unaccented_logo_list) if str(unaccented_first_word) in s][0]
        logo_ht=logo_list[index]
        return logo_ht
    except IndexError:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

def country_flag_home():

    var_b_="https://commons.wikimedia.org/wiki/"+str(equipo_casa_input_())

    var_b=urllib.parse.quote(var_b_,safe=':/.%')

    try:
        html_page = urlopen(str(var_b))
    except OSError as e:
        html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")


    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    flag_list: List[Any] = [k for k in images if "Flag_of_" in k]

    import unidecode

    unaccented_flag_list=[]

    for i in flag_list:
        j=unidecode.unidecode(i)
        unaccented_flag_list.append(j)

    my_string=str(equipo_casa_input_())
    first_word=my_string.partition("File:")[2]

    unaccented_first_word = unidecode.unidecode(first_word)

    try:
        index = [idx for idx, s in enumerate(unaccented_flag_list) if str(unaccented_first_word) in s][0]
        flag_ht=flag_list[index]
        return flag_ht
    except IndexError:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

def print_team_logo_home():
    if spi_global_rankings['name'].str.contains(str(equipo_casa_input)).any():
        return club_logo_home()
    elif spi_global_rankings_intl['name'].str.contains(str(equipo_casa_input)).any():
        return country_flag_home()


def club_logo_road():
    try:
        from wikipedia import search
    except ImportError:
        print('No module named google found')

    query =  wikipedia.search(str(equipo_visita_input)+" "+str("football club"))

    print(query)

    var_c_ = []

    for i in query:
        j=i.replace(" ","_")
        var_c_.append(j)
    print(str(var_c_))

    var_c = []

    for b in var_c_:
        a="https://en.wikipedia.org/wiki/"+str(b)
        j=urllib.parse.quote(a,safe=':/.%')
        var_c.append(j)
    print (var_c)

    var_c_unquote = []

    for b in var_c_:
        a="https://en.wikipedia.org/wiki/"+str(b)
        var_c_unquote.append(a)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen
    import unidecode

    my_string_=str(equipo_visita_input)
    first_word_coded = ''
    for character in my_string_:
        if character != '/' and character !=' ' and character !='-':
            first_word_coded = first_word_coded + character
        else:
            break

    first_word_=unidecode.unidecode(first_word_coded)

    var_c_unidecoded = []

    for i in var_c_unquote:
        j=unidecode.unidecode(i)
        var_c_unidecoded.append(j)

    if len(var_c)==0:
        html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")
    else:
        try:
            index_c = [idx for idx, s in enumerate(var_c_unidecoded) if str(first_word_) in s][0]
            try:
                html_page = urlopen(str(var_c[index_c]))
            except OSError as e:
                html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")
        except IndexError:
            html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")

    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    logo_list: List[Any] = [k for k in images if "https" and "logo" or "badge" or "crest" or "FC" or "CF" or "CD" in k]

    unquoted_logo_list=[]

    for i in logo_list:
        j=urllib.parse.unquote(i)
        unquoted_logo_list.append(j)

    unaccented_logo_list=[]

    for i in unquoted_logo_list:
        j=unidecode.unidecode(i)
        unaccented_logo_list.append(j)

    my_string=str(equipo_visita_input)
    first_word = ''
    for character in my_string:
        if character != '/' and character !=' ' and character !='-':
            first_word = first_word + character
        else:
            break

    unaccented_first_word = unidecode.unidecode(first_word)

    try:
        index = [idx for idx, s in enumerate(unaccented_logo_list) if str(unaccented_first_word) in s][0]
        logo_rt=logo_list[index]
        return logo_rt
    except IndexError:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

def country_flag_road():
 
    var_d_="https://commons.wikimedia.org/wiki/"+str(equipo_visita_input_())

    var_d=urllib.parse.quote(var_d_,safe=':/.%')

    try:
        html_page = urlopen(str(var_d))
    except OSError as e:
        html_page = urlopen("https://commons.wikimedia.org/wiki/File:No_image_available.svg")

    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    flag_list: List[Any] = [k for k in images if "Flag_of_" in k]

    import unidecode

    unaccented_flag_list=[]

    for i in flag_list:
        j=unidecode.unidecode(i)
        unaccented_flag_list.append(j)

    my_string=str(equipo_visita_input_())
    first_word=my_string.partition("File:")[2]

    unaccented_first_word = unidecode.unidecode(first_word)

    try:
        index = [idx for idx, s in enumerate(unaccented_flag_list) if str(unaccented_first_word) in s][0]
        flag_rt=flag_list[index]
        return flag_rt
    except IndexError:
        return "https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

def print_team_logo_road():
    if spi_global_rankings['name'].str.contains(str(equipo_visita_input)).any():
        return club_logo_road()
    elif spi_global_rankings_intl['name'].str.contains(str(equipo_visita_input)).any():
        return country_flag_road()

enlace = "http"
team_logo_home = print_team_logo_home()
team_logo_road = print_team_logo_road()

def logo_home():
    if "http" not in str(team_logo_home):
        return "https:"+print_team_logo_home()
    else:
        return print_team_logo_home()

def logo_road():
    if "http" not in str(team_logo_road):
        return "https:"+print_team_logo_road()
    else:
        return print_team_logo_road()

try:
    col1, mid1, col2, mid2, col3, mid3, col4 = st.columns([1,1,5,5,1,1,5])
    with col1:
        try:
            st.image(logo_home(), width=60)
        except OSError as e:
            st.image("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",width=60)
    with col2:
        st.write(equipo_casa_input)
    with mid2:
        st.markdown("contra")
    with col3:
        try:
            st.image(logo_road(), width=60)
        except OSError as e:
            st.image("https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg",width=60)
    with col4:
        st.markdown(equipo_visita_input)
except TypeError:
    st.markdown("Por favor seleccioná equipos")

st.write("Simulación de partido")

latest_iteration3 = st.empty()
bar3= st.progress(0)

for i in range(100):
    latest_iteration3.markdown(f'Calculando goles esperados por equipo. Porcentaje completado {i+1}')
    bar3.progress(i+1)
    time.sleep(0.1)

try:
    index_casa_equipo = df_pf.index[df_pf['name'] == equipo_casa_input]
    index_visita_equipo = df_pf.index[df_pf['name'] == equipo_visita_input]

    equipo_casa_of = df_pf.at[index_casa_equipo[0], 'off']
    equipo_casa_def = df_pf.at[index_casa_equipo[0], 'defe']

    equipo_visita_of = df_pf.at[index_visita_equipo[0], 'off']
    equipo_visita_def = df_pf.at[index_visita_equipo[0], 'defe']

    goles_esperados_equipo_casa = ((equipo_casa_of) + (equipo_visita_def)) / 2
    goles_esperados_equipo_visita = ((equipo_visita_of) + (equipo_casa_def)) / 2

    goles_esperados_equipo_casa_redondeado = round(goles_esperados_equipo_casa,2)

    goles_esperados_equipo_visita_redondeado = round(goles_esperados_equipo_visita,2)

except IndexError:
    goles_esperados_equipo_casa_redondeado = 1
    goles_esperados_equipo_visita_redondeado= 1
    goles_esperados_equipo_casa=1
    goles_esperados_equipo_visita=1

col5, mid4, col6, mid5, col7, mid5, col8 = st.columns([1,1,5,5,1,1,5])

with col6:
    st.write('Goles esperados en el partido')

with col8:
    st.write('Goles esperados en el partido')

col9, mid6, col10, mid7, col11, mid5, col12 = st.columns([1,1,5,5,1,1,5])

with col10:
    st.write(goles_esperados_equipo_casa_redondeado)

with col12:
    st.write(goles_esperados_equipo_visita_redondeado)

latest_iteration4 = st.empty()
bar4 = st.progress(0)

for i in range(100):
    latest_iteration4.markdown(f'Simulando 10 000 partidos entre los equipos. Porcentaje completado {i+1}')
    bar4.progress(i+1)
    time.sleep(0.1)

probabilidad_casa = [random.random()]

for x in range(0, 9999):
    probabilidad_casa.append(random.random())

probabilidad_visita = [random.random()]

for x in range(0, 9999):
    probabilidad_visita.append(random.random())

random_marcadores_equipo_casa = poisson.ppf(probabilidad_casa, goles_esperados_equipo_casa)
random_marcadores_equipo_visita = poisson.ppf(probabilidad_visita, goles_esperados_equipo_visita)
random_marcadores_partido = [str(x[0])+" - " + str(x[1]) for x in zip(random_marcadores_equipo_casa, random_marcadores_equipo_visita)]

results = list()

for i, j in zip(random_marcadores_equipo_casa, random_marcadores_equipo_visita):
    if i > j:
        results.append("equipo de casa gana")
    elif i < j:
        results.append("equipo de visita gana")
    else:
        results.append("empate")

resultados_posibles_equipo_casa = list(range(0, 11))
resultados_posibles_equipo_visita = list(range(0, 11))

probabilidad_marcadores_final_casa = [((random_marcadores_equipo_casa == 0).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 1).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 2).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 3).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 4).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 5).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 6).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 7).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 8).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 9).sum()) / 10000,
                                      ((random_marcadores_equipo_casa == 10).sum()) / 10000]

probabilidad_marcadores_final_visita = [((random_marcadores_equipo_visita == 0).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 1).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 2).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 3).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 4).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 5).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 6).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 7).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 8).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 9).sum()) / 10000,
                                        ((random_marcadores_equipo_visita == 10).sum()) / 10000]

probabilidad_marcadores_final_partido = [a * b for a, b in zip(probabilidad_casa, probabilidad_visita)]

equipo_casa_gana = equipo_casa_input + " gana un " + str(round(((results.count("equipo de casa gana") / 10000) * 100),2)) + " % de las 10 000 simulaciones del partido"
equipo_visita_gana= equipo_visita_input + " gana un " + str(round(((results.count("equipo de visita gana") / 10000) * 100),2)) + " % de las 10 000 simulaciones del partido"
empate = "El partido termina como un empate el " + str(round(((results.count("empate") / 10000) * 100),2)) + " % de las simulaciones del partido"

datalinea_casa = pd.DataFrame({'Equipo':[equipo_casa_input, equipo_casa_input, equipo_casa_input, equipo_casa_input, equipo_casa_input,
                                         equipo_casa_input, equipo_casa_input, equipo_casa_input, equipo_casa_input, equipo_casa_input, equipo_casa_input],
                               'Probabilidad de marcadores': probabilidad_marcadores_final_casa, 'Resultados posibles': resultados_posibles_equipo_casa},
                              index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
datalinea_visita = pd.DataFrame({'Equipo':[equipo_visita_input, equipo_visita_input, equipo_visita_input, equipo_visita_input,equipo_visita_input, equipo_visita_input,
                                           equipo_visita_input, equipo_visita_input,equipo_visita_input, equipo_visita_input, equipo_visita_input],
                                 'Probabilidad de marcadores': probabilidad_marcadores_final_visita, 'Resultados posibles': resultados_posibles_equipo_visita},
                                index=[12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])

marco = [datalinea_casa, datalinea_visita]

datalinea_partido = pd.concat(marco)

datalinea_partido_grafico= alt.Chart(datalinea_partido).mark_line().encode(
    x='Resultados posibles',
    y='Probabilidad de marcadores',
    color=alt.Color('Equipo',
                    scale=alt.Scale(
                        domain=[equipo_casa_input,equipo_visita_input],
                        range=['red',
                               'blue'])
                    )
).properties(
)

latest_iteration5 = st.empty()
bar5 = st.progress(0)

for i in range(100):
    latest_iteration5.markdown(f'Resumiendo resultados de simulaciones gráficamente. Porcentaje completado {i+1}')
    bar5.progress(i+1)
    time.sleep(0.1)

st.altair_chart(datalinea_partido_grafico)

etiquetas = equipo_casa_input + ' gana', equipo_visita_input + ' gana', 'Empate'
proporciones = [results.count("equipo de casa gana"), results.count("equipo de visita gana"), results.count("empate")]
colores = ['green', 'red', 'gold']

st.markdown(equipo_casa_gana)
st.markdown(equipo_visita_gana)
st.markdown(empate)

fig1, ax1 = plt.subplots()
ax1.pie(proporciones, labels=etiquetas, colors=colores, autopct='%1.1f%%',
        shadow=True, startangle=140)
ax1.axis('equal')

st.pyplot(fig1)

lista_marcadores_casa = [0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         0.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         1.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         2.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         3.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         4.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         5.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         6.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         7.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         8.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         9.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0,
                         10.0]

lista_marcadores_visita = [0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0,
                           0.0,
                           1.0,
                           2.0,
                           3.0,
                           4.0,
                           5.0,
                           6.0,
                           7.0,
                           8.0,
                           9.0,
                           10.0]

# Create list of bins.

marcadores_posibles_partido = [str(x[0])+" - " + str(x[1]) for x in zip(lista_marcadores_casa, lista_marcadores_visita)]

# Construct array of frequency of possible scores.

frecuencia_de_marcadores_posibles = list()

for i in marcadores_posibles_partido:
    result = random_marcadores_partido.count(i)
    frecuencia_de_marcadores_posibles.append(result)

# Create bar chart to visualize score frequencies in the 10 000 simulations.

plt.style.use('ggplot')

objects = marcadores_posibles_partido
y_pos = np.arange(len(objects))
desempeño = frecuencia_de_marcadores_posibles

fig2, ax2 = plt.subplots()
ax2.bar(y_pos, frecuencia_de_marcadores_posibles, align='center', alpha=0.5)
plt.xticks(y_pos, marcadores_posibles_partido, fontsize= 3, rotation='vertical')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de marcadores posibles ' + equipo_casa_input + ' contra ' + equipo_visita_input)

st.pyplot(fig2)

# Define forecast algorithm in a function.
# Forecast as a winner the team that has more victories and more than 40 % of the victories in the simulations.

latest_iteration6 = st.empty()
bar6 = st.progress(0)

for i in range(100):
    latest_iteration6.markdown(f'Evaluando los resultados con algoritmo, para pronosticar. Porcentaje completado {i+1}')
    bar6.progress(i+1)
    time.sleep(0.1)

from scipy.stats import chi2

expected = [3333,3334,3333]

simulated=[results.count("equipo de casa gana"),results.count("empate"),results.count("equipo de visita gana")]

x = sum([(o-e)**2./e for o,e in zip(simulated,expected)])

import scipy

alpha = 0.5

df = 2

cr=chi2.ppf(q=1-alpha,df=df)

def forecast():
    if x>cr:
        if ((results.count("equipo de casa gana")) / 10000) > ((results.count("equipo de visita gana")) / 10000)+0.02 and ((results.count("equipo de casa gana")) / 10000) > ((results.count("empate"))/10000): return(str(equipo_casa_input) + " gana:")
        elif ((results.count("equipo de visita gana")) / 10000) > ((results.count("equipo de casa gana")) / 10000)+0.02 and ((results.count("equipo de visita gana")) / 10000) > ((results.count("empate"))/10000): return(str(equipo_visita_input) + " gana:")
        else: return("el partido termina en un empate:")
    else:
        return("el partido termina en un empate:")

Results = results
Scores = random_marcadores_partido

forecast_scores_dataframe=pd.DataFrame(
    {'Results': Results,
     'Scores': Scores})


scores_home_team_wins = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "equipo de casa gana"]
scores_road_team_wins = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "equipo de visita gana"]
scores_tie = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "empate"]

idxmax_score_home_team_wins = scores_home_team_wins['Scores'].value_counts().sort_index().idxmax()
idxmax_score_road_team_wins = scores_road_team_wins['Scores'].value_counts().sort_index().idxmax()
idxmax_score_tie = scores_tie['Scores'].value_counts().sort_index().idxmax()

def score_forecast():
    if x>cr:
        if ((results.count("equipo de casa gana")) / 10000) > ((results.count("equipo de visita gana")) / 10000)+0.02 and (
                (results.count("equipo de casa gana")) / 10000) > ((results.count("empate"))/10000):
            return(idxmax_score_home_team_wins)
        elif ((results.count("equipo de visita gana")) / 10000) > ((results.count("equipo de casa gana")) / 10000)+0.02 and (
                (results.count("equipo de visita gana")) / 10000) > ((results.count("empate"))/10000):
            return(idxmax_score_road_team_wins)
        else:
            return(idxmax_score_tie)
    else:
        return(idxmax_score_tie)

st.subheader("Resultado de las simulaciones")

st.markdown("Después de 10 000 simulaciones del\npartido, y considerando los últimos\níndices ofensivos y defensivos de\nlos equipos, el pronóstico es\nque " + str(forecast()) + "\n" + str(score_forecast()))

st.subheader("Fuentes")

st.markdown("Los datos de la simulación provienen del repositorio público actualizado de FiveThirtyEight\nen GitHub sobre el Soccer Power Index, disponible en:")
link='Soccer-SPI Github [link](https://github.com/fivethirtyeight/data/tree/master/soccer-spi)'
st.markdown(link,unsafe_allow_html=True)

st.markdown("Los logos y banderas de los equipos provienen de imágenes en el dominio público,\ndisponibles en:")
link2='Wikipedia [link](https://www.Wikipedia.org)'
st.markdown(link2,unsafe_allow_html=True)
