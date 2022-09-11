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
