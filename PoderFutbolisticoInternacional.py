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
    
input = ['Afghanistan', 'Albania', 'Algeria', 'Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Basque Country', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde Islands', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China PR', 'Chinese Taipei', 'Colombia', 'Comoros', 'Congo', 'Congo DR', 'Cook Islands', 'Costa Rica', 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia', 'Northern Ireland', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Rep of Ireland', 'Romania', 'Russia', 'Rwanda', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Tahiti', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'Uruguay', 'US Virgin Islands', 'USA', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zanzibar', 'Zimbabwe', 'Manchester City', 'Paris Saint-Germain', 'Liverpool', 'Barcelona', 'Real Madrid', 'Ajax', 'Tottenham Hotspur', 'FC Salzburg', 'Chelsea', 'Arsenal', 'Internazionale', 'Atletico Madrid', 'FC Porto', 'Napoli', 'Borussia Dortmund', 'Villarreal', 'AC Milan', 'RB Leipzig', 'Sporting CP', 'Benfica', 'Brighton and Hove Albion', 'Celtic', 'PSV', 'Zenit St Petersburg', 'Manchester United', 'Real Sociedad', 'Athletic Bilbao', 'Bayer Leverkusen', 'Lyon', 'Newcastle', 'Atalanta', 'Stade Rennes', 'Marseille', 'AS Roma', 'Feyenoord', 'Real Betis', 'West Ham United', '1. FC Union Berlin', 'SC Freiburg', 'Aston Villa', 'Crystal Palace', 'Valencia', 'Borussia Monchengladbach', 'Club Brugge', 'Juventus', 'Lazio', 'Brentford', 'AS Monaco', 'Celta Vigo', 'Flamengo', 'TSG Hoffenheim', 'FC Cologne', 'Lille', 'Rangers', 'Eintracht Frankfurt', 'Lens', 'Osasuna', 'Mainz', 'Sevilla FC', 'Braga', 'Wolverhampton', 'Leicester City', 'Fiorentina', 'VfB Stuttgart', 'VfL Wolfsburg', 'Strasbourg', 'Fenerbahce', 'AZ', 'FC Twente', 'Slavia Prague', 'Leeds United', 'Monterrey', 'Nice', 'Southampton', 'Club América', 'Everton', 'Dinamo Zagreb', 'Torino', 'Palmeiras', 'Genk', 'Udinese', 'Young Boys', 'Rayo Vallecano', 'Atletico Mineiro', 'Werder Bremen', 'Internacional', 'Shakhtar Donetsk', 'Fulham', 'Hertha Berlin', 'Espanyol', 'Getafe', 'Girona FC', 'Norwich City', 'Philadelphia Union', 'Sassuolo', 'Almeria', 'Slovácko', 'Verona', 'São Paolo', 'Nantes', 'Schalke 04', 'Fluminense', 'Tigres UANL', 'Mallorca', 'Pachuca', 'CSKA Moscow', 'Steaua Bucuresti', 'Olympiacos', 'Sheffield United', 'River Plate', 'Red Star Belgrade', 'Real Valladolid', 'Reims', 'Trabzonspor', 'FC Augsburg', 'Spartak Moscow', 'FC Utrecht', 'Anderlecht', 'Antwerp', 'West Bromwich Albion', 'VfL Bochum', 'Cadiz', 'Corinthians', 'Ferencvaros', 'SC Dnipro-1', 'Lorient', 'Molde', 'Istanbul Basaksehir', 'Bodo/Glimt', 'Bragantino', 'Dynamo Kiev', 'Nottingham Forest', 'Watford', 'Bologna', 'Los Angeles FC', 'Viktoria Plzen', 'AFC Bournemouth', 'KAA Gent', 'FC Sheriff Tiraspol', 'Elche', 'FC Copenhagen', 'Kawasaki Frontale', 'Montpellier', 'SK Sturm Graz', 'Besiktas', 'Troyes', 'Toulouse', 'Burnley', 'Yokohama F. Marinos', 'Vitesse', 'Sampdoria', 'Guimaraes', 'Gil Vicente', 'Lecce', 'Brest', 'Angers', 'FC Krasnodar', 'Santos', 'Galatasaray', 'Ceará', 'Dinamo Moscow', 'Guadalajara', 'FC Midtjylland', 'Levante', 'AC Ajaccio', 'FK Partizan Belgrade', 'LASK Linz', 'Fortaleza', 'Santos Laguna', 'Union Saint Gilloise', 'Atlético Paranaense', 'Urawa Red Diamonds', 'Clermont Foot', 'Sochi', 'Cremonese', 'Empoli', 'Heerenveen', 'New York City FC', 'Middlesbrough', 'Konyaspor', 'Salernitana', 'Lech Poznan', 'Auxerre', 'NEC', 'Montreal Impact', 'América Mineiro', 'Portimonense', 'Monza', 'Famalicao', 'Rostov', 'Hapoel Be\'er', 'Basel', 'Spezia', 'St Etienne', 'Chaves', 'Vizela', 'Cuiaba', 'Rosenborg', 'León', 'Boca Juniors', 'Apollon Limassol', 'Estoril Praia', 'Cagliari', 'St Gallen', 'Bordeaux', 'Hamburg SV', 'Metz', 'Santa Clara', 'Botafogo', 'PAOK Salonika', 'Puebla', 'Maccabi Haifa', 'Granada', 'Boavista', 'New York Red Bulls', 'FK Austria Vienna', 'Rio Ave', 'Nashville SC', 'Adana Demirspor', 'Panathinaikos', 'Sparta', 'Los Angeles Galaxy', 'Atlas', 'Silkeborg', 'FC Groningen', 'RKC', 'Cruz Azul', 'Parma', 'Sochaux', 'Casa Pia', 'Rapid Vienna', 'Atlanta United FC', 'Sporting de Charleroi', 'Lokomotiv Moscow', 'AEK Athens', 'Millwall', 'Randers FC', 'Huracán', 'Luton Town', 'Preston North End', 'Austin FC', 'Toluca', 'Sanfrecce Hiroshima', 'Emmen', 'FK Qarabag', 'Stoke City', 'Pumas Unam', 'Velez Sarsfield', 'AEK Larnaca', 'Alanyaspor', 'FC Nordsjaelland', 'Genoa', 'Go Ahead Eagles', 'Bristol City', 'Antalyaspor', 'Wolfsberger AC', 'Seattle Sounders FC', 'Racing Club', 'St. Truidense', 'Cerezo Osaka', 'Valerenga', 'Queens Park Rangers', 'Coventry City', 'CFR 1907 Cluj', 'Cambuur Leeuwarden', 'Aberdeen', 'Necaxa', 'Caen', 'Estudiantes', 'Columbus Crew', 'Kashima Antlers', 'FC Dallas', 'Terek Grozny', 'Orlando City SC', 'Djurgardens IF', 'Tijuana', 'Atlético Goianiense', 'Talleres de Córdoba', 'Tigre', 'Gazisehir Gaziantep', 'Kasimpasa', 'Swansea City', 'Argentinos Juniors', 'Brondby', 'Krylia Sovetov', 'New England Revolution', 'FC Volendam', 'Maritimo', 'SV Darmstadt 98', 'Hammarby', 'Ludogorets', 'Portland Timbers', 'Goiás', 'San Lorenzo', 'FC Cincinnati', 'Lillestrom', 'FC Arouca', 'Cardiff City', 'Blackburn', 'CA Independiente', 'Minnesota United FC', 'Excelsior', 'OH Leuven', 'Eibar', 'Alavés', 'Hearts', 'Real Salt Lake', 'Coritiba', 'KV Mechelen', 'Blackpool', 'Chicago Fire', 'FC Zurich', 'BK Hacken', 'Pacos Ferreira', 'Brescia', 'Viborg', 'Sheffield Wednesday', 'Sunderland', 'SC Paderborn', 'Fortuna Düssseldorf', 'Las Palmas', 'Benevento', 'Ipswich Town', 'Frosinone', 'Standard Liege', 'Fortuna Sittard', 'Querétaro', 'FC Luzern', 'Colorado Rapids', 'Huddersfield Town', 'Avaí', 'Hibernian', 'Slovan Bratislava', 'FC St. Pauli', 'FC Juárez', 'Sporting Kansas City', 'Gimnasia La Plata', 'Newell\'s Old Boys', 'Kayserispor', 'Aris Salonika', 'Paris FC', 'FK Nizhny Novgorod', 'Mamelodi Sundowns', 'Union Santa Fe', 'Toronto FC', 'Hull City', 'Viking FK', 'Derby County', 'Real Oviedo', 'AaB', 'Omonia Nicosia', 'Guingamp', 'Le Havre', 'Juventude', 'Defensa y Justicia', 'Wigan', 'Real Zaragoza', 'F.B.C Unione Venezia', 'Lanus', 'Arminia Bielefeld', 'Servette', 'Malmo FF', 'Fatih Karagümrük', 'IFK Goteborg', 'IF Elfsborg', 'Mazatlán FC', 'Sagan Tosu', 'FC Tokyo', 'SD Huesca', 'KVC Westerlo', 'Rosario Central', 'Reading', 'Karlsruher SC', 'Atlético San Luis', 'Amiens', 'SK Austria Klagenfurt', 'Inter Miami CF', 'Austria Lustenau', 'AGF Aarhus', 'WSG Swarovski Wattens', 'Cercle Brugge', 'Sivasspor', 'Sporting Gijón', 'Nagoya Grampus Eight', 'Birmingham', 'Godoy Cruz', 'Livingston', 'Dijon FCO', 'FC Lugano', 'FC Cartagena', 'Rigas Futbola Skola', 'Banfield', '1. FC Heidenheim 1846', 'Rotherham United', 'Platense', 'Hatayspor', 'FC Sion', 'Hartberg', 'Central Córdoba Santiago del Estero', 'Grasshoppers Zürich', 'Stromsgodset', 'Ballkani', 'FC Khimki', 'AIK', 'Leganes', 'Motherwell', 'Vancouver Whitecaps', 'Colon Santa Fe', 'Charlotte FC', 'Ascoli', 'San Jose Earthquakes', 'Vissel Kobe', 'Tenerife', 'Sarmiento', 'Zalgiris Vilnius', 'Patronato', 'Cittadella', 'Atlético Tucumán', 'Portsmouth', 'KV Oostende', 'KV Kortrijk', 'Barnsley', '1. FC Nürnberg', 'DC United', 'Shimizu S-Pulse', 'Spal', 'Odense BK', 'Arsenal Sarandi', 'Fakel Voronezh', 'Hannover 96', 'Nimes', 'Ross County', 'Houston Dynamo', 'Ternana', 'Haugesund', 'SV Ried', 'Reggina', 'Pisa', 'Giresunspor', 'Holstein Kiel', 'Bari', 'Ural Sverdlovsk Oblast', 'Sarpsborg', 'Barracas Central', 'Kashiwa Reysol', 'SpVgg Greuther Fürth', 'Melbourne City', 'Kilmarnock', 'Gazovik Orenburg', 'AC Horsens', 'Ankaragucu', 'St Mirren', 'Tromso', 'Volos NFC', 'SD Ponferradina', 'Valenciennes', 'Burgos', 'Perugia', 'SV Zulte Waregem', 'Tampa Bay Rowdies', 'Umraniyespor', 'St Johnstone', 'Kalmar FF', 'Villarreal B', 'Peterborough United', 'Consadole Sapporo', 'Mirandes', 'Atromitos', 'UD Ibiza', 'Bastia', 'IFK Norrkoping', 'Louisville City FC', 'Bolton', 'Dundee Utd', 'Málaga', 'Guangzhou Evergrande', 'HJK Helsinki', 'Albacete', 'Cashpoint SC Rheindorf Altach', 'Odd BK', 'Grenoble', 'Eupen', 'Ionikos FC', 'Milton Keynes Dons', 'Wycombe Wanderers', 'FC Vaduz', 'Lyngby', 'Kyoto Purple Sanga', 'Asteras Tripolis', 'Como', 'Istanbulspor', 'Panetolikos', 'Hansa Rostock', 'FC Andorra', 'Avispa Fukuoka', 'Shonan Bellmare', 'Racing Santander', 'Plymouth Argyle', 'Lugo', 'Modena', 'Torpedo Moskow', 'San Diego Loyal SC', 'Aalesund', 'Sydney FC', 'Oxford United', 'Annecy', 'Hamarkamaratene', 'Pau', 'Aldosivi', 'Palermo', 'Laval', 'Melbourne Victory', 'Beijing Guoan', 'Kristiansund BK', 'Gamba Osaka', 'Giannina', 'San Antonio FC', 'Birmingham Legion FC', 'Niort', 'Mjallby', 'Jahn Regensburg', 'Cosenza', 'Shanghai SIPG', 'SV Sandhausen', 'RFC Seraing', 'Charlton Athletic', 'Rodez', 'OFI Crete', 'Sudtirol', '1. FC Kaiserslautern', 'Salford City', 'Orlando Pirates', 'US Quevilly', 'Sandefjord', 'Levadiakos', 'Rio Grande Valley FC Toros', 'Pittsburgh Riverhounds', 'Pyunik Yerevan', 'Memphis 901 FC', 'Western Sydney FC', 'Western United', 'Adelaide United', 'IK Sirius', 'Central Coast Mariners', 'Sacramento Republic FC', 'Kaizer Chiefs', 'SuperSport United', 'Newcastle Jets', 'Shrewsbury Town', 'Shamrock Rovers', 'Eintracht Braunschweig', 'Oakland Roots', 'Miami FC', 'New Mexico United', 'Colorado Springs Switchbacks FC', '1. FC Magdeburg', 'IFK Värnamo', 'Lincoln City', 'Jubilo Iwata', 'Shandong Luneng', 'Jiangsu Suning FC', 'Black Aces', 'Mansfield Town', 'Fleetwood Town', 'Exeter City', 'Lamia', 'Winterthur', 'Cambridge United', 'Varbergs BoIS FC', 'Brisbane Roar', 'El Paso Locomotive FC', 'Cheltenham Town', 'Leyton Orient', 'Doncaster Rovers', 'Bristol Rovers', 'Macarthur FC', 'Stellenbosch FC', 'Accrington Stanley', 'Arizona United', 'Northampton Town', 'Detroit City FC', 'Swindon Town', 'Port Vale', 'Orange County SC', 'AmaZulu', 'Golden Arrows', 'Degerfors IF', 'Colchester United', 'Forest Green Rovers', 'Tulsa Roughnecks', 'Wellington Phoenix', 'FK Jerv', 'Royal AM', 'Burton Albion', 'LA Galaxy II', 'Moroka Swallows', 'Hartford Athletic', 'Charleston Battery', 'Helsingborgs IF', 'Tianjin Teda', 'Tranmere Rovers', 'Monterey Bay', 'Morecambe', 'Sekhukhune United', 'Shanghai Greenland', 'Richards Bay', 'Chippa United', 'Bradford City', 'Newport County', 'Sutton United', 'TS Galaxy', 'Stevenage', 'Crewe Alexandra', 'Hebei China Fortune FC', 'Tshakhuma Tsha Madzivhandila', 'Maritzburg Utd', 'Henan Jianye', 'AFC Wimbledon', 'Indy Eleven', 'Dalian Aerbin', 'Guangzhou RF', 'Perth Glory', 'Wuhan Zall', 'Stockport County', 'GIF Sundsvall', 'Barrow', 'Gillingham', 'Grimsby Town', 'Rochdale', 'Tianjin Quanujian', 'Shenzhen FC', 'Crawley Town', 'Chongqing Lifan', 'Las Vegas Lights FC', 'Walsall', 'Loudoun United FC', 'Harrogate Town', 'Carlisle United', 'Atlanta United 2', 'Hartlepool', 'Guizhou Renhe', 'New York Red Bulls II']

