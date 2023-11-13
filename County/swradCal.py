import pandas as pd
from scipy import stats
import math
import matplotlib.pyplot as plt
import numpy as np
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
for eco in prod1:
    print(k)
    k+=1
    print(eco)
    path = "./county"+str(eco)
    # creating df for productivity
    prod = pd.read_csv('./county_annual_productivity.csv')
    prod = prod[prod['county']==eco]
    # creating df for gridmet mean weekly
    climate = pd.read_csv('./county_gridmet_mean_weekly_ppt_et0_gddetc.csv')
    climate = climate[climate['county']==eco]
    # joining data frames on year 
    climateProd = pd.merge(climate,prod, on = ['county','year'])
    tavgAll = pd.DataFrame()
    # subset of tavg
    tavgL = climateProd[['year','Week_Number','swrad','productivity']]
    for y in range(1984,2022):
        tavg = tavgL[tavgL['year']==y]
        for i in range(1,27,2):
            tavg = tavg.reset_index(drop=True)
            rolling = tavg['swrad'].rolling(window=i,center=True).mean().fillna(-1).reset_index()
            rolling = rolling.rename(columns={'swrad': 'swrad'+str(-i)})
            roll = rolling['swrad'+str(-i)]
            tavg = tavg.join(roll)
        tavgAll = pd.concat([tavgAll,tavg])
    tavgAll.to_csv('TAVG_mean.csv')
    #print(tavgAll)
    res = []
    for w in list(tavgAll.Week_Number.unique()):
        tWeek = tavgAll[tavgAll['Week_Number']==w]
        ans = []
        ans.append(w)
        for column in tWeek.loc[:,~tWeek.columns.isin(['year','Week_Number','swrad','productivity'])]:
            ans.append(stats.pearsonr(tWeek['productivity'], tWeek[column])[0])
        res.append(ans)
    tcorr = pd.DataFrame(res, columns=['Week_Number','r-1','r-3','r-5','r-7','r-9','r-11','r-13','r-15','r-17',
        'r-19','r-21','r-23','r-25'])
    pvalues = []
    for w in list(tavgAll.Week_Number.unique()):
        tWeek = tavgAll[tavgAll['Week_Number']==w]
        ans = []
        ans.append(w)
        for column in tWeek.loc[:,~tWeek.columns.isin(['year','Week_Number','swrad','productivity'])]:
            ans.append(-math.log10(stats.pearsonr(tWeek['productivity'], tWeek[column])[1]))
        pvalues.append(ans)
    tpvalue = pd.DataFrame(pvalues, columns=['Week_Number','p-1','p-3','p-5','p-7','p-9','p-11','p-13','p-15','p-17',
        'p-19','p-21','p-23','p-25'])
    tcorr['max_col'] = tcorr[['r-1','r-3','r-5','r-7','r-9','r-11','r-13','r-15','r-17',
        'r-19','r-21','r-23','r-25']].abs().idxmax(axis = 1)
    tcorr['max_value'] = [tcorr.loc[row,col] for row, col in zip(tcorr.index, tcorr.max_col)]
    tcorr['p_value'] = [tpvalue.loc[row,col.replace('r','p')] for row, col in zip(tpvalue.index, tcorr.max_col)]
    tcorr.to_csv(path+'/swradcorr.csv')
# figure, axis = plt.subplots(2)

# axis[0].plot(tcorr['Week_Number'],tcorr['p_value'])
# axis[0].set(xlabel='swrad', ylabel='-logP')
# axis[0].set_xlim(left=1 ,right= 53)
# axis[0].set_ylim(bottom=0 ,top=10)
# axis[1].axhline(y=0.0, c="blue", linewidth=2, zorder=0)
# axis[1].plot(tcorr['Week_Number'],tcorr['max_value'])
# axis[1].set(xlabel='swrad', ylabel='r')
# axis[1].set_xlim(left=1 ,right= 53)
# axis[1].set_ylim(bottom=-1 ,top=1)
# plt.show()
#print(tcorr)
