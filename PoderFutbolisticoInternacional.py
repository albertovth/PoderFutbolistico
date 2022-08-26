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

st.title('Poder Futbolístico de clubes y selecciones nacionales')
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

spi = pd.concat(spi_frames, ignore_index=True)

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Reuniendo índices ofensivos y defensivos por equipo. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

@st.cache
def load_data():
    return spi

df_pf=load_data()
df_pf

Equipo_casa = df_pf['name']

Equipo_visita = df_pf['name']

st.sidebar.subheader('Simular Partido')

params={
    'equipo_casa' : st.sidebar.selectbox('Equipo de casa', Equipo_casa),
    'equipo_visita' : st.sidebar.selectbox('Equipo de visita', Equipo_visita)
}

equipo_casa_input = params['equipo_casa']
equipo_visita_input = params['equipo_visita']

st.text("Has registrado el siguiente equipo en casa: " + equipo_casa_input)
st.text("Has registrado el siguiente equipo de visita: " + equipo_visita_input)

for i in range(100):
    latest_iteration.text(f'Recogiendo logos de los equipos. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

def equipo_casa_input_():
    if equipo_casa_input == "Lille":
        return "LOSC"
    elif equipo_casa_input == "Lyon":
        return "Olympique Lyonnais datei"
    elif equipo_casa_input == "Malmo FF":
        return "Malmo FF datei"
    else:
        return equipo_casa_input

def equipo_visita_input_():
    if equipo_visita_input == "Lille":
        return "LOSC"
    elif equipo_visita_input == "Lyon":
        return "Olympique Lyonnais datei"
    elif equipo_visita_input == "Malmo FF":
        return "Malmo FF datei"
    else:
        return equipo_visita_input

print(equipo_casa_input_())
print(equipo_visita_input_())

def club_logo_home():
    try:
        from googlesearch import search
    except ImportError:
        print('No module named google found')

    query = equipo_casa_input_() + " wikipedia file: logo.svg"

    for j in search(query, num=1, stop=1):
        global j
        print(j)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen

    try:
        html_page = urlopen(j)
    except RuntimeError:
        print('Not found')
    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    logo_list: List[Any] = [k for k in images if "https" and "logo" or "badge" or "crest" in k]

    logo_ht = logo_list[0]

    return logo_ht

def country_flag_home():
    try:
        from googlesearch import search
    except ImportError:
        print('No module named google found')

    query = "'Flag of " + equipo_casa_input + "'" + "File AND svg AND wikipedia AND commons"

    for j in search(query, num=1, stop=1):
        print(j)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen

    try:
        html_page = urlopen(j)
    except RuntimeError:
        print('Not found')
    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    flag_list: List[Any] = [k for k in images if "Flag_of_" in k]

    flag_ht = flag_list[0]

    return flag_ht

def print_team_logo_home():
    if spi_global_rankings['name'].str.contains(str(equipo_casa_input)).any():
        return club_logo_home()
    elif spi_global_rankings_intl['name'].str.contains(str(equipo_casa_input)).any():
        return country_flag_home()


def club_logo_road():
    try:
        from googlesearch import search
    except ImportError:
        print('No module named google found')

    query = equipo_visita_input_() + " wikipedia file: logo.svg"

    for j in search(query, num=1, stop=1):
        print(j)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen

    try:
        html_page = urlopen(j)
    except RuntimeError:
        print('Not found')
    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    logo_list: List[Any] = [k for k in images if "https" and "logo" or "badge" or "crest" in k]

    logo_rt = logo_list[0]

    return logo_rt

def country_flag_road():
    try:
        from googlesearch import search
    except ImportError:
        print('No module named google found')

    query = "'Flag of " + equipo_visita_input + "'" + " File AND svg AND wikipedia AND commons"

    for j in search(query, num=1, stop=1):
        print(j)

    from bs4 import BeautifulSoup as bs
    from urllib.request import urlopen

    try:
        html_page = urlopen(j)
    except RuntimeError:
        print('Not found')
    soup = bs(html_page, features='html.parser')
    images = []

    for img in soup.findAll('img'):
        images.append(img.get('src'))

    flag_list: List[Any] = [k for k in images if "Flag_of_" in k]

    flag_rt = flag_list[0]

    return flag_rt

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

st.write("Simulación de partido")
col1, mid1, col2, mid2, col3, mid3, col4 = st.columns([1,1,5,5,1,1,5])
with col1:
    try:
        st.image(logo_home(), width=60)
    except RuntimeError:
        st.error("Logo no disponible")
with col2:
    st.write(equipo_casa_input)
with mid2:
    st.write("contra")
with col3:
    try:
        st.image(logo_road(), width=60)
    except RuntimeError:
        st.error("Logo no disponible")
with col4:
    st.write(equipo_visita_input)

for i in range(100):
    latest_iteration.text(f'Calculando goles esperados por equipo. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

index_casa_equipo = df_pf.index[df_pf['name'] == equipo_casa_input]
index_visita_equipo = df_pf.index[df_pf['name'] == equipo_visita_input]

equipo_casa_of = df_pf.at[index_casa_equipo[0], 'off']
equipo_casa_def = df_pf.at[index_visita_equipo[0], 'defe']

equipo_visita_of = df_pf.at[index_visita_equipo[0], 'off']
equipo_visita_def = df_pf.at[index_visita_equipo[0], 'defe']

goles_esperados_equipo_casa = ((equipo_casa_of) + (equipo_visita_def)) / 2
goles_esperados_equipo_visita = ((equipo_visita_of) + (equipo_casa_def)) / 2

goles_esperados_equipo_casa_redondeado = round(goles_esperados_equipo_casa,2)

goles_esperados_equipo_visita_redondeado = round(goles_esperados_equipo_visita,2)

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

for i in range(100):
    latest_iteration.text(f'Simulando 10 000 partidos entre los equipos. Porcentaje completado {i+1}')
    bar.progress(i+1)
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
    width=900,
    height=500
)

for i in range(100):
    latest_iteration.text(f'Resumiendo resultados de simulaciones gráficamente. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.altair_chart(datalinea_partido_grafico)

etiquetas = equipo_casa_input + ' gana', equipo_visita_input + ' gana', 'Empate'
proporciones = [results.count("equipo de casa gana"), results.count("equipo de visita gana"), results.count("empate")]
colores = ['green', 'red', 'gold']

st.text(equipo_casa_gana)
st.text(equipo_visita_gana)
st.text(empate)

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

for i in range(100):
    latest_iteration.text(f'Evaluando los resultados con algoritmo, para pronosticar. Porcentaje completado {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

def forecast():
    if ((results.count("equipo de casa gana")) / 10000) > ((results.count("equipo de visita gana")) / 10000) and ((results.count("equipo de casa gana")) / 10000) > (0.4): return(str(equipo_casa_input) + " gana:")
    elif ((results.count("equipo de visita gana")) / 10000) > ((results.count("equipo de casa gana")) / 10000) and ((results.count("equipo de visita gana")) / 10000) > (0.4): return(str(equipo_visita_input) + " gana:")
    else: return("el partido termina en un empate:")

Results = results
Scores = random_marcadores_partido

forecast_scores_dataframe=pd.DataFrame(
    {'Results': Results,
     'Scores': Scores})


scores_home_team_wins = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "equipo de casa gana"]
scores_road_team_wins = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "equipo de visita gana"]
scores_tie = forecast_scores_dataframe.loc[forecast_scores_dataframe.Results == "empate"]

idxmax_score_home_team_wins = scores_home_team_wins['Scores'].value_counts().idxmax()
idxmax_score_road_team_wins = scores_road_team_wins['Scores'].value_counts().idxmax()
idxmax_score_tie = scores_tie['Scores'].value_counts().idxmax()

def score_forecast():
    if ((results.count("equipo de casa gana")) / 10000) > ((results.count("equipo de visita gana")) / 10000) and (
            (results.count("equipo de casa gana")) / 10000) > (0.4):
        return(idxmax_score_home_team_wins)
    elif ((results.count("equipo de visita gana")) / 10000) > ((results.count("equipo de casa gana")) / 10000) and (
            (results.count("equipo de visita gana")) / 10000) > (0.4):
        return(idxmax_score_road_team_wins)
    else:
        return(idxmax_score_tie)

st.sidebar.subheader("Resultado de las simulaciones")

st.sidebar.text("Después de 10 000 simulaciones del\npartido, y considerando los últimos\níndices ofensivos y defensivos de\nlos equipos, el pronóstico es\nque " + str(forecast()) + "\n" + str(score_forecast()))