new_input = ['File:Flag_of_Afghanistan.svg', 'File:Flag_of_Albania.svg', 'File:Flag_of_Algeria.svg', 'File:Flag_of_American_Samoa.svg', 'File:Flag_of_Andorra.svg', 'File:Flag_of_Angola.svg', 'File:Flag_of_Anguilla.svg', 'File:Flag_of_Antigua_and_Barbuda.svg', 'File:Flag_of_Argentina.svg', 'File:Flag_of_Armenia.svg', 'File:Flag_of_Aruba.svg', 'File:Flag_of_Australia.svg', 'File:Flag_of_Austria.svg', 'File:Flag_of_Azerbaijan.svg', 'File:Flag_of_Bahamas.svg', 'File:Flag_of_Bahrain.svg', 'File:Flag_of_Bangladesh.svg', 'File:Flag_of_Barbados.svg', 'File:Flag_of_the_Basque_Country.svg', 'File:Flag_of_Belarus.svg', 'File:Flag_of_Belgium.svg', 'File:Flag_of_Belize.svg', 'File:Flag_of_Benin.svg', 'File:Flag_of_Bermuda.svg', 'File:Flag_of_Bhutan.svg', 'File:Flag_of_Bolivia.svg', 'File:Flag_of_Bonaire.svg', 'File:Flag_of_Bosnia_and_Herzegovina.svg', 'File:Flag_of_Botswana.svg', 'File:Flag_of_Brazil.svg', 'File:Flag_of_British_Virgin_Islands.svg', 'File:Flag_of_Brunei.svg', 'File:Flag_of_Bulgaria.svg', 'File:Flag_of_Burkina_Faso.svg', 'File:Flag_of_Burundi.svg', 'File:Flag_of_Cambodia.svg', 'File:Flag_of_Cameroon.svg', 'File:Flag_of_Canada.svg', 'File:Flag_of_Cape_Verde.svg', 'File:Flag_of_Cayman_Islands.svg', 'File:Flag_of_Central_African_Republic.svg', 'File:Flag_of_Chad.svg', 'File:Flag_of_Chile.svg', "File:Flag_of_the_People%27s_Republic_of_China.svg", 'File:Flag_of_the_Republic_of_China.svg', 'File:Flag_of_Colombia.svg', 'File:Flag_of_Comoros.svg', 'File:Flag_of_Congo.svg', 'File:Flag_of_the_Democratic_Republic_of_the_Congo.svg', 'File:Flag_of_Cook_Islands.svg', 'File:Flag_of_Costa_Rica.svg', 'File:Flag_of_Croatia.svg', 'File:Flag_of_Cuba.svg', 'File:Flag_of_Curaçao.svg', 'File:Flag_of_Cyprus.svg', 'File:Flag_of_Czech_Republic.svg', 'File:Flag_of_Denmark.svg', 'File:Flag_of_Djibouti.svg', 'File:Flag_of_Dominica.svg', 'File:Flag_of_Dominican_Republic.svg', 'File:Flag_of_Ecuador.svg', 'File:Flag_of_Egypt.svg', 'File:Flag_of_El_Salvador.svg', 'File:Flag_of_England.svg', 'File:Flag_of_Equatorial_Guinea.svg', 'File:Flag_of_Eritrea.svg', 'File:Flag_of_Estonia.svg', 'File:Flag_of_Ethiopia.svg', 'File:Flag_of_Faroe_Islands.svg', 'File:Flag_of_Fiji.svg', 'File:Flag_of_Finland.svg', 'File:Flag_of_France.svg', 'File:Flag_of_French_Guiana.svg', 'File:Flag_of_Gabon.svg', 'File:Flag_of_Gambia.svg', 'File:Flag_of_Georgia.svg', 'File:Flag_of_Germany.svg', 'File:Flag_of_Ghana.svg', 'File:Flag_of_Gibraltar.svg', 'File:Flag_of_Greece.svg', 'File:Flag_of_Grenada.svg', 'File:Flag_of_Guadeloupe_(local)_variant.svg', 'File:Flag_of_Guam.svg', 'File:Flag_of_Guatemala.svg', 'File:Flag_of_Guinea.svg', 'File:Flag_of_Guinea-Bissau.svg', 'File:Flag_of_Guyana.svg', 'File:Flag_of_Haiti.svg', 'File:Flag_of_Honduras.svg', 'File:Flag_of_Hong_Kong.svg', 'File:Flag_of_Hungary.svg', 'File:Flag_of_Iceland.svg', 'File:Flag_of_India.svg', 'File:Flag_of_Indonesia.svg', 'File:Flag_of_Iran.svg', 'File:Flag_of_Iraq.svg', 'File:Flag_of_Israel.svg', 'File:Flag_of_Italy.svg', 'File:Flag_of_Ivory_Coast.svg', 'File:Flag_of_Jamaica.svg', 'File:Flag_of_Japan.svg', 'File:Flag_of_Jordan.svg', 'File:Flag_of_Kazakhstan.svg', 'File:Flag_of_Kenya.svg', 'File:Flag_of_Kosovo.svg', 'File:Flag_of_Kuwait.svg', 'File:Flag_of_Kyrgyzstan.svg', 'File:Flag_of_Laos.svg', 'File:Flag_of_Latvia.svg', 'File:Flag_of_Lebanon.svg', 'File:Flag_of_Lesotho.svg', 'File:Flag_of_Liberia.svg', 'File:Flag_of_Libya.svg', 'File:Flag_of_Liechtenstein.svg', 'File:Flag_of_Lithuania.svg', 'File:Flag_of_Luxembourg.svg', 'File:Flag_of_Macau.svg', 'File:Flag_of_Madagascar.svg', 'File:Flag_of_Malawi.svg', 'File:Flag_of_Malaysia.svg', 'File:Flag_of_Maldives.svg', 'File:Flag_of_Mali.svg', 'File:Flag_of_Malta.svg', 'File:Flag_of_Martinique.svg', 'File:Flag_of_Mauritania.svg', 'File:Flag_of_Mauritius.svg', 'File:Flag_of_Mexico.svg', 'File:Flag_of_Moldova.svg', 'File:Flag_of_Mongolia.svg', 'File:Flag_of_Montenegro.svg', 'File:Flag_of_Montserrat.svg', 'File:Flag_of_Morocco.svg', 'File:Flag_of_Mozambique.svg', 'File:Flag_of_Myanmar.svg', 'File:Flag_of_Namibia.svg', 'File:Flag_of_Nepal.svg', 'File:Flag_of_Netherlands.svg', 'File:Flag_of_New_Caledonia.svg', 'File:Flag_of_New_Zealand.svg', 'File:Flag_of_Nicaragua.svg', 'File:Flag_of_Niger.svg', 'File:Flag_of_Nigeria.svg', 'File:Flag_of_North_Korea.svg', 'File:Flag_of_North_Macedonia.svg', 'File:Flag_of_Northern_Ireland.svg', 'File:Flag_of_Northern_Mariana_Islands.svg', 'File:Flag_of_Norway.svg', 'File:Flag_of_Oman.svg', 'File:Flag_of_Pakistan.svg', 'File:Flag_of_Palestine.svg', 'File:Flag_of_Panama.svg', 'File:Flag_of_Papua_New_Guinea.svg', 'File:Flag_of_Paraguay.svg', 'File:Flag_of_Peru.svg', 'File:Flag_of_Philippines.svg', 'File:Flag_of_Poland.svg', 'File:Flag_of_Portugal.svg', 'File:Flag_of_Puerto_Rico.svg', 'File:Flag_of_Qatar.svg', 'File:Flag_of_Ireland.svg', 'File:Flag_of_Romania.svg', 'File:Flag_of_Russia.svg', 'File:Flag_of_Rwanda.svg', 'File:Flag_of_San_Marino.svg', 'File:Flag_of_Sao_Tome_and_Principe.svg', 'File:Flag_of_Saudi_Arabia.svg', 'File:Flag_of_Scotland.svg', 'File:Flag_of_Senegal.svg', 'File:Flag_of_Serbia.svg', 'File:Flag_of_Seychelles.svg', 'File:Flag_of_Sierra_Leone.svg', 'File:Flag_of_Singapore.svg', 'File:Flag_of_Sint_Maarten.svg', 'File:Flag_of_Slovakia.svg', 'File:Flag_of_Slovenia.svg', 'File:Flag_of_Solomon_Islands.svg', 'File:Flag_of_Somalia.svg', 'File:Flag_of_South_Africa.svg', 'File:Flag_of_South_Korea.svg', 'File:Flag_of_South_Sudan.svg', 'File:Flag_of_Spain.svg', 'File:Flag_of_Sri_Lanka.svg', 'File:Flag_of_Saint_Kitts_and_Nevis.svg', 'File:Flag_of_Saint_Lucia.svg', 'File:Saint-Martin_Flag.svg', 'File:Flag_of_Saint_Vincent_and_the_Grenadines.svg', 'File:Flag_of_Sudan.svg', 'File:Flag_of_Suriname.svg', 'File:Flag_of_Eswatini.svg', 'File:Flag_of_Sweden.svg', 'File:Flag_of_Switzerland.svg', 'File:Flag_of_Syria.svg', 'File:Flag_of_Tahiti.svg', 'File:Flag_of_Tajikistan.svg', 'File:Flag_of_Tanzania.svg', 'File:Flag_of_Thailand.svg', 'File:Flag_of_East_Timor.svg', 'File:Flag_of_Togo.svg', 'File:Flag_of_Tonga.svg', 'File:Flag_of_Trinidad_and_Tobago.svg', 'File:Flag_of_Tunisia.svg', 'File:Flag_of_Turkey.svg', 'File:Flag_of_Turkmenistan.svg', 'File:Flag_of_Turks_and_Caicos_Islands.svg', 'File:Flag_of_Tuvalu.svg', 'File:Flag_of_Uganda.svg', 'File:Flag_of_Ukraine.svg', 'File:Flag_of_United_Arab_Emirates.svg', 'File:Flag_of_Uruguay.svg', 'File:Flag_of_the_United_States_Virgin_Islands.svg', 'File:Flag_of_the_United_States.svg', 'File:Flag_of_Uzbekistan.svg', 'File:Flag_of_Vanuatu.svg', 'File:Flag_of_Venezuela.svg', 'File:Flag_of_Vietnam.svg', 'File:Flag_of_Wales.svg', 'File:Flag_of_Yemen.svg', 'File:Flag_of_Zambia.svg', 'File:Flag_of_Zanzibar.svg', 'File:Flag_of_Zimbabwe.svg', 'Manchester City', 'Paris Saint-Germain', 'Liverpool', 'Barcelona', 'Real Madrid', 'Ajax', 'Tottenham Hotspur', 'Salzburg FC', 'Chelsea', 'Arsenal', 'Football Club Internazionale Milano', 'Atletico Madrid', 'Porto FC', 'Napoli', 'Borussia Dortmund', 'Villarreal', 'Milan AC', 'Leipzig RB', 'Sporting CP', 'Benfica', 'Brighton and Hove', 'Celtic', 'Eindhoven PSV', 'Zenit St Petersburg', 'Manchester United', 'Real Sociedad', 'Athletic Bilbao', 'Bayer Leverkusen', 'Lyon', 'Newcastle', 'Atalanta', 'Stade Rennes', 'Marseille', 'Roma AS', 'Feyenoord', 'Real Betis', 'West Ham United', 'Union Berlin FC 1.', 'Freiburg SC', 'Aston Villa', 'Crystal Palace', 'Valencia', 'Borussia Monchengladbach', 'Club Brugge', 'Juventus', 'Lazio', 'Brentford', 'Monaco AS', 'Celta Vigo', 'Flamengo', 'Hoffenheim TSG', 'Cologne FC', 'Lille', 'Rangers', 'Eintracht Frankfurt', 'Lens', 'Osasuna', 'Mainz', 'Sevilla FC', 'Braga', 'Wolverhampton', 'Leicester City', 'Fiorentina', 'Stuttgart VfB', 'Wolfsburg VfL', 'Strasbourg', 'Fenerbahce', 'Alkmaar AZ', 'Twente FC', 'Slavia Prague', 'Leeds United', 'Monterrey', 'Nice', 'Southampton', 'America America', 'Everton', 'Dinamo Zagreb', 'Torino', 'Palmeiras', 'Genk', 'Udinese', 'Young Boys', 'Rayo Vallecano', 'Club Atletico Mineiro', 'Werder Bremen', 'Sport Club Internacional', 'Shakhtar Donetsk', 'Fulham', 'Hertha Berlin', 'Espanyol', 'Getafe', 'Girona FC', 'Norwich City', 'Philadelphia Union', 'Sassuolo', 'Almeria', 'Slovacko', 'Verona', 'Sao Paulo', 'Nantes', 'Schalke 4', 'Fluminense', 'Tigres UANL', 'Mallorca', 'Pachuca', 'Moscow CSKA', 'Steaua Bucuresti', 'Olympiacos', 'Sheffield United', 'River Plate', 'Red Star Belgrade', 'Real Valladolid', 'Reims', 'Trabzonspor', 'Augsburg FC', 'Spartak Moscow', 'Utrecht FC', 'Anderlecht', 'Antwerp', 'West Bromwich Albion', 'Bochum VfL', 'Cadiz', 'Corinthians', 'Ferencvaros', 'Dnipro-1 SC', 'Lorient', 'Molde', 'Istanbul Basaksehir', 'Bodo/Glimt', 'Bragantino', 'Dynamo Kiev', 'Nottingham Forest', 'Watford', 'Bologna', 'Los Angeles FC', 'Viktoria Plzen', 'Bournemouth AFC', 'Gent KAA', 'Sheriff Tiraspol FC', 'Elche', 'Copenhagen FC', 'Kawasaki Frontale', 'Montpellier', 'Sturm Graz FK', 'Besiktas', 'Troyes', 'Toulouse', 'Burnley', 'Yokohama F. Marinos', 'Vitesse', 'Sampdoria', 'Guimaraes', 'Gil Vicente', 'Lecce', 'Brest', 'Angers', 'Krasnodar FC', 'Santos', 'Galatasaray', 'Ceara Sporting Club', 'Dinamo Moscow', 'Guadalajara', 'Midtjylland FC', 'Levante', 'Ajaccio AC', 'Partizan Belgrade FK', 'Linz LASK', 'Fortaleza', 'Santos Laguna', 'Union Saint Gilloise', 'Atletico Paranaense', 'Urawa Red Diamonds', 'Clermont Foot', 'Sochi', 'Cremonese', 'Empoli', 'Heerenveen', 'New York City FC', 'Middlesbrough', 'Konyaspor', 'Salernitana', 'Lech Poznan', 'Auxerre', 'NEC', 'Montreal Impact', 'America Futebol Clube MG', 'Portimonense', 'Monza', 'Famalicao', 'Rostov', 'Hapoel Be\'er', 'Basel', 'Spezia', 'Etienne', 'Chaves', 'Vizela', 'Cuiaba', 'Rosenborg', 'Leon', 'Boca Juniors', 'Apollon Limassol', 'Estoril Praia', 'Cagliari', 'Gallen', 'Bordeaux', 'Hamburg SV', 'Metz', 'Santa Clara', 'Botafogo', 'Salonika PAOK', 'Puebla', 'Maccabi Haifa', 'Granada', 'Boavista', 'New York Red Bulls', 'Austria Vienna FK', 'Rio Ave', 'Nashville SC', 'Adana Demirspor', 'Panathinaikos', 'Sparta', 'Galaxy Los Angeles', 'Atlas', 'Silkeborg', 'Groningen FC', 'Waalwijk RKC', 'Cruz Azul', 'Parma', 'Sochaux', 'Casa Pia', 'Rapid Vienna', 'Atlanta United FC', 'Sporting de Charleroi', 'Lokomotiv Moscow', 'Athens AEK', 'Millwall', 'Randers FC', 'Huracan', 'Luton Town', 'Preston North End', 'Austin FC', 'Toluca', 'Sanfrecce Hiroshima', 'Emmen', 'Qarabag FK', 'Stoke City', 'Pumas Unam', 'Velez Sarsfield', 'Larnaca AEK', 'Alanyaspor', 'Nordsjaelland FC', 'Genoa', 'Go Ahead Eagles', 'Bristol City', 'Antalyaspor', 'Wolfsberger AC', 'Seattle Sounders FC', 'Racing Club', 'Truidense', 'Cerezo Osaka', 'Valerenga', 'Queens Park Rangers', 'Coventry City', 'Cluj 1907 CFR', 'Cambuur Leeuwarden', 'Aberdeen', 'Necaxa', 'Caen', 'Estudiantes', 'Columbus Crew', 'Kashima Antlers', 'Dallas FC', 'Terek Grozny', 'Orlando City SC', 'Djurgardens IF', 'Tijuana', 'Atletico Goianiense', 'Talleres de Cordoba', 'Tigre', 'Gazisehir Gaziantep', 'Kasimpasa', 'Swansea City', 'Argentinos Juniors', 'Brondby', 'Krylia Sovetov', 'New England Revolution', 'Volendam FC', 'Maritimo', 'Darmstadt SV 98', 'Hammarby', 'Ludogorets', 'Portland Timbers', 'Goias', 'San Lorenzo', 'Cincinnati FC', 'Lillestrom', 'Arouca FC', 'Cardiff City', 'Blackburn', 'Independiente CA', 'Minnesota United FC', 'Excelsior', 'Leuven OH', 'Eibar', 'Alaves', 'Hearts', 'Real Salt Lake', 'Coritiba', 'Mechelen KV', 'Blackpool', 'Chicago Fire', 'Zurich FC', 'Hacken BK', 'Pacos Ferreira', 'Brescia', 'Viborg', 'Sheffield Wednesday', 'Sunderland', 'Paderborn SC', 'Fortuna Dusseldorf', 'Las Palmas', 'Benevento', 'Ipswich Town', 'Frosinone', 'Standard Liege', 'Fortuna Sittard', 'Queretaro', 'Luzern FC', 'Colorado Rapids', 'Huddersfield Town', 'Avai', 'Hibernian', 'Slovan Bratislava', 'St Pauli FC', 'Juarez FC', 'Sporting Kansas City', 'Gimnasia La Plata', 'Newell\'s Old Boys', 'Kayserispor', 'Aris Salonika', 'Paris FC', 'Nizhny Novgorod FK', 'Mamelodi Sundowns', 'Union Santa Fe', 'Toronto FC', 'Hull City', 'Viking FK', 'Derby County', 'Real Oviedo', 'Fodbold AaB', 'Omonia Nicosia', 'Guingamp', 'Havre Le', 'Juventude', 'Defensa y Justicia', 'Wigan', 'Real Zaragoza', 'Venezia Unione Venezia F.B.C.', 'Lanus', 'Arminia Bielefeld', 'Servette', 'Malmo FF', 'Fatih Karagümrük', 'Goteborg IFK', 'Elfsborg IF', 'Mazatlan FC', 'Sagan Tosu', 'Tokyo FC', 'Huesca SD', 'Westerlo KVC', 'Rosario Central', 'Reading', 'Karlsruher SC', 'Atletico San Luis', 'Amiens', 'Austria Klagenfurt SK', 'Inter Miami CF', 'Austria Lustenau', 'Aarhus AGF', 'Swarovski Wattens WSG', 'Cercle Brugge', 'Sivasspor', 'Sporting Gijón', 'Nagoya Grampus Eight', 'Birmingham', 'Godoy Cruz', 'Livingston', 'Dijon FCO', 'Lugano FC', 'Cartagena FC', 'Rigas Futbola Skola', 'Banfield', 'Heidenheim FC 1. 1846', 'Rotherham United', 'Platense', 'Hatayspor', 'Sion FC', 'Hartberg', 'Central Cordoba Santiago del Estero', 'Grasshoppers Zurich', 'Stromsgodset', 'Ballkani', 'Khimki FC', 'Fotboll AIK', 'Leganes', 'Motherwell', 'Vancouver Whitecaps', 'Colon Santa Fe', 'Charlotte FC', 'Ascoli', 'San Jose Earthquakes', 'Vissel Kobe', 'Tenerife', 'Sarmiento', 'Zalgiris Vilnius', 'Patronato', 'Cittadella', 'Atletico Tucuman', 'Portsmouth', 'Oostende KV', 'Kortrijk KV', 'Barnsley', 'Nurnberg FC 1.', 'D.C. United', 'Shimizu S-Pulse', 'Spal', 'Odense BK', 'Arsenal Sarandi', 'Fakel Voronezh', 'Hannover 96', 'Nimes', 'Ross County', 'Houston Dynamo', 'Ternana', 'Haugesund', 'Ried SV', 'Reggina', 'Pisa', 'Giresunspor', 'Holstein Kiel', 'Bari', 'Ural Sverdlovsk Oblast', 'Sarpsborg', 'Barracas Central', 'Kashiwa Reysol', 'SpVgg Greuther Furth', 'Melbourne City', 'Kilmarnock', 'Gazovik Orenburg', 'Horsens AC', 'Ankaragucu', 'Mirren', 'Tromso', 'Volos NFC', 'Ponferradina SD', 'Valenciennes', 'Burgos', 'Perugia', 'Zulte SV Waregem', 'Tampa Bay Rowdies', 'Umraniyespor', 'Johnstone', 'Kalmar FF', 'Villarreal B', 'Peterborough United', 'Consadole Sapporo', 'Mirandes', 'Atromitos', 'Ibiza UD', 'Bastia', 'Norrkoping IFK', 'Louisville City FC', 'Bolton', 'Dundee Utd', 'Malaga', 'Guangzhou Evergrande', 'Helsinki HJK', 'Albacete', 'Cashpoint SC Rheindorf', 'Odd BK', 'Grenoble', 'Eupen', 'Ionikos FC', 'Milton Keynes Dons', 'Wycombe Wanderers', 'Vaduz FC', 'Lyngby', 'Kyoto Purple Sanga', 'Asteras Tripolis', 'Como', 'Istanbulspor', 'Panetolikos', 'Hansa Rostock', 'Andorra FC', 'Avispa Fukuoka', 'Shonan Bellmare', 'Racing Santander', 'Plymouth Argyle', 'Lugo', 'Modena', 'Torpedo Moskow', 'San Diego Loyal', 'Aalesund', 'Sydney FC', 'Oxford United', 'Annecy', 'Hamarkamaratene', 'Pau', 'Aldosivi', 'Palermo', 'Laval', 'Melbourne Victory', 'Beijing Guoan', 'Kristiansund BK', 'Gamba Osaka', 'Giannina', 'San Antonio FC', 'Birmingham Legion FC', 'Niort', 'Mjallby', 'Jahn Regensburg', 'Cosenza', 'Shanghai SIPG', 'Sandhausen SV', 'Seraing RFC', 'Charlton Athletic', 'Rodez', 'Crete OFI', 'Sudtirol', 'Kaiserlautern FC 1.', 'Salford City', 'Orlando Pirates', 'Quevilly US', 'Sandefjord', 'Levadiakos', 'Rio Grande Valley Toros FC', 'Pittsburgh Riverhounds', 'Pyunik Yerevan', 'Memphis 901 FC', 'Western Sydney FC', 'Western United', 'Adelaide United', 'Sirius IK', 'Central Coast Mariners', 'Sacramento Republic FC', 'Kaizer Chiefs', 'SuperSport United', 'Newcastle Jets', 'Shrewsbury Town', 'Shamrock Rovers', 'Eintracht Braunschweig', 'Oakland Roots', 'Miami FC', 'New Mexico United', 'Colorado Springs Switchbacks FC', 'Magdeburg FC 1.', 'Varnamo IFK', 'Lincoln City', 'Jubilo Iwata', 'Shandong Luneng', 'Jiangsu Suning FC', 'Black Aces', 'Mansfield Town', 'Fleetwood Town', 'Exeter City', 'Lamia', 'Winterthur', 'Cambridge United', 'Varbergs BoIS FC', 'Brisbane Roar', 'El Paso Locomotive FC', 'Cheltenham Town', 'Leyton Orient', 'Doncaster Rovers', 'Bristol Rovers', 'Macarthur FC', 'Stellenbosch FC', 'Accrington Stanley', 'Arizona United', 'Northampton Town', 'Detroit City FC', 'Swindon Town', 'Port Vale', 'Orange County SC', 'AmaZulu', 'Golden Arrows', 'Degerfors IF', 'Colchester United', 'Forest Green Rovers', 'Tulsa Roughnecks', 'Wellington Phoenix', 'Jerv FK', 'Royal AM', 'Burton Albion', 'Galaxy LA II', 'Moroka Swallows', 'Hartford Athletic', 'Charleston Battery', 'Helsingborgs IF', 'Tianjin Teda', 'Tranmere Rovers', 'Monterey Bay', 'Morecambe', 'Sekhukhune United', 'Shanghai Greenland', 'Richards Bay', 'Chippa United', 'Bradford City', 'Newport County', 'Sutton United', 'Galaxy TS', 'Stevenage', 'Crewe Alexandra', 'Hebei China Fortune FC', 'Tshakhuma Tsha Madzivhandila', 'Maritzburg Utd', 'Henan Jianye', 'Wimbledon AFC', 'Indy Eleven', 'Dalian Aerbin', 'Guangzhou RF', 'Perth Glory', 'Wuhan Zall', 'Stockport County', 'Sundsvall GIF', 'Barrow', 'Gillingham', 'Grimsby Town', 'Rochdale', 'Tianjin Quanujian', 'Shenzhen FC', 'Crawley Town', 'Chongqing Lifan', 'Las Vegas Lights FC', 'Walsall', 'Loudoun United FC', 'Harrogate Town', 'Carlisle United', 'Atlanta United 2', 'Hartlepool', 'Guizhou Renhe', 'New York Red Bulls II']

