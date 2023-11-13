import pandas as pd
from scipy import stats
import math
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
from urllib.request import urlopen
import json
import plotly.express as px
import matplotlib.pyplot as plt
# loading the datasets
prod = pd.read_csv('./county_annual_productivity.csv')
prod1 = list(prod.county.unique())
ans = []
k = 0
for i in prod1:
    temp = prod[prod['county']==i]
    n = len(temp)
    if n <=1:
        ans.append(i)
for i in ans:
    prod1.remove(i)
x = []
for i in range(1,53,10):
    x.append(i)
def window_length(colValue):
    return int(colValue[2:])
TempWeek = pd.DataFrame()
dGDDWeek = pd.DataFrame()
pptWeek = pd.DataFrame()
swradWeek = pd.DataFrame()
shortGrassWeek = pd.DataFrame()
tallGrassWeek = pd.DataFrame()

def calc_window(row):
    return int(row['max_col'][2:])
for eco in prod1:
    path = "./county"+str(eco)
    tavg = pd.read_csv(path+'/Tcorr.csv')
    dGDD = pd.read_csv(path+'/dayGDDcorr.csv')
    ppt = pd.read_csv(path+'/PPTcorr.csv')
    swrad = pd.read_csv(path+'/swradcorr.csv')
    shortGrass = pd.read_csv(path+'/Ref_ET_Shortgrasscorr.csv')
    tallGrass = pd.read_csv(path+'/Ref_ET_Tallgrasscorr.csv')
    # tavg 
    tavg['county'] = eco
    tavg= tavg[['Week_Number','max_value','max_col','p_value','county']]
    temp1 = tavg[tavg['p_value'] > 4.806]
    temp1 = temp1.reset_index(drop=True)
    TempWeek = pd.concat([TempWeek,temp1])

     # dgdd
    dGDD['county'] = eco
    dGDD= dGDD[['Week_Number','max_value','max_col','p_value','county']]
    temp2 = dGDD[dGDD['p_value'] > 4.806]
    temp2 = temp2.reset_index(drop=True)
    dGDDWeek = pd.concat([dGDDWeek,temp2])

#      # ppt 
    ppt['county'] = eco
    ppt= ppt[['Week_Number','max_value','max_col','p_value','county']]
    temp3 = ppt[ppt['p_value'] > 4.806]
    temp3 = temp3.reset_index(drop=True)
    pptWeek = pd.concat([pptWeek,temp3])

#      # swrad
    swrad['county'] = eco
    swrad= swrad[['Week_Number','max_value','max_col','p_value','county']]
    temp4 = swrad[swrad['p_value'] > 4.806]
    temp4 = temp4.reset_index(drop=True)
    swradWeek = pd.concat([swradWeek,temp4])

#      # shortGrass
    shortGrass['county'] = eco
    shortGrass= shortGrass[['Week_Number','max_value','max_col','p_value','county']]
    temp5 = shortGrass[shortGrass['p_value'] > 4.806]
    temp5 = temp5.reset_index(drop=True)
    shortGrassWeek = pd.concat([shortGrassWeek,temp5])

#      # tallGrass 
    tallGrass['county'] = eco
    tallGrass= tallGrass[['Week_Number','max_value','max_col','p_value','county']]
    temp6 = tallGrass[tallGrass['p_value'] > 4.806]
    temp6 = temp6.reset_index(drop=True)
    tallGrassWeek = pd.concat([tallGrassWeek,temp6])
    
# Maps = pd.read_csv('./county_id_name_fips.csv')
# TempWeek.to_csv('TempWeek.csv')
# swradWeek.to_csv('swradWeek.csv')
# dGDDWeek.to_csv('dGDDWeek.csv')
# pptWeek.to_csv('pptWeek.csv')
# shortGrassWeek.to_csv('shortGrassWeek.csv')
# tallGrassWeek.to_csv('tallGrassWeek.csv')
TempWeek['window'] = TempWeek.apply(calc_window,axis=1)
dGDDWeek['window'] = dGDDWeek.apply(calc_window,axis=1)
pptWeek['window'] = pptWeek.apply(calc_window,axis=1)
swradWeek['window'] = swradWeek.apply(calc_window,axis=1)
shortGrassWeek['window'] = shortGrassWeek.apply(calc_window,axis=1)
tallGrassWeek['window'] = tallGrassWeek.apply(calc_window,axis=1)

TavgHigh = TempWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()
dGDDHigh = dGDDWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()
pptHigh = pptWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()
swradHigh = swradWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()
shortGrassHigh = shortGrassWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()
tallGrassHigh = tallGrassWeek.sort_values('p_value', ascending=False).drop_duplicates(['county']).reset_index()

result = pd.concat((TavgHigh, dGDDHigh, pptHigh, swradHigh, shortGrassHigh, tallGrassHigh))
print(result)

VarSign = result['county'].value_counts().reset_index()
Maps = pd.read_csv('./county_id_name_fips.csv')
VarSign = pd.merge(VarSign,Maps, on = ['county'])
print(VarSign)

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

fig1 = px.choropleth(VarSign, geojson=counties, locations='FIPS', color='count',
                            color_continuous_scale="speed",
                            range_color=(1,6),
                            hover_data=['STATE','county_name'],
                            scope="usa",
                            title = 'dGDDCorrelation for Counties(r)',
                            labels={"window":'window'}
                          )

fig1.update_layout(margin={"r":0,"t":50,"l":0,"b":0},title='Number of climatic factors for which correlation is statistically significant',title_x=0.5)
fig1.write_html("NumberOfVariablesPerCounty.html")
fig1.show()

ax = tallGrassHigh['Week_Number'].value_counts().sort_index().plot.bar()
ax.set_title("Weeks exhibiting the highest correlation for Ref_ET_Tallgrass")
ax.set_xlabel("Week Number")
ax.set_ylabel("Frequency")
plt.show()