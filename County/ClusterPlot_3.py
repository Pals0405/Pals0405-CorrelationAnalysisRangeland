import pandas as pd
from urllib.request import urlopen
import json
import certifi
import plotly.express as px
prod = pd.read_csv('./county_annual_productivity.csv')
prod1 = list(prod.county.unique())  # 1627 counties with annual productivity data 
print(len(prod1))

prod = pd.read_csv('./county_id_name_fips.csv')
prod1 = list(prod.county.unique())
print(len(prod1))

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
CountyMaps = pd.read_csv('./CountyMaps_3.csv')
print(CountyMaps)
fig = px.choropleth(CountyMaps, geojson=counties, locations='FIPS', color="('cluster', '')",
                            hover_data=['STATE','county_name'],
                           scope="usa",
                           labels={"('cluster', '')":'Cluster'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.write_html("County_Cluster_3.html")
fig.show()