countries = ['File:Flag_of_Afghanistan.svg', 'File:Flag_of_Albania.svg', 'File:Flag_of_Algeria.svg', 'File:Flag_of_American_Samoa.svg', 'File:Flag_of_Andorra.svg', 'File:Flag_of_Angola.svg', 'File:Flag_of_Anguilla.svg', 'File:Flag_of_Antigua_and_Barbuda.svg', 'File:Flag_of_Argentina.svg', 'File:Flag_of_Armenia.svg', 'File:Flag_of_Aruba.svg', 'File:Flag_of_Australia.svg', 'File:Flag_of_Austria.svg', 'File:Flag_of_Azerbaijan.svg', 'File:Flag_of_Bahamas.svg', 'File:Flag_of_Bahrain.svg', 'File:Flag_of_Bangladesh.svg', 'File:Flag_of_Barbados.svg', 'File:Flag_of_the_Basque_Country.svg', 'File:Flag_of_Belarus.svg', 'File:Flag_of_Belgium.svg', 'File:Flag_of_Belize.svg', 'File:Flag_of_Benin.svg', 'File:Flag_of_Bermuda.svg', 'File:Flag_of_Bhutan.svg', 'File:Flag_of_Bolivia.svg', 'File:Flag_of_Bonaire.svg', 'File:Flag_of_Bosnia_and_Herzegovina.svg', 'File:Flag_of_Botswana.svg', 'File:Flag_of_Brazil.svg', 'File:Flag_of_British_Virgin_Islands.svg', 'File:Flag_of_Brunei.svg', 'File:Flag_of_Bulgaria.svg', 'File:Flag_of_Burkina_Faso.svg', 'File:Flag_of_Burundi.svg', 'File:Flag_of_Cambodia.svg', 'File:Flag_of_Cameroon.svg', 'File:Flag_of_Canada.svg', 'File:Flag_of_Cape_Verde.svg', 'File:Flag_of_Cayman_Islands.svg', 'File:Flag_of_Central_African_Republic.svg', 'File:Flag_of_Chad.svg', 'File:Flag_of_Chile.svg', "File:Flag_of_the_People%27s_Republic_of_China.svg", 'File:Flag_of_the_Republic_of_China.svg', 'File:Flag_of_Colombia.svg', 'File:Flag_of_Comoros.svg', 'File:Flag_of_Congo.svg', 'File:Flag_of_the_Democratic_Republic_of_the_Congo.svg', 'File:Flag_of_Cook_Islands.svg', 'File:Flag_of_Costa_Rica.svg', 'File:Flag_of_Croatia.svg', 'File:Flag_of_Cuba.svg', 'File:Flag_of_Curaçao.svg', 'File:Flag_of_Cyprus.svg', 'File:Flag_of_Czech_Republic.svg', 'File:Flag_of_Denmark.svg', 'File:Flag_of_Djibouti.svg', 'File:Flag_of_Dominica.svg', 'File:Flag_of_Dominican_Republic.svg', 'File:Flag_of_Ecuador.svg', 'File:Flag_of_Egypt.svg', 'File:Flag_of_El_Salvador.svg', 'File:Flag_of_England.svg', 'File:Flag_of_Equatorial_Guinea.svg', 'File:Flag_of_Eritrea.svg', 'File:Flag_of_Estonia.svg', 'File:Flag_of_Ethiopia.svg', 'File:Flag_of_Faroe_Islands.svg', 'File:Flag_of_Fiji.svg', 'File:Flag_of_Finland.svg', 'File:Flag_of_France.svg', 'File:Flag_of_French_Guiana.svg', 'File:Flag_of_Gabon.svg', 'File:Flag_of_Gambia.svg', 'File:Flag_of_Georgia.svg', 'File:Flag_of_Germany.svg', 'File:Flag_of_Ghana.svg', 'File:Flag_of_Gibraltar.svg', 'File:Flag_of_Greece.svg', 'File:Flag_of_Grenada.svg', 'File:Flag_of_Guadeloupe_(local)_variant.svg', 'File:Flag_of_Guam.svg', 'File:Flag_of_Guatemala.svg', 'File:Flag_of_Guinea.svg', 'File:Flag_of_Guinea-Bissau.svg', 'File:Flag_of_Guyana.svg', 'File:Flag_of_Haiti.svg', 'File:Flag_of_Honduras.svg', 'File:Flag_of_Hong_Kong.svg', 'File:Flag_of_Hungary.svg', 'File:Flag_of_Iceland.svg', 'File:Flag_of_India.svg', 'File:Flag_of_Indonesia.svg', 'File:Flag_of_Iran.svg', 'File:Flag_of_Iraq.svg', 'File:Flag_of_Israel.svg', 'File:Flag_of_Italy.svg', 'File:Flag_of_Ivory_Coast.svg', 'File:Flag_of_Jamaica.svg', 'File:Flag_of_Japan.svg', 'File:Flag_of_Jordan.svg', 'File:Flag_of_Kazakhstan.svg', 'File:Flag_of_Kenya.svg', 'File:Flag_of_Kosovo.svg', 'File:Flag_of_Kuwait.svg', 'File:Flag_of_Kyrgyzstan.svg', 'File:Flag_of_Laos.svg', 'File:Flag_of_Latvia.svg', 'File:Flag_of_Lebanon.svg', 'File:Flag_of_Lesotho.svg', 'File:Flag_of_Liberia.svg', 'File:Flag_of_Libya.svg', 'File:Flag_of_Liechtenstein.svg', 'File:Flag_of_Lithuania.svg', 'File:Flag_of_Luxembourg.svg', 'File:Flag_of_Macau.svg', 'File:Flag_of_Madagascar.svg', 'File:Flag_of_Malawi.svg', 'File:Flag_of_Malaysia.svg', 'File:Flag_of_Maldives.svg', 'File:Flag_of_Mali.svg', 'File:Flag_of_Malta.svg', 'File:Flag_of_Martinique.svg', 'File:Flag_of_Mauritania.svg', 'File:Flag_of_Mauritius.svg', 'File:Flag_of_Mexico.svg', 'File:Flag_of_Moldova.svg', 'File:Flag_of_Mongolia.svg', 'File:Flag_of_Montenegro.svg', 'File:Flag_of_Montserrat.svg', 'File:Flag_of_Morocco.svg', 'File:Flag_of_Mozambique.svg', 'File:Flag_of_Myanmar.svg', 'File:Flag_of_Namibia.svg', 'File:Flag_of_Nepal.svg', 'File:Flag_of_Netherlands.svg', 'File:Flag_of_New_Caledonia.svg', 'File:Flag_of_New_Zealand.svg', 'File:Flag_of_Nicaragua.svg', 'File:Flag_of_Niger.svg', 'File:Flag_of_Nigeria.svg', 'File:Flag_of_North_Korea.svg', 'File:Flag_of_North_Macedonia.svg', 'File:Flag_of_Northern_Ireland.svg', 'File:Flag_of_Northern_Mariana_Islands.svg', 'File:Flag_of_Norway.svg', 'File:Flag_of_Oman.svg', 'File:Flag_of_Pakistan.svg', 'File:Flag_of_Palestine.svg', 'File:Flag_of_Panama.svg', 'File:Flag_of_Papua_New_Guinea.svg', 'File:Flag_of_Paraguay.svg', 'File:Flag_of_Peru.svg', 'File:Flag_of_Philippines.svg', 'File:Flag_of_Poland.svg', 'File:Flag_of_Portugal.svg', 'File:Flag_of_Puerto_Rico.svg', 'File:Flag_of_Qatar.svg', 'File:Flag_of_Ireland.svg', 'File:Flag_of_Romania.svg', 'File:Flag_of_Russia.svg', 'File:Flag_of_Rwanda.svg', 'File:Flag_of_San_Marino.svg', 'File:Flag_of_Sao_Tome_and_Principe.svg', 'File:Flag_of_Saudi_Arabia.svg', 'File:Flag_of_Scotland.svg', 'File:Flag_of_Senegal.svg', 'File:Flag_of_Serbia.svg', 'File:Flag_of_Seychelles.svg', 'File:Flag_of_Sierra_Leone.svg', 'File:Flag_of_Singapore.svg', 'File:Flag_of_Sint_Maarten.svg', 'File:Flag_of_Slovakia.svg', 'File:Flag_of_Slovenia.svg', 'File:Flag_of_Solomon_Islands.svg', 'File:Flag_of_Somalia.svg', 'File:Flag_of_South_Africa.svg', 'File:Flag_of_South_Korea.svg', 'File:Flag_of_South_Sudan.svg', 'File:Flag_of_Spain.svg', 'File:Flag_of_Sri_Lanka.svg', 'File:Flag_of_Saint_Kitts_and_Nevis.svg', 'File:Flag_of_Saint_Lucia.svg', 'File:Saint-Martin_Flag.svg', 'File:Flag_of_Saint_Vincent_and_the_Grenadines.svg', 'File:Flag_of_Sudan.svg', 'File:Flag_of_Suriname.svg', 'File:Flag_of_Eswatini.svg', 'File:Flag_of_Sweden.svg', 'File:Flag_of_Switzerland.svg', 'File:Flag_of_Syria.svg', 'File:Flag_of_Tahiti.svg', 'File:Flag_of_Tajikistan.svg', 'File:Flag_of_Tanzania.svg', 'File:Flag_of_Thailand.svg', 'File:Flag_of_East_Timor.svg', 'File:Flag_of_Togo.svg', 'File:Flag_of_Tonga.svg', 'File:Flag_of_Trinidad_and_Tobago.svg', 'File:Flag_of_Tunisia.svg', 'File:Flag_of_Turkey.svg', 'File:Flag_of_Turkmenistan.svg', 'File:Flag_of_Turks_and_Caicos_Islands.svg', 'File:Flag_of_Tuvalu.svg', 'File:Flag_of_Uganda.svg', 'File:Flag_of_Ukraine.svg', 'File:Flag_of_United_Arab_Emirates.svg', 'File:Flag_of_Uruguay.svg', 'File:Flag_of_the_United_States_Virgin_Islands.svg', 'File:Flag_of_the_United_States.svg', 'File:Flag_of_Uzbekistan.svg', 'File:Flag_of_Vanuatu.svg', 'File:Flag_of_Venezuela.svg', 'File:Flag_of_Vietnam.svg', 'File:Flag_of_Wales.svg', 'File:Flag_of_Yemen.svg', 'File:Flag_of_Zambia.svg', 'File:Flag_of_Zanzibar.svg', 'File:Flag_of_Zimbabwe.svg']

