import pandas as pd
from scipy import stats
import math
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
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
#prod1 = [1]
Counties = pd.DataFrame()
for eco in prod1:
    path = "./county"+str(eco)
    tavg = pd.read_csv(path+'/Tcorr.csv')
    # dGDD = pd.read_csv(path+'/dayGDDcorr.csv')
    ppt = pd.read_csv(path+'/PPTcorr.csv')
    # swrad = pd.read_csv(path+'/swradcorr.csv')
    # shortGrass = pd.read_csv(path+'/Ref_ET_Shortgrasscorr.csv')
    # tallGrass = pd.read_csv(path+'/Ref_ET_Tallgrasscorr.csv')
    tavg['County'] = str(eco)
    # dGDD['County'] = str(eco)
    ppt['County'] = str(eco)
    # swrad['County'] = str(eco)
    # shortGrass['County'] = str(eco)
    # tallGrass['County'] = str(eco)
    tavg = tavg.set_index('Week_Number')
    # dGDD = dGDD.set_index('Week_Number')
    ppt = ppt.set_index('Week_Number')
    # swrad = swrad.set_index('Week_Number')
    # shortGrass = shortGrass.set_index('Week_Number')
    # tallGrass = tallGrass.set_index('Week_Number')
    tavg = tavg[['max_value']].swapaxes("index", "columns")
    # dGDD = dGDD[['max_value']].swapaxes("index", "columns")
    ppt = ppt[['max_value']].swapaxes("index", "columns")
    # swrad = swrad[['max_value']].swapaxes("index", "columns")
    # shortGrass = shortGrass[['max_value']].swapaxes("index", "columns")
    # tallGrass = tallGrass[['max_value']].swapaxes("index", "columns")
    tavg.columns = pd.MultiIndex.from_product([['tavg'], tavg.columns])
    # dGDD.columns = pd.MultiIndex.from_product([['dGDD'], dGDD.columns])
    ppt.columns = pd.MultiIndex.from_product([['ppt'], ppt.columns])
    # swrad.columns = pd.MultiIndex.from_product([['swrad'], swrad.columns])
    # shortGrass.columns = pd.MultiIndex.from_product([['shortGrass'], shortGrass.columns])
    # tallGrass.columns = pd.MultiIndex.from_product([['tallGrass'], tallGrass.columns])
    ans = pd.concat([tavg, ppt], axis = 1)
    ans['County'] = eco
    Counties = pd.concat([Counties,ans])
print(Counties)
Counties = Counties.dropna()
CountyName = Counties['County']
Counties.drop('County',inplace=True,axis=1)

# kmeans_kwargs = {
# "init": "random",
# "n_init": 10,
# "random_state": 1,
# }

# #create list to hold SSE values for each k
# sse = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
#     kmeans.fit(Counties)
#     sse.append(kmeans.inertia_)

# #visualize results
# plt.plot(range(1, 11), sse)
# plt.xticks(range(1, 11))
# plt.xlabel("Number of Clusters")
# plt.ylabel("SSE")
# plt.show()
# print(Counties)

# kmeans = KMeans(n_clusters=2, init='random', max_iter=300, n_init=10, random_state=0)
# y_kmeans = kmeans.fit_predict(Counties)
# print(y_kmeans)
# print(len(y_kmeans))
# silhouette_avg = silhouette_score(Counties, y_kmeans)
# print('The average silhouette score is:', silhouette_avg)

# Counties['cluster'] = kmeans.labels_
# Counties.rename(columns = {'County':'county'}, inplace = True)
# Maps = pd.read_csv('./county_id_name_fips.csv')
# CountyMaps = pd.merge(Counties,Maps, on = ['county'])
# print(CountyMaps)
# CountyMaps.to_csv('CountyMaps_2.csv')

# kmeans = KMeans(n_clusters=3, init='random', max_iter=300, n_init=10, random_state=0)
# y_kmeans = kmeans.fit_predict(Counties)
# print(y_kmeans)
# print(len(y_kmeans))
# silhouette_avg = silhouette_score(Counties, y_kmeans)
# print('The average silhouette score is:', silhouette_avg)

# Counties['cluster'] = kmeans.labels_
# Counties.rename(columns = {'County':'county'}, inplace = True)
# Maps = pd.read_csv('./county_id_name_fips.csv')
# CountyMaps = pd.merge(Counties,Maps, on = ['county'])
# print(CountyMaps)
# CountyMaps.to_csv('CountyMaps_3.csv')

# kmeans = KMeans(n_clusters=4, init='random', max_iter=300, n_init=10, random_state=0)
# y_kmeans = kmeans.fit_predict(Counties)
# print(y_kmeans)
# print(len(y_kmeans))
# silhouette_avg = silhouette_score(Counties, y_kmeans)
# print('The average silhouette score is:', silhouette_avg)

# Counties['cluster'] = kmeans.labels_
# Counties.rename(columns = {'County':'county'}, inplace = True)
# Maps = pd.read_csv('./county_id_name_fips.csv')
# CountyMaps = pd.merge(Counties,Maps, on = ['county'])
# print(CountyMaps)
# CountyMaps.to_csv('CountyMaps_4.csv')

kmeans = KMeans(n_clusters=7, init='random', max_iter=300, n_init=10, random_state=0)
y_kmeans = kmeans.fit_predict(Counties)
print(y_kmeans)
print(len(y_kmeans))
silhouette_avg = silhouette_score(Counties, y_kmeans)
print('The average silhouette score is:', silhouette_avg)

Counties['cluster'] = kmeans.labels_
print(Counties)
Counties['county'] = CountyName
print(Counties)
Maps = pd.read_csv('./county_id_name_fips.csv')
Counties.columns = Counties.columns.droplevel(1)
CountyMaps = pd.merge(Counties,Maps, on = ['county'])
print(CountyMaps)
CountyMaps.to_csv('CountyMaps_TAVG_PPT_7.csv')


