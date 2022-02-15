# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:20:01 2021

@author: PSClo
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
import pandas as pd
import glob
#%%
angle, count = np.loadtxt('H:/x-ray/initial_meas/Mo_refbeam1.txt', skiprows = 1, unpack = True)
angle2, count2 = np.loadtxt('H:/x-ray/initial_meas/NaClcrystal_initial.txt', skiprows = 1, unpack = True)

kangle, kcount = np.loadtxt('H:/x-ray/kabsorption.txt', skiprows = 1, unpack = True)

#Ag data

agangle, agcount=  np.loadtxt('H:/x-ray/foil_filters/Ag_foildata.txt', skiprows = 1, unpack = True)


# Finding peaks

#Kalpha peak 1
anglepeak_index1 = np.where(kcount == 3644.9)
kalpha_1 = kangle[anglepeak_index1[0][0]]

#Kalpha peak 2
akcountreduced = kcount[100:110]
aidx_2 = np.where(kcount == max(akcountreduced))
kalpha_2 = kangle[aidx_2]

#Kalpha peak 3
akcountreduced2 = kcount[170:190]
aidx_3 = np.where(kcount == max(akcountreduced2))
kalpha_3 = kangle[aidx_3]

#Kbeta peak 1
kcountreduced = kcount[0:27]
idx_1 = np.where(kcount == max(kcountreduced))
kbeta_1 = kangle[idx_1]

#Kbeta peak 2
kcountreduced2 = kcount[84:93]
idx_2 = np.where(kcount == max(kcountreduced2))
kbeta_2 = kangle[idx_2]

#Kbeta peak 3
kcountreduced3 = kcount[151:159]
idx_3 = np.where(kcount == max(kcountreduced3))
kbeta_3 = kangle[idx_3]





#Zirconium foil data
Zrangle, Zrcount = np.loadtxt('H:/x-ray/foil_filters/Zrfoildata.txt', skiprows = 1, unpack = True) #10s
Zrangle_1s, Zrcount_1s = np.loadtxt('H:/x-ray/foil_filters/Zr_1s.txt', skiprows = 1, unpack = True)
Zrangle30, Zrcount30 = np.loadtxt('H:/x-ray/foil_filters/Zr_30s_data.txt', skiprows = 1, unpack = True) #30s
Zr_wavel = 4*282.01e-12*np.sin(np.radians(Zrangle))
#Aluminium foil data
Alangle, Alcount = np.loadtxt('H:/x-ray/foil_filters/al_foildata.txt', skiprows = 1, unpack = True) 
#Indium foil data
Inangle, Incount = np.loadtxt('H:/x-ray/foil_filters/In_foildata.txt', skiprows = 1, unpack = True) 

#Mo foil data
Moangle, Mocount = np.loadtxt('H:/x-ray/foil_filters/Mo_foildata.txt', skiprows = 1, unpack = True)
Moangle30, Mocount30 = np.loadtxt('H:/x-ray/foil_filters/Mo_foildata_30s.txt', skiprows = 1, unpack = True)
#Copper foil data
Cuangle, Cucount = np.loadtxt('H:/x-ray/foil_filters/Cu_foildata.txt', skiprows = 1, unpack = True)
#Ag foil data
Agangle, Agcount = np.loadtxt('H:/x-ray/foil_filters/Ag_foildata.txt', skiprows = 1, unpack = True)
#Refbeamdata
refbangle, refbcount = np.loadtxt('H:/x-ray/foil_filters/kabsorb_ref.txt', skiprows = 1, unpack = True)
refbangle_1s, refbcount_1s = np.loadtxt('H:/x-ray/foil_filters/1s_kabsorb_ref.txt', skiprows = 1, unpack = True)

#Transmission ratios
#Transmission ratio I_Zr/I0 10 second run
trans_Zr = Zrcount/kcount
wavel_a = 2*282.01e-12*np.sin(np.radians(kangle))

#Transmission Zirconium 30 second run
trans30_Zr = Zrcount30/kcount

#Transmission ratio for Al
trans_Al = Alcount/kcount

#Transmission ratio for In
trans_In = Incount/kcount

#Transmission Mo 30 and 10
trans_Mo = Mocount/refbcount
trans30_Mo = Mocount30/refbcount[0:len(Mocount30)]

#Transmission ratio Cu, Ag
trans_Cu = Cucount[0:len(refbcount)]/refbcount
trans_Ag = Agcount/refbcount
##############################################################