clubs = ['Manchester City', 'Paris Saint-Germain', 'Liverpool', 'Barcelona', 'Real Madrid', 'Ajax', 'Tottenham Hotspur', 'Salzburg FC', 'Chelsea', 'Arsenal', 'Football Club Internazionale Milano', 'Atletico Madrid', 'Porto FC', 'Napoli', 'Borussia Dortmund', 'Villarreal', 'Milan AC', 'Leipzig RB', 'Sporting CP', 'Benfica', 'Brighton and Hove', 'Celtic', 'Eindhoven PSV', 'Zenit St Petersburg', 'Manchester United', 'Real Sociedad', 'Athletic Bilbao', 'Bayer Leverkusen', 'Lyon', 'Newcastle', 'Atalanta', 'Stade Rennes', 'Marseille', 'Roma AS', 'Feyenoord', 'Real Betis', 'West Ham United', 'Union Berlin FC 1.', 'Freiburg SC', 'Aston Villa', 'Crystal Palace', 'Valencia', 'Borussia Monchengladbach', 'Club Brugge', 'Juventus', 'Lazio', 'Brentford', 'Monaco AS', 'Celta Vigo', 'Flamengo', 'Hoffenheim TSG', 'Cologne FC', 'Lille', 'Rangers', 'Eintracht Frankfurt', 'Lens', 'Osasuna', 'Mainz', 'Sevilla FC', 'Braga', 'Wolverhampton', 'Leicester City', 'Fiorentina', 'Stuttgart VfB', 'Wolfsburg VfL', 'Strasbourg', 'Fenerbahce', 'Alkmaar AZ', 'Twente FC', 'Slavia Prague', 'Leeds United', 'Monterrey', 'Nice', 'Southampton', 'America America', 'Everton', 'Dinamo Zagreb', 'Torino', 'Palmeiras', 'Genk', 'Udinese', 'Young Boys', 'Rayo Vallecano', 'Club Atletico Mineiro', 'Werder Bremen', 'Sport Club Internacional', 'Shakhtar Donetsk', 'Fulham', 'Hertha Berlin', 'Espanyol', 'Getafe', 'Girona FC', 'Norwich City', 'Philadelphia Union', 'Sassuolo', 'Almeria', 'Slovacko', 'Verona', 'Sao Paulo', 'Nantes', 'Schalke 4', 'Fluminense', 'Tigres UANL', 'Mallorca', 'Pachuca', 'Moscow CSKA', 'Steaua Bucuresti', 'Olympiacos', 'Sheffield United', 'River Plate', 'Red Star Belgrade', 'Real Valladolid', 'Reims', 'Trabzonspor', 'Augsburg FC', 'Spartak Moscow', 'Utrecht FC', 'Anderlecht', 'Antwerp', 'West Bromwich Albion', 'Bochum VfL', 'Cadiz', 'Corinthians', 'Ferencvaros', 'Dnipro-1 SC', 'Lorient', 'Molde', 'Istanbul Basaksehir', 'Bodo/Glimt', 'Bragantino', 'Dynamo Kiev', 'Nottingham Forest', 'Watford', 'Bologna', 'Los Angeles FC', 'Viktoria Plzen', 'Bournemouth AFC', 'Gent KAA', 'Sheriff Tiraspol FC', 'Elche', 'Copenhagen FC', 'Kawasaki Frontale', 'Montpellier', 'Sturm Graz FK', 'Besiktas', 'Troyes', 'Toulouse', 'Burnley', 'Yokohama F. Marinos', 'Vitesse', 'Sampdoria', 'Guimaraes', 'Gil Vicente', 'Lecce', 'Brest', 'Angers', 'Krasnodar FC', 'Santos', 'Galatasaray', 'Ceara Sporting Club', 'Dinamo Moscow', 'Guadalajara', 'Midtjylland FC', 'Levante', 'Ajaccio AC', 'Partizan Belgrade FK', 'Linz LASK', 'Fortaleza', 'Santos Laguna', 'Union Saint Gilloise', 'Atletico Paranaense', 'Urawa Red Diamonds', 'Clermont Foot', 'Sochi', 'Cremonese', 'Empoli', 'Heerenveen', 'New York City FC', 'Middlesbrough', 'Konyaspor', 'Salernitana', 'Lech Poznan', 'Auxerre', 'NEC', 'Montreal Impact', 'America Futebol Clube MG', 'Portimonense', 'Monza', 'Famalicao', 'Rostov', 'Hapoel Be\'er', 'Basel', 'Spezia', 'Etienne', 'Chaves', 'Vizela', 'Cuiaba', 'Rosenborg', 'Leon', 'Boca Juniors', 'Apollon Limassol', 'Estoril Praia', 'Cagliari', 'Gallen', 'Bordeaux', 'Hamburg SV', 'Metz', 'Santa Clara', 'Botafogo', 'Salonika PAOK', 'Puebla', 'Maccabi Haifa', 'Granada', 'Boavista', 'New York Red Bulls', 'Austria Vienna FK', 'Rio Ave', 'Nashville SC', 'Adana Demirspor', 'Panathinaikos', 'Sparta', 'Galaxy Los Angeles', 'Atlas', 'Silkeborg', 'Groningen FC', 'Waalwijk RKC', 'Cruz Azul', 'Parma', 'Sochaux', 'Casa Pia', 'Rapid Vienna', 'Atlanta United FC', 'Sporting de Charleroi', 'Lokomotiv Moscow', 'Athens AEK', 'Millwall', 'Randers FC', 'Huracan', 'Luton Town', 'Preston North End', 'Austin FC', 'Toluca', 'Sanfrecce Hiroshima', 'Emmen', 'Qarabag FK', 'Stoke City', 'Pumas Unam', 'Velez Sarsfield', 'Larnaca AEK', 'Alanyaspor', 'Nordsjaelland FC', 'Genoa', 'Go Ahead Eagles', 'Bristol City', 'Antalyaspor', 'Wolfsberger AC', 'Seattle Sounders FC', 'Racing Club', 'Truidense', 'Cerezo Osaka', 'Valerenga', 'Queens Park Rangers', 'Coventry City', 'Cluj 1907 CFR', 'Cambuur Leeuwarden', 'Aberdeen', 'Necaxa', 'Caen', 'Estudiantes', 'Columbus Crew', 'Kashima Antlers', 'Dallas FC', 'Terek Grozny', 'Orlando City SC', 'Djurgardens IF', 'Tijuana', 'Atletico Goianiense', 'Talleres de Cordoba', 'Tigre', 'Gazisehir Gaziantep', 'Kasimpasa', 'Swansea City', 'Argentinos Juniors', 'Brondby', 'Krylia Sovetov', 'New England Revolution', 'Volendam FC', 'Maritimo', 'Darmstadt SV 98', 'Hammarby', 'Ludogorets', 'Portland Timbers', 'Goias', 'San Lorenzo', 'Cincinnati FC', 'Lillestrom', 'Arouca FC', 'Cardiff City', 'Blackburn', 'Independiente CA', 'Minnesota United FC', 'Excelsior', 'Leuven OH', 'Eibar', 'Alaves', 'Hearts', 'Real Salt Lake', 'Coritiba', 'Mechelen KV', 'Blackpool', 'Chicago Fire', 'Zurich FC', 'Hacken BK', 'Pacos Ferreira', 'Brescia', 'Viborg', 'Sheffield Wednesday', 'Sunderland', 'Paderborn SC', 'Fortuna Dusseldorf', 'Las Palmas', 'Benevento', 'Ipswich Town', 'Frosinone', 'Standard Liege', 'Fortuna Sittard', 'Queretaro', 'Luzern FC', 'Colorado Rapids', 'Huddersfield Town', 'Avai', 'Hibernian', 'Slovan Bratislava', 'St Pauli FC', 'Juarez FC', 'Sporting Kansas City', 'Gimnasia La Plata', 'Newell\'s Old Boys', 'Kayserispor', 'Aris Salonika', 'Paris FC', 'Nizhny Novgorod FK', 'Mamelodi Sundowns', 'Union Santa Fe', 'Toronto FC', 'Hull City', 'Viking FK', 'Derby County', 'Real Oviedo', 'Fodbold AaB', 'Omonia Nicosia', 'Guingamp', 'Havre Le', 'Juventude', 'Defensa y Justicia', 'Wigan', 'Real Zaragoza', 'Venezia Unione Venezia F.B.C.', 'Lanus', 'Arminia Bielefeld', 'Servette', 'Malmo FF', 'Fatih Karagümrük', 'Goteborg IFK', 'Elfsborg IF', 'Mazatlan FC', 'Sagan Tosu', 'Tokyo FC', 'Huesca SD', 'Westerlo KVC', 'Rosario Central', 'Reading', 'Karlsruher SC', 'Atletico San Luis', 'Amiens', 'Austria Klagenfurt SK', 'Inter Miami CF', 'Austria Lustenau', 'Aarhus AGF', 'Swarovski Wattens WSG', 'Cercle Brugge', 'Sivasspor', 'Sporting Gijón', 'Nagoya Grampus Eight', 'Birmingham', 'Godoy Cruz', 'Livingston', 'Dijon FCO', 'Lugano FC', 'Cartagena FC', 'Rigas Futbola Skola', 'Banfield', 'Heidenheim FC 1. 1846', 'Rotherham United', 'Platense', 'Hatayspor', 'Sion FC', 'Hartberg', 'Central Cordoba Santiago del Estero', 'Grasshoppers Zurich', 'Stromsgodset', 'Ballkani', 'Khimki FC', 'Fotboll AIK', 'Leganes', 'Motherwell', 'Vancouver Whitecaps', 'Colon Santa Fe', 'Charlotte FC', 'Ascoli', 'San Jose Earthquakes', 'Vissel Kobe', 'Tenerife', 'Sarmiento', 'Zalgiris Vilnius', 'Patronato', 'Cittadella', 'Atletico Tucuman', 'Portsmouth', 'Oostende KV', 'Kortrijk KV', 'Barnsley', 'Nurnberg FC 1.', 'D.C. United', 'Shimizu S-Pulse', 'Spal', 'Odense BK', 'Arsenal Sarandi', 'Fakel Voronezh', 'Hannover 96', 'Nimes', 'Ross County', 'Houston Dynamo', 'Ternana', 'Haugesund', 'Ried SV', 'Reggina', 'Pisa', 'Giresunspor', 'Holstein Kiel', 'Bari', 'Ural Sverdlovsk Oblast', 'Sarpsborg', 'Barracas Central', 'Kashiwa Reysol', 'SpVgg Greuther Furth', 'Melbourne City', 'Kilmarnock', 'Gazovik Orenburg', 'Horsens AC', 'Ankaragucu', 'Mirren', 'Tromso', 'Volos NFC', 'Ponferradina SD', 'Valenciennes', 'Burgos', 'Perugia', 'Zulte SV Waregem', 'Tampa Bay Rowdies', 'Umraniyespor', 'Johnstone', 'Kalmar FF', 'Villarreal B', 'Peterborough United', 'Consadole Sapporo', 'Mirandes', 'Atromitos', 'Ibiza UD', 'Bastia', 'Norrkoping IFK', 'Louisville City FC', 'Bolton', 'Dundee Utd', 'Malaga', 'Guangzhou Evergrande', 'Helsinki HJK', 'Albacete', 'Cashpoint SC Rheindorf', 'Odd BK', 'Grenoble', 'Eupen', 'Ionikos FC', 'Milton Keynes Dons', 'Wycombe Wanderers', 'Vaduz FC', 'Lyngby', 'Kyoto Purple Sanga', 'Asteras Tripolis', 'Como', 'Istanbulspor', 'Panetolikos', 'Hansa Rostock', 'Andorra FC', 'Avispa Fukuoka', 'Shonan Bellmare', 'Racing Santander', 'Plymouth Argyle', 'Lugo', 'Modena', 'Torpedo Moskow', 'San Diego Loyal', 'Aalesund', 'Sydney FC', 'Oxford United', 'Annecy', 'Hamarkamaratene', 'Pau', 'Aldosivi', 'Palermo', 'Laval', 'Melbourne Victory', 'Beijing Guoan', 'Kristiansund BK', 'Gamba Osaka', 'Giannina', 'San Antonio FC', 'Birmingham Legion FC', 'Niort', 'Mjallby', 'Jahn Regensburg', 'Cosenza', 'Shanghai SIPG', 'Sandhausen SV', 'Seraing RFC', 'Charlton Athletic', 'Rodez', 'Crete OFI', 'Sudtirol', 'Kaiserlautern FC 1.', 'Salford City', 'Orlando Pirates', 'Quevilly US', 'Sandefjord', 'Levadiakos', 'Rio Grande Valley Toros FC', 'Pittsburgh Riverhounds', 'Pyunik Yerevan', 'Memphis 901 FC', 'Western Sydney FC', 'Western United', 'Adelaide United', 'Sirius IK', 'Central Coast Mariners', 'Sacramento Republic FC', 'Kaizer Chiefs', 'SuperSport United', 'Newcastle Jets', 'Shrewsbury Town', 'Shamrock Rovers', 'Eintracht Braunschweig', 'Oakland Roots', 'Miami FC', 'New Mexico United', 'Colorado Springs Switchbacks FC', 'Magdeburg FC 1.', 'Varnamo IFK', 'Lincoln City', 'Jubilo Iwata', 'Shandong Luneng', 'Jiangsu Suning FC', 'Black Aces', 'Mansfield Town', 'Fleetwood Town', 'Exeter City', 'Lamia', 'Winterthur', 'Cambridge United', 'Varbergs BoIS FC', 'Brisbane Roar', 'El Paso Locomotive FC', 'Cheltenham Town', 'Leyton Orient', 'Doncaster Rovers', 'Bristol Rovers', 'Macarthur FC', 'Stellenbosch FC', 'Accrington Stanley', 'Arizona United', 'Northampton Town', 'Detroit City FC', 'Swindon Town', 'Port Vale', 'Orange County SC', 'AmaZulu', 'Golden Arrows', 'Degerfors IF', 'Colchester United', 'Forest Green Rovers', 'Tulsa Roughnecks', 'Wellington Phoenix', 'Jerv FK', 'Royal AM', 'Burton Albion', 'Galaxy LA II', 'Moroka Swallows', 'Hartford Athletic', 'Charleston Battery', 'Helsingborgs IF', 'Tianjin Teda', 'Tranmere Rovers', 'Monterey Bay', 'Morecambe', 'Sekhukhune United', 'Shanghai Greenland', 'Richards Bay', 'Chippa United', 'Bradford City', 'Newport County', 'Sutton United', 'Galaxy TS', 'Stevenage', 'Crewe Alexandra', 'Hebei China Fortune FC', 'Tshakhuma Tsha Madzivhandila', 'Maritzburg Utd', 'Henan Jianye', 'Wimbledon AFC', 'Indy Eleven', 'Dalian Aerbin', 'Guangzhou RF', 'Perth Glory', 'Wuhan Zall', 'Stockport County', 'Sundsvall GIF', 'Barrow', 'Gillingham', 'Grimsby Town', 'Rochdale', 'Tianjin Quanujian', 'Shenzhen FC', 'Crawley Town', 'Chongqing Lifan', 'Las Vegas Lights FC', 'Walsall', 'Loudoun United FC', 'Harrogate Town', 'Carlisle United', 'Atlanta United 2', 'Hartlepool', 'Guizhou Renhe', 'New York Red Bulls II']

