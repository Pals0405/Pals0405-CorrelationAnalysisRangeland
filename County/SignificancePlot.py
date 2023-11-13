import pandas as pd
from urllib.request import urlopen
import json
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# import seaborn as sns

SignCounties = pd.read_csv('./CountyAvg.csv')
Maps = pd.read_csv('./county_id_name_fips.csv')
SignCounties = pd.merge(SignCounties,Maps, on = ['county'])
print(SignCounties)

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig1 = px.choropleth(SignCounties, geojson=counties, locations='FIPS', color='window',
                            color_continuous_scale="Picnic",
                            range_color=(1,25),
                            hover_data=['STATE','county_name'],
                            scope="usa",
                            title = 'dGDDCorrelation for Counties(r)',
                            labels={"window":'window'}
                          )

fig1.update_layout(margin={"r":0,"t":50,"l":0,"b":0},title='Avg Window size for counties',title_x=0.5)
fig1.write_html("SignificanceCountyWithWindows.html")
fig1.show()

ax = SignCounties['window'].value_counts().sort_index().plot.bar()
ax.set_title("Frequency of average window size across counties")
ax.set_xlabel("Average Window Size")
ax.set_ylabel("Frequency")
plt.show()