# Cu tube
df = pd.read_csv('H:/x-ray/Cu_tube/straight_through.txt', header = 0)
cutube_ref_angle, cutube_ref_count = np.loadtxt('H:/x-ray/Cu_tube/straight_through.txt', skiprows = 1, unpack = True)
ni_cutube_angle, ni_cutube_count = np.loadtxt('H:/x-ray/Cu_tube/Ni_straight_through.txt', skiprows = 1, unpack = True)
nifilterCU_angle, nifilterCU_count = np.loadtxt('H:/x-ray/Cu_tube/highres_powderrun.txt', skiprows = 1, unpack = True) 
CUst_angle, CUst_count = np.loadtxt('H:/x-ray/Cu_tube/straight_throughCU.txt', skiprows = 1, unpack = True)
##############################################################

#NaCl powder results
highres_angle, highres_count = np.loadtxt('H:/x-ray/Cu_tube/highres_powderrun.txt', unpack = True, skiprows = 1)
powderangle, powdercount  = np.loadtxt('H:/x-ray/Cu_tube/NaCl_powder_table_i.txt', unpack = True, skiprows = 1)
peak1_angle, peak1_count  = np.loadtxt('H:/x-ray/Cu_tube/first_peak_res_table.txt', unpack = True, skiprows = 1)
##############################################################

#Bremmstrahlung radiation 
br35_Zr_angle, br35_Zr_count = np.loadtxt('H:/x-ray/Cu_tube/NaCl_Zr_br_table_35.txt', unpack = True, skiprows = 1)
##############################################################


# Xray fluorescence data - known elements

pathknown = 'H:/x-ray/fluor/csvdata/'

dfk = pd.read_csv(pathknown + 'Ag_90_120s.csv')
Cu_fl_120s = pd.read_csv(pathknown + 'Cu_90_120s.csv')
Cu_fl_480s = pd.read_csv(pathknown + 'Cu_90_480s.csv')
Cu_fl_900s = pd.read_csv(pathknown + 'Cu_90_900s.csv')
Fe_fl_120s = pd.read_csv(pathknown + 'Fe_90_120s.csv')
Mo_fl_120s = pd.read_csv(pathknown + 'Mo_90_120s.csv')
Ni_fl_120s = pd.read_csv(pathknown + 'Ni_90_120s.csv')
Ti_fl_120s = pd.read_csv(pathknown + 'Ti_90_120s.csv')
Zr_fl_120s = pd.read_csv(pathknown + 'Zr_90_120s.csv')

dfk = dfk.join(Ni_fl_120s['count(Ni_90_120s)'])
dfk = dfk.join(Fe_fl_120s['count(Fe_90_120s)'])
dfk = dfk.join(Cu_fl_120s['count(Cu_90_120s)'])
dfk = dfk.join(Cu_fl_900s['count(Cu_90_900s)'])
dfk = dfk.join(Cu_fl_480s['count(Cu_90_480s)'])
dfk = dfk.join(Zr_fl_120s['count(Zr_90_120s)'])
dfk = dfk.join(Mo_fl_120s['count(Mo_90_120s)'])
dfk = dfk.join(Ti_fl_120s['count(Ti_90_120s)'])


#Unknown materials data
pathunknown = 'H:/x-ray/unknown/csvdata/'
dfu = pd.read_csv('H:/x-ray/unknown/csvdata/brassdata.csv')
dfag = pd.read_csv('H:/x-ray/unknown/csvdata/silverblockdata.csv')
dfCU = pd.read_csv(pathunknown + 'copperlikedata.csv')
dfgrey3 = pd.read_csv(pathunknown + 'grey3data.csv')
dfgrey5 = pd.read_csv(pathunknown + 'grey5data.csv')
dfgrey5_600s = pd.read_csv(pathunknown + 'grey5_600sdata.csv')
dftransblock = pd.read_csv(pathunknown + 'transblockdata.csv')

dfu = dfu.join(dfag['count(silverblock)'])
dfu = dfu.join(dfCU['count(copperlike)'])
dfu = dfu.join(dfgrey3['count(grey3)'])
dfu = dfu.join(dfgrey5['count(grey5)'])
dfu = dfu.join(dfgrey5_600s['count(grey5_600s)'])
dfu = dfu.join(dftransblock['count(transblock)'])