clubs_df=pd.DataFrame()

countries_df=pd.DataFrame()

clubs_df['clubs']=clubs

countries_df['countries']=countries
    
def equipo_casa_input_():
    if equipo_casa_input in input:
        i=input.index(equipo_casa_input)
        return(new_input[i])
    else:
        return equipo_casa_input
    
def equipo_visita_input_():
    if equipo_visita_input in input:
        i=input.index(equipo_visita_input)
        return(new_input[i])
    else:
        return equipo_visita_input

def club_logo_home():
    try:
        from wikipedia import search
    except ImportError:
        print('No module named google found')

    query =  wikipedia.search(str(equipo_casa_input_())+" "+str("football club"))

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

    my_string_=str(equipo_casa_input_())
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

    my_string=str(equipo_casa_input_())
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
        
    print(flag_list)

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

    print(flag_ht)
    
def print_team_logo_home():
    if countries_df['countries'].eq(str(equipo_casa_input_())).any():
        return country_flag_home()
    else:
        return club_logo_home()

def club_logo_road():
    try:
        from wikipedia import search
    except ImportError:
        print('No module named google found')

    query =  wikipedia.search(str(equipo_visita_input_())+" "+str("football club"))

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

    my_string_=str(equipo_visita_input_())
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

    my_string=str(equipo_visita_input_())
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
    if countries_df['countries'].eq(str(equipo_visita_input_())).any():
        return country_flag_road()
    else:
        return club_logo_road()

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

alpha = 0.05

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
