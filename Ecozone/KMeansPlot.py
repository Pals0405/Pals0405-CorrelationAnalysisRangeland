import pandas as pd
from scipy import stats
import math
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import geopandas as gpd 
import os 
import plotly.express as px
# loading the datasets
prod = pd.read_csv('./ecozone_annual_productivity.csv')
prod1 = list(prod.ecozone.unique())
prod1.remove(38)
print(len(prod1)) #76 ecozones
#prod1 = [1]
# Ecozones = pd.DataFrame(prod1, columns=['Ecozone']) 
# print(Ecozones)
Ecozones = pd.DataFrame()
for eco in prod1:
    path = "./ecozone"+str(eco)
    tavg = pd.read_csv(path+'/Tcorr.csv')
    dGDD = pd.read_csv(path+'/dayGDDcorr.csv')
    ppt = pd.read_csv(path+'/PPTcorr.csv')
    swrad = pd.read_csv(path+'/swradcorr.csv')
    shortGrass = pd.read_csv(path+'/Ref_ET_Shortgrasscorr.csv')
    tallGrass = pd.read_csv(path+'/Ref_ET_Tallgrasscorr.csv')
    tavg['Ecozone'] = eco
    dGDD['Ecozone'] = eco
    ppt['Ecozone'] = eco
    swrad['Ecozone'] = eco
    shortGrass['Ecozone'] = eco
    tallGrass['Ecozone'] = eco
    tavg = tavg.set_index('Week_Number')
    dGDD = dGDD.set_index('Week_Number')
    ppt = ppt.set_index('Week_Number')
    swrad = swrad.set_index('Week_Number')
    shortGrass = shortGrass.set_index('Week_Number')
    tallGrass = tallGrass.set_index('Week_Number')
    tavg = tavg[['max_value']].swapaxes("index", "columns")
    dGDD = dGDD[['max_value']].swapaxes("index", "columns")
    ppt = ppt[['max_value']].swapaxes("index", "columns")
    swrad = swrad[['max_value']].swapaxes("index", "columns")
    shortGrass = shortGrass[['max_value']].swapaxes("index", "columns")
    tallGrass = tallGrass[['max_value']].swapaxes("index", "columns")
    tavg.columns = pd.MultiIndex.from_product([['tavg'], tavg.columns])
    dGDD.columns = pd.MultiIndex.from_product([['dGDD'], dGDD.columns])
    ppt.columns = pd.MultiIndex.from_product([['ppt'], ppt.columns])
    swrad.columns = pd.MultiIndex.from_product([['swrad'], swrad.columns])
    shortGrass.columns = pd.MultiIndex.from_product([['shortGrass'], shortGrass.columns])
    tallGrass.columns = pd.MultiIndex.from_product([['tallGrass'], tallGrass.columns])
    ans = pd.concat([tavg, dGDD, ppt,swrad,shortGrass,tallGrass], axis = 1)
    ans['Ecozone'] = eco
    Ecozones = pd.concat([Ecozones,ans])
# print(Ecozones.columns)
#print(Ecozones)
Ecozones = Ecozones.dropna()
kmeans_kwargs = {
"init": "random",
"n_init": 10,
"random_state": 1,
}

#create list to hold SSE values for each k
sse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(Ecozones)
    sse.append(kmeans.inertia_)

#visualize results
plt.plot(range(1, 11), sse)
plt.xticks(range(1, 11))
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.show()

df = gpd.read_file('./us_eco_l3_state_boundaries/us_eco_l3_state_boundaries.shp')
df = df.to_crs("EPSG:4326")

kmeans = KMeans(n_clusters=2, init='k-means++', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(Ecozones)
print(y_kmeans)
print(len(y_kmeans))
silhouette_avg = silhouette_score(Ecozones, y_kmeans)
print('The average silhouette score is:', silhouette_avg)
Ecozones['cluster'] = kmeans.labels_
EcozonesMap = Ecozones[['Ecozone','cluster']]

print(Ecozones)
print(EcozonesMap)
print(df)
df.rename(columns = {'US_L3CODE':'Ecozone'}, inplace = True)
df['Ecozone']=df['Ecozone'].astype(int)
print(EcozonesMap)
print(EcozonesMap.info())
EcozonesMap.columns = EcozonesMap.columns.droplevel(1)
# data = df.join(EcozonesMap.droplevel(0), on='Ecozone')
data = df.merge(EcozonesMap,on='Ecozone', how='right')
print(df.iloc[0,:])
print(df.info())
print(EcozonesMap.columns)
print(EcozonesMap.info())
print(data.info())
print(data)

fig = px.choropleth(data, geojson=data.geometry, 
                    locations=data.index, color="cluster",
                    height=500,
                   color_continuous_scale="Viridis")
fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(
    title_text='Map'
)
fig.update(layout = dict(title=dict(x=0.5)))
fig.update_layout(
    margin={"r":0,"t":30,"l":10,"b":10},
    coloraxis_colorbar={
        'title':'Sum'})
fig.show()

# print(data.info())
# kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
# y_kmeans = kmeans.fit_predict(Ecozones)
# print(y_kmeans)
# print(len(y_kmeans))
# silhouette_avg = silhouette_score(Ecozones, y_kmeans)
# print('The average silhouette score is:', silhouette_avg)
# Ecozones['cluster'] = kmeans.labels_
# print(Ecozones)