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
    temp1 = tavg[tavg['p_value'] > 5.115]
    temp1 = temp1.reset_index(drop=True)
    TempWeek = pd.concat([TempWeek,temp1])

     # dgdd
    dGDD['county'] = eco
    dGDD= dGDD[['Week_Number','max_value','max_col','p_value','county']]
    temp2 = dGDD[dGDD['p_value'] > 5.115]
    temp2 = temp2.reset_index(drop=True)
    dGDDWeek = pd.concat([dGDDWeek,temp2])

#      # ppt 
    ppt['county'] = eco
    ppt= ppt[['Week_Number','max_value','max_col','p_value','county']]
    temp3 = ppt[ppt['p_value'] > 5.115]
    temp3 = temp3.reset_index(drop=True)
    pptWeek = pd.concat([pptWeek,temp3])

#      # swrad
    swrad['county'] = eco
    swrad= swrad[['Week_Number','max_value','max_col','p_value','county']]
    temp4 = swrad[swrad['p_value'] > 5.115]
    temp4 = temp4.reset_index(drop=True)
    swradWeek = pd.concat([swradWeek,temp4])

#      # shortGrass
    shortGrass['county'] = eco
    shortGrass= shortGrass[['Week_Number','max_value','max_col','p_value','county']]
    temp5 = shortGrass[shortGrass['p_value'] > 5.115]
    temp5 = temp5.reset_index(drop=True)
    shortGrassWeek = pd.concat([shortGrassWeek,temp5])

#      # tallGrass 
    tallGrass['county'] = eco
    tallGrass= tallGrass[['Week_Number','max_value','max_col','p_value','county']]
    temp6 = tallGrass[tallGrass['p_value'] > 5.115]
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

AvgWindow1 = TempWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow2 = TempWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow1.to_csv('window_counties/TempWeek_counties.csv')
AvgWindow2.to_csv('window_weeks/TempWeek_weeks.csv')
print(AvgWindow1)
print(AvgWindow2)

AvgWindow3 = dGDDWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow4 = dGDDWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow3.to_csv('window_counties/dGDDWeek_counties.csv')
AvgWindow4.to_csv('window_weeks/dGDDWeek_weeks.csv')
print(AvgWindow3)
print(AvgWindow4)
    
AvgWindow5 = pptWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow6 = pptWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow5.to_csv('window_counties/pptWeek_counties.csv')
AvgWindow6.to_csv('window_weeks/pptWeek_weeks.csv')
print(AvgWindow5)
print(AvgWindow6)

AvgWindow7 = swradWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow8 = swradWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow7.to_csv('window_counties/swradWeek_counties.csv')
AvgWindow8.to_csv('window_weeks/swradWeek_weeks.csv')
print(AvgWindow7)
print(AvgWindow8)

AvgWindow9 = shortGrassWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow10 = shortGrassWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow9.to_csv('window_counties/shortGrassWeek_counties.csv')
AvgWindow10.to_csv('window_weeks/shortGrassWeek_weeks.csv')
print(AvgWindow9)
print(AvgWindow10)

AvgWindow11 = tallGrassWeek.groupby('county')['window'].mean().round(0).reset_index()
AvgWindow12 = tallGrassWeek.groupby('Week_Number')['window'].mean().round(0).reset_index()
AvgWindow11.to_csv('window_counties/tallGrassWeek_counties.csv')
AvgWindow12.to_csv('window_weeks/tallGrassWeek_weeks.csv')
print(AvgWindow11)
print(AvgWindow12)

WeeklyAvg = pd.concat((AvgWindow2, AvgWindow4, AvgWindow6, AvgWindow8, AvgWindow10, AvgWindow12)).groupby('Week_Number')['window'].mean().round(0).reset_index()
CountyAvg = pd.concat((AvgWindow1, AvgWindow3, AvgWindow5, AvgWindow7, AvgWindow9, AvgWindow11)).groupby('county')['window'].mean().round(0).reset_index()
print(WeeklyAvg)
print(CountyAvg)

WeeklyAvg.to_csv('WeeklyAvg.csv')
CountyAvg.to_csv('CountyAvg.csv')
