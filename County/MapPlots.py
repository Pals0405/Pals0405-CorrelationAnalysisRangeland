import pandas as pd
from urllib.request import urlopen
import json
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def offsetWeeks(row):
  if row['Week_Number'] < 50:
    val = row['Week_Number']+4
  else:
    val = (row['Week_Number']-50)+1
  return val
dGDDWeek = pd.read_csv('./dGDDWeek.csv')
Maps = pd.read_csv('./county_id_name_fips.csv')
dGDDWeek = pd.merge(dGDDWeek,Maps, on = ['county'])
#TempCounties['Week'] = TempCounties.apply(offsetWeeks,axis=1)
print(dGDDWeek)
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig1 = px.choropleth(dGDDWeek, geojson=counties, locations='FIPS', color='max_value',
                            color_continuous_scale="Picnic",
                            range_color=(-1,1),
                            hover_data=['STATE','county_name'],
                            scope="usa",
                            title = 'ppt Correlation for Counties(r)',
                            labels={"max_value":'r'}
                          )
fig2 = px.choropleth(dGDDWeek, geojson=counties, locations='FIPS', color='Week_Number',
                            color_continuous_scale="matter",
                            range_color=(1,53),
                            hover_data=['STATE','county_name'],
                            scope="usa",
                            title = 'ppt Correlation for Counties(Week Number)',
                            labels={"Week_Number":'Week'}
                          )
fig3 = px.choropleth(dGDDWeek, geojson=counties, locations='FIPS', color='window',
                            color_continuous_scale="speed",
                            range_color=(1,25),
                            hover_data=['STATE','county_name'],
                            scope="usa",
                            title = 'ppt Correlation for Counties(Week Number)',
                            labels={"Week_Number":'Week'}
                          )


fig1.update_layout(margin={"r":0,"t":50,"l":0,"b":0},title='dayGDD Correlation for Counties(r)',title_x=0.5)
fig1.write_html("./CorrelationResultsMaps/dGDDWeekMap1.html")
fig1.show()

fig2.update_layout(margin={"r":0,"t":50,"l":0,"b":0},title='dayGDD Correlation for Counties(Week Number)',title_x=0.5)
fig2.write_html("./CorrelationResultsMaps/dGDDWeekMap2.html")
fig2.show()

fig3.update_layout(margin={"r":0,"t":50,"l":0,"b":0},title='dayGDD Correlation for Counties(Window Size)',title_x=0.5)
fig3.write_html("./CorrelationResultsMaps/dGDDWeekMap3.html")
fig3.show()
