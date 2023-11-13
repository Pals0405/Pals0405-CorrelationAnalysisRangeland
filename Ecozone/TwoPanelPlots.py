import pandas as pd
from scipy import stats
import math
import matplotlib as mat
import matplotlib.pyplot as plt
import numpy as np
# loading the datasets
prod = pd.read_csv('./ecozone_annual_productivity.csv')
prod1 = list(prod.ecozone.unique())
prod1.remove(38)
x = []
for i in range(1,53,10):
    x.append(i)
def window_size(colValue,weekNumber):
    if "-" in colValue:
        return str(weekNumber-(int(colValue[2:])//2))+"-"+str(weekNumber+(int(colValue[2:])//2))
    else:
        return str(weekNumber)+"-"+str(weekNumber+int(colValue[1:]))
for eco in prod1:
    path = "./ecozone"+str(eco)
    tavg = pd.read_csv(path+'/Tcorr.csv')
    dGDD = pd.read_csv(path+'/dayGDDcorr.csv')
    ppt = pd.read_csv(path+'/PPTcorr.csv')
    swrad = pd.read_csv(path+'/swradcorr.csv')
    shortGrass = pd.read_csv(path+'/Ref_ET_Shortgrasscorr.csv')
    tallGrass = pd.read_csv(path+'/Ref_ET_Tallgrasscorr.csv')
    # finding the week that shows maximum positive correlation
    # tavgValue = tavg['max_value'].max()
    # dGDDValue = dGDD['max_value'].max()
    #swradValue = swrad['max_value'].max()
    # pptValue = ppt['max_value'].max()
    # shortGrassVal = shortGrass['max_value'].max()
    # tallGrassVal = tallGrass['max_value'].max()
    # print(tavgValue, dGDDValue, swradValue, pptValue, shortGrassVal, tallGrassVal)
    # finding the week that shows maximum negative correlation
    # tavgValue = tavg['max_value'].min()
    # dGDDValue = dGDD['max_value'].min()
    # swradValue = swrad['max_value'].min()
    # pptValue = ppt['max_value'].min()
    # shortGrassVal = shortGrass['max_value'].min()
    #tallGrassVal = tallGrass['max_value'].min()
    # print(tavgValue, dGDDValue, swradValue, pptValue, shortGrassVal, tallGrassVal)
    # # maxpositive correlation 
    # posCorrRow = swrad[swrad['max_value']==swradValue]
    # print(posCorrRow)
    # posCorrRvalue = swradValue
    # posCorrPvalue = posCorrRow['p_value'].item()
    # posCorrWeek = posCorrRow['Week_Number'].item()
    # posCorrCol = posCorrRow['max_col'].item()
    # print(posCorrCol)
    # if "-" in posCorrCol:
    #     posCorrWindow = str(posCorrWeek-int(posCorrCol[2:]))+"-"+str(posCorrWeek)
    # else:
    #     posCorrWindow = str(posCorrWeek)+"-"+str(posCorrWeek+int(posCorrCol[1:]))

    # negCorrRow = tallGrass[tallGrass['max_value']==tallGrassVal]
    # print(negCorrRow)
    # negCorrRvalue = tallGrassVal
    # negCorrPvalue = negCorrRow['p_value'].item()
    # negCorrWeek = negCorrRow['Week_Number'].item()
    # negCorrCol = negCorrRow['max_col'].item()
    # print(negCorrCol)
    # if "-" in negCorrCol:
    #     negCorrWindow = str(negCorrWeek-int(negCorrCol[2:]))+"-"+str(negCorrWeek)
    # else:
    #     negCorrWindow = str(negCorrWeek)+"-"+str(negCorrWeek+int(negCorrCol[1:]))
    # # plots 
    tavg1 = tavg[tavg['p_value']>5.115]
    tweek, gweek, pweek, sweek, sgweek, tgweek = [],[],[],[],[],[]
    tpheight, gpheight, ppheight, spheight, sgpheight, tgpheight = [],[],[],[],[],[]
    trheight, grheight, prheight, srheight, sgrheight, tgrheight = [],[],[],[],[],[]
    for i in tavg1.index:
        window = window_size(tavg1['max_col'][i],tavg1['Week_Number'][i])
        tweek.append([tavg1['Week_Number'][i],window])
        tpheight.append(tavg1['p_value'][i])
        trheight.append(tavg1['max_value'][i])
    dGDD1 = dGDD[dGDD['p_value']>5.115]
    for i in dGDD1.index:
        window = window_size(dGDD1['max_col'][i],dGDD1['Week_Number'][i])
        gweek.append([dGDD1['Week_Number'][i],window])
        gpheight.append(dGDD1['p_value'][i])
        grheight.append(dGDD1['max_value'][i])
    ppt1 = ppt[ppt['p_value']>5.115]
    for i in ppt1.index:
        window = window_size(ppt1['max_col'][i],ppt1['Week_Number'][i])
        pweek.append([ppt1['Week_Number'][i],window])
        ppheight.append(ppt1['p_value'][i])
        prheight.append(ppt1['max_value'][i])
    swrad1 = swrad[swrad['p_value']>5.115]
    for i in swrad1.index:
        window = window_size(swrad1['max_col'][i],swrad1['Week_Number'][i])
        sweek.append([swrad1['Week_Number'][i],window])
        spheight.append(swrad1['p_value'][i])
        srheight.append(swrad1['max_value'][i])
    shortGrass1 = shortGrass[shortGrass['p_value']>5.115]
    for i in shortGrass1.index:
        window = window_size(shortGrass1['max_col'][i],shortGrass1['Week_Number'][i])
        sgweek.append([shortGrass1['Week_Number'][i],window])
        sgpheight.append(shortGrass1['p_value'][i])
        sgrheight.append(shortGrass1['max_value'][i])
    tallGrass1 = tallGrass[tallGrass['p_value']>5.115]
    for i in tallGrass1.index:
        window = window_size(tallGrass1['max_col'][i],tallGrass1['Week_Number'][i])
        tgweek.append([tallGrass1['Week_Number'][i],window])
        tgpheight.append(tallGrass1['p_value'][i])
        tgrheight.append(tallGrass1['max_value'][i])
    print(tweek, gweek, pweek, sweek, sgweek, tgweek)
    fig = plt.figure(figsize=(12,8))
    gs = fig.add_gridspec(2, 6, hspace=0.1, wspace=0)
    (ax1, ax2, ax3, ax4, ax5, ax6), (ax7, ax8, ax9, ax10, ax11, ax12) = gs.subplots(sharex='col', sharey='row')
    fig.suptitle('ecozone'+str(eco))
    ax1.plot(tavg['Week_Number'],tavg['p_value'])
    ax1.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    ax1.set_ylim(bottom=0,top=12)
    tavgWeeks = []
    for i in tweek:
        tavgWeeks.append(i[0])
    ax1.vlines(tavgWeeks,ymin=0,ymax=tpheight,colors='yellow',ls='--',label=tweek)
    ax1.legend(loc=(0,0), bbox_to_anchor=(-1,1.25),
            ncols=len(tweek),fontsize=7.5, fancybox=False, shadow=False)
    ax1.set(xlabel='TAVG', ylabel='-logP')
    ax1.set_xticks(x,labels=x) 
    ax2.plot(dGDD['Week_Number'],dGDD['p_value'])
    ax2.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    dgddWeeks = []
    for i in gweek:
        dgddWeeks.append(i[0])
    ax2.vlines(dgddWeeks,ymin=0,ymax=gpheight,colors='magenta',ls='--',label=gweek)
    ax2.legend(loc=(0,0), bbox_to_anchor=(-2, 1.15),
                ncols=len(gweek),fontsize=7.5)
    ax2.set(xlabel='dayGDD')
    ax2.set_xticks(x) 
    ax2.set_ylim(bottom=0,top=12)
    ax3.plot(ppt['Week_Number'],ppt['p_value'])
    ax3.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    pptWeeks = []
    for i in pweek:
        pptWeeks.append(i[0])
    ax3.vlines(pptWeeks,ymin=0,ymax=ppheight,colors='red',ls='--',label=pweek)
    ax3.legend(loc=(0,0), bbox_to_anchor=(-3,1.05),
            ncols=len(pweek),fontsize=5.9, fancybox=False, shadow=False)
    ax3.set(xlabel='PPT')
    ax3.set_xticks(x)
    ax3.set_ylim(bottom=0,top=12)
    ax4.plot(swrad['Week_Number'],swrad['p_value'])
    ax4.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    sradWeeks = []
    for i in sweek:
        sradWeeks.append(i[0])
    ax4.vlines(sradWeeks,ymin=0,ymax=spheight,colors='blue',ls='--',label=sweek)
    ax4.legend(loc=(0,0), bbox_to_anchor=(-4,-1.25),
            ncols=len(sweek) if len(sweek) > 0 else 1,fontsize=7.5, fancybox=False, shadow=False)
    ax4.set(xlabel='swrad')
    ax4.set_xticks(x) 
    ax4.set_ylim(bottom=0,top=12)
    ax5.plot(shortGrass['Week_Number'],shortGrass['p_value'])
    ax5.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    sgrassWeeks = []
    for i in sgweek:
        sgrassWeeks.append(i[0])
    ax5.vlines(sgrassWeeks,ymin=0,ymax=sgpheight,colors='cyan',ls='--',label=sgweek)
    ax5.legend(loc=(0,0), bbox_to_anchor=(-5, -1.30),
            ncol=len(sgweek) if len(sgweek)>0 else 1, fontsize=7.5, fancybox=False, shadow=False)
    ax5.set(xlabel='Ref_ET_Shortgrass')
    ax5.set_xticks(x) 
    ax5.set_ylim(bottom=0,top=12)
    ax6.plot(tallGrass['Week_Number'],tallGrass['p_value'])
    ax6.axhline(y=5.115, c="gray", linewidth=1, zorder=0)
    tgrassWeeks = []
    for i in tgweek:
        tgrassWeeks.append(i[0])
    ax6.vlines(tgrassWeeks,ymin=0,ymax=tgpheight,colors='green',ls='--',label=tgweek)
    ax6.legend(loc=(0,0), bbox_to_anchor=(-6, -1.35),
            ncol=len(tgweek) if len(tgweek)>0 else 1, fontsize=7.5, fancybox=False, shadow=False)
    ax6.set(xlabel='Ref_ET_Tallgrass')
    ax6.set_xticks(x) 
    ax6.set_ylim(bottom=0,top=12)
    ax7.plot(tavg['Week_Number'],tavg['max_value'])
    ax7.vlines(tavgWeeks,ymin=0,ymax=trheight,colors='yellow',ls='--')
    ax7.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax7.set(ylabel='r')
    ax7.set_ylim(bottom=-1 ,top=1)
    ax8.plot(dGDD['Week_Number'],dGDD['max_value'])
    ax8.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax8.vlines(dgddWeeks,ymin=0,ymax=grheight,colors='magenta',ls='--')
    ax8.set_ylim(bottom=-1 ,top=1)
    ax9.plot(ppt['Week_Number'],ppt['max_value'])
    ax9.vlines(pptWeeks,ymin=0,ymax=prheight,colors='red',ls='--')
    ax9.set_ylim(bottom=-1 ,top=1)
    ax9.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax10.plot(swrad['Week_Number'],swrad['max_value'])
    ax10.vlines(sradWeeks,ymin=0,ymax=srheight,colors='blue',ls='--')
    ax10.set_ylim(bottom=-1 ,top=1)
    ax10.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax11.plot(shortGrass['Week_Number'],shortGrass['max_value'])
    ax11.vlines(sgrassWeeks,ymin=0,ymax=sgrheight,colors='cyan',ls='--')
    ax11.set_ylim(bottom=-1 ,top=1)
    ax11.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax12.plot(tallGrass['Week_Number'],tallGrass['max_value'])
    ax12.vlines(tgrassWeeks,ymin=0,ymax=tgrheight,colors='green',ls='--')
    ax12.axhline(y=0.0, c="gray", linewidth=1, zorder=0)
    ax12.set_ylim(bottom=-1 ,top=1)
    plt.savefig('./Results/ecozone'+str(eco))
    #plt.show()
    for ax in fig.get_axes():
        ax.label_outer()