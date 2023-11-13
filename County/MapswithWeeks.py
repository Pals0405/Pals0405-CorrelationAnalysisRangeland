import pandas as pd
from scipy import stats
import math
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
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

for eco in prod1:
    temp1 = pd.DataFrame()
    temp2 = pd.DataFrame()
    temp3 = pd.DataFrame()
    temp4 = pd.DataFrame()
    temp5 = pd.DataFrame()
    temp6 = pd.DataFrame()
    path = "./county"+str(eco)
    tavg = pd.read_csv(path+'/Tcorr.csv')
    dGDD = pd.read_csv(path+'/dayGDDcorr.csv')
    ppt = pd.read_csv(path+'/PPTcorr.csv')
    swrad = pd.read_csv(path+'/swradcorr.csv')
    shortGrass = pd.read_csv(path+'/Ref_ET_Shortgrasscorr.csv')
    tallGrass = pd.read_csv(path+'/Ref_ET_Tallgrasscorr.csv')
    # tavg 
    idx = tavg['max_value'].abs().idxmax()
    temp1 = tavg.loc[[idx]]
    temp1= temp1[['Week_Number','max_value','max_col']]
    temp1['county'] = eco
    temp1['window'] = window_length(tavg['max_col'][idx])
    temp1 = temp1.reset_index(drop=True)
    TempWeek = pd.concat([TempWeek,temp1])

     # dgdd
    idx = dGDD['max_value'].abs().idxmax()
    temp2 = dGDD.loc[[idx]]
    temp2= temp2[['Week_Number','max_value','max_col']]
    temp2['county'] = eco
    temp2['window'] = window_length(dGDD['max_col'][idx])
    temp2 = temp2.reset_index(drop=True)
    dGDDWeek = pd.concat([dGDDWeek,temp2])

     # ppt 
    idx = ppt['max_value'].abs().idxmax()
    temp3 = ppt.loc[[idx]]
    temp3= temp3[['Week_Number','max_value','max_col']]
    temp3['county'] = eco
    temp3['window'] = window_length(ppt['max_col'][idx])
    temp3 = temp3.reset_index(drop=True)
    pptWeek = pd.concat([pptWeek,temp3])

     # swrad
    idx = swrad['max_value'].abs().idxmax()
    temp4 = swrad.loc[[idx]]
    temp4= temp4[['Week_Number','max_value','max_col']]
    temp4['county'] = eco
    temp4['window'] = window_length(swrad['max_col'][idx])
    temp4 = temp4.reset_index(drop=True)
    swradWeek = pd.concat([swradWeek,temp4])

     # shortGrass
    idx = shortGrass['max_value'].abs().idxmax()
    temp5 = shortGrass.loc[[idx]]
    temp5= temp5[['Week_Number','max_value','max_col']]
    temp5['county'] = eco
    temp5['window'] = window_length(shortGrass['max_col'][idx])
    temp5 = temp5.reset_index(drop=True)
    shortGrassWeek = pd.concat([shortGrassWeek,temp5])

     # tallGrass 
    idx = tallGrass['max_value'].abs().idxmax()
    temp6 = tallGrass.loc[[idx]]
    temp6= temp6[['Week_Number','max_value','max_col']]
    temp6['county'] = eco
    temp6['window'] = window_length(tallGrass['max_col'][idx])
    temp6 = temp6.reset_index(drop=True)
    tallGrassWeek = pd.concat([tallGrassWeek,temp6])
    
Maps = pd.read_csv('./county_id_name_fips.csv')
TempWeek.to_csv('TempWeek.csv')
swradWeek.to_csv('swradWeek.csv')
dGDDWeek.to_csv('dGDDWeek.csv')
pptWeek.to_csv('pptWeek.csv')
shortGrassWeek.to_csv('shortGrassWeek.csv')
tallGrassWeek.to_csv('tallGrassWeek.csv')

print(TempWeek)
    
    