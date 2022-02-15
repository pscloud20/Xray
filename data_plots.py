# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:20:18 2021

@author: PSClo
"""
import matplotlib.pyplot as plt
import xlsxwriter
import numpy as np
import io
import pyxll
from scipy import signal
import xray_data
#%%
params = {
    'font.family' : 'serif',
    'font.size': 13.5,
    'figure.figsize':  [8.8, 8.8/1.618],
    'axes.grid': True,
    'legend.loc' :'best',
    'legend.fontsize': 10,
    'legend.handlelength':2,

}

plt.rcParams.update(params)
#%%

plt.plot(kangle, kcount)
plt.xlabel('Angle')
plt.ylabel('Count (s$^-1$)')
plt.title('K-alpha and K-beta energies of X-ray source')


#%% Absorption of K-beta graph
plt.plot(Zr_wavel, kcount, 'black', label = 'K-$\\alpha$ and K-$\\beta$ peaks of Mo X-ray source')
plt.plot(Zr_wavel, trans_Zr*6000, 'red', linestyle = '--', label = 'Transmission ratio')
plt.title('K-$\\alpha$ and K-$\\beta$ absorption of Mo source')
plt.xlabel('Wavelength (m)')
plt.ylabel('counts / s')
plt.legend()
plt.ylim(0, 4500)
plt.show()



#%%
plt.plot(Zr_wavel, Zrcount, 'darkblue', label = 'K-$\\beta$ filtered spectrum')
plt.plot(Zr_wavel, trans_Zr*6000, 'red', linestyle = '--', label = 'Transmission ratio')
plt.plot(Zr_wavel, kcount, 'black', label = 'K-$\\alpha$ and K-$\\beta$ peaks of Mo X-ray source')

plt.xlabel('Wavelength')
plt.ylim(0, 4500)
plt.ylabel('Count $s^-1$')
plt.title('K-$\\alpha$ and K-$\\beta$ absorption of Mo source')
plt.legend()

#%% Reference beam plot

plt.plot(refbangle, refbcount, label = '10s data')
#plt.plot(refbangle_1s, refbcount_1s, label = '1s data')
plt.xlabel('Angle/degrees')
plt.ylabel('Count/s')

plt.title('Reference beam K-absorption')
#%% Zr plot
plt.plot(Zrangle, Zrcount)
plt.xlabel('Angle/degrees')
plt.ylabel('Count/s')
plt.title('Zirconium (Zr) foil K-absorption')



#%% Molybdenum plot
plt.plot(Moangle, Mocount, 'green')
#plt.plot(Moangle30, Mocount30, 'yellow')
plt.xlabel('Angle/degrees')
plt.ylabel('Count/s')
plt.title('Molybdenum (Mo) foil K-absorption')


#%% Cu plot
plt.plot(Cuangle, Cucount, 'orange')
plt.xlabel('Angle/degrees')
plt.ylabel('Count/s')
plt.title('Copper (Cu) foil K-absorption')


#%% Ag plot
plt.plot(Agangle, Agcount, 'darkorchid')
plt.xlabel('Angle/degrees')
plt.ylabel('Count/s')
plt.title('Silver (Ag) foil K-absorption')


#%% Transmission coefficient plot for Zr
plt.plot(wavel_a, trans_Zr, label = '10s data')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of Zr vs wavelength')
plt.plot(wavel_a, trans30_Zr, 'red', label = '30s data')
plt.legend()



    
#%% Transmission coefficient plot for Al
plt.plot(wavel_a, trans_Al, 'grey')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of Al vs wavelength')


#%% Transmission coefficient plot for In
plt.plot(wavel_a, trans_In, 'yellow')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of In vs wavelength')



#%% Transmission coefficient plot for Mo
plt.plot(wavel_a, trans_Mo, 'green', label = '10s data')
plt.plot(wavel_a[0:len(trans30_Mo)], trans30_Mo, label = '30s data')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of Mo vs wavelength')
plt.legend()


#%% Transmission coefficient plot for Cu
plt.plot(wavel_a, trans_Cu, 'orange')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of Cu vs wavelength')


#%% Transmission coefficient plot for Ag
plt.plot(wavel_a, trans_Ag, 'darkorchid')
plt.xlabel('Wavelength (m)')
plt.ylabel('Transmission Coefficient')
plt.title('Measuring transmission coefficient of Ag vs wavelength')



#%% Copper x-ray tube plots

plt.plot(cutube_ref_angle, cutube_ref_count, 'red', label = 'Cu tube ref. beam')
plt.plot(ni_cutube_angle, ni_cutube_count, 'grey', label ='Ni filter copper tube x-ray')
plt.plot(angle, count, 'black', label = 'Ref. beam Mo tube')
plt.xlabel('Angle/degrees')
plt.ylabel('Count s$^-1$')
plt.title('Comparison of Mo and Cu X-ray tubes')
plt.show()
error_mo = np.sqrt(count)

#%% NaCl powder analysis highres (40s), powder_angle (10s), peak_1 (60s for range around first peak)
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(highres_angle, highres_count, label = '40s run')
ax1.legend()
ax2.plot(powderangle, powdercount, 'red',label = '10s run')
ax2.legend()
#%%NaCl powder analysis highres (40s), powder_angle (10s), peak_1 (60s for range around first peak)
plt.plot(highres_angle, highres_count, label = '40s run')
plt.plot(powderangle, powdercount, label = '10s run')
plt.plot(peak1_angle, peak1_count, label = 'High res data of first peak')
plt.plot(nifilterCU_angle, nifilterCU_count, label = 'Ni filter')

#%% Comparison of Cu and Mo tube
plt.plot(CUst_angle, CUst_count)
plt.plot(angle, count, 'green')
plt.xlabel('Angle/degrees')
plt.ylabel('Count s$^-1$')





#%% Known elements plots

savepath_k = 'H:/x-ray/plots/known_elements_plots/'

plt.plot(dfk['energy'], dfk['count(Ag_90_120s)'], label = 'Ag (47)')
plt.legend()
plt.title('Ag (Z = 47) fluorescence peak')
plt.savefig(savepath_k + 'Ag_120s.png')
plt.show()

plt.plot(dfk['energy'], dfk['count(Ni_90_120s)'], label = 'Ni (28)')
plt.legend()
plt.title('Ni (Z = 28) fluorescence peak')
plt.savefig(savepath_k + 'Ni_120s.png')
plt.show()

plt.plot(dfk['energy'], dfk['count(Fe_90_120s)'], label = 'Fe (26)')
plt.legend()
plt.title('Fe (Z = 26) fluorescence peak')
plt.savefig(savepath_k + 'Fe_120s.png')
plt.show()

plt.plot(dfk['energy'], dfk['count(Cu_90_120s)'], label = 'Cu (29)')
plt.legend()
plt.title('Cu (Z = 29) fluorescence peak')
plt.savefig(savepath_k + 'Cu_120s.png')
plt.show()

# =============================================================================
# plt.plot(dfk['energy'], dfk['count(Cu_90_900s)'], label = 'Cu_900s')
# plt.legend()
# plt.savefig(savepath_k + 'Cu_900s.png')
# plt.show()
# 
# plt.plot(dfk['energy'], dfk['count(Cu_90_480s)'], label = 'Cu_480s')
# plt.legend()
# plt.title('Zr (Z = 40) fluorescence peak')
# plt.savefig(savepath_k + 'Cu_480s.png')
# plt.show()
# =============================================================================

plt.plot(dfk['energy'], dfk['count(Zr_90_120s)'], label = 'Zr(40)')
plt.legend()
plt.title('Zr (Z = 40) fluorescence peak')
plt.savefig(savepath_k + 'Zr_120s.png')
plt.show()

plt.plot(dfk['energy'], dfk['count(Mo_90_120s)'], label = 'Mo (42)')
plt.legend()
plt.title('Mo (Z = 42) fluorescence peak')
plt.savefig(savepath_k + 'Mo_120s.png')
plt.show()

plt.plot(dfk['energy'], dfk['count(Ti_90_120s)'], label = 'Ti (22)')
plt.legend()
plt.title('Ti (Z = 22) fluorescence peak')
plt.savefig(savepath_k + 'Ti.png')
plt.show()

#%% Singular plot of all known element xray spectra
#dfk['energy'] = dfk['energy']*74.587/1000

plt.plot(dfk['energy'], dfk['count(Ti_90_120s)'], label = 'Ti (4.7 keV)')
plt.plot(dfk['energy'], dfk['count(Fe_90_120s)'], label = 'Fe (6.49 keV)')
plt.plot(dfk['energy'], dfk['count(Cu_90_120s)'], label = 'Cu (8.06 keV)')
plt.plot(dfk['energy'], dfk['count(Ni_90_120s)'], label = 'Ni (7.46 keV)')
plt.plot(dfk['energy'], dfk['count(Zr_90_120s)'], label = 'Zr (15.59 keV)')
plt.plot(dfk['energy'], dfk['count(Mo_90_120s)'], label = 'Mo (17.08 keV)')
plt.plot(dfk['energy'], dfk['count(Ag_90_120s)'], label = 'Ag (21.41 keV)')

plt.annotate("Ti (22)", (63/1000*74.5873, 96))
plt.plot(63*74.587/1000,96,'ko')
plt.annotate("Fe (26)", (87*74.587/1000, 451))
plt.plot(87*74.587/1000,451,'ko')
plt.annotate("Cu (29)", (108*74.587/1000, 665))
plt.plot(108*74.587/1000, 665, 'ko')
plt.annotate("Ni (28)", (100*74.587/1000, 634))
plt.plot(100*74.587/1000, 634, 'ko')
plt.annotate("Zr(40)", (209*74.587/1000, 257))
plt.plot(209*74.587/1000, 257, 'ko')
plt.annotate("Mo (42)", (229*74.587/1000, 155))
plt.plot(229*74.587/1000, 155, 'ko')
plt.annotate("Ag (47)", (287*74.587/1000, 46))
plt.plot(287*74.587/1000, 46, 'ko')
plt.xlim(0)
plt.ylim(0)
plt.title('X-ray spectra of certain elements')
plt.xlabel('Energy (keV)')
plt.ylabel('Count /s')
plt.legend()




#%% Unknown materials plots

savepath = 'H:/x-ray/plots/unknownplots/'

plt.plot(dfu['energy'], dfu['count(brass)'], 'gold', label = 'brass')
plt.legend()
plt.savefig(savepath + 'Brass.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(silverblock)'], 'silver', label = 'Silver block')
plt.legend()
plt.savefig(savepath + 'Silver block.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(copperlike)'], 'orange', label = 'Copper-like block')
plt.legend()
plt.savefig(savepath + 'Copperlike.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(grey3)'], 'grey', label = 'Grey 3')
plt.legend()
plt.savefig(savepath + 'Grey 3.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(grey5)'], 'dimgrey', label = 'Grey 5')
plt.legend()
plt.savefig(savepath + 'grey5.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(grey5_600s)'], 'black', label = 'Grey 5 600s run')
plt.legend()
plt.savefig(savepath + 'grey5_600s.png')
plt.show()
plt.plot(dfu['energy'], dfu['count(transblock)'], 'red', label = 'Transparent block')
plt.legend()
plt.savefig(savepath + 'Transparent block.png')
plt.show()

#%%
#dfu['energy'] = dfu['energy']*74.587/1000

#plt.plot(dfu['energy'], dfu['count(brass)'], 'gold', label = 'brass (E = 8.06 keV)')
plt.plot(dfu['energy'], dfu['count(silverblock)'], 'silver', label = 'Silver block (E = 7.98 keV)')
#plt.plot(dfu['energy'], dfu['count(copperlike)'], 'orange', label = 'Copper-like block (E = 8.06 keV)')
plt.plot(dfu['energy'], dfu['count(grey3)'], 'grey', label = 'Grey 3 (E = 4.77 keV)')
plt.plot(dfu['energy'], dfu['count(grey5)'], 'dimgrey', label = 'Grey 5 (E = 24.31 keV')
#plt.plot(dfu['energy'], dfu['count(grey5_600s)'], 'black', label = 'Grey 5 600s run')
plt.plot(dfu['energy'], dfu['count(transblock)'], 'red', label = 'Transparent block (16.5583 keV)')

plt.legend()

plt.xlabel('Energy (keV)')
plt.ylabel('Counts /s')

plt.annotate("Silver block", (7.98081, 36))
plt.plot(7.98081, 36, 'bo')

#plt.annotate("Copper colour block", (8.0554, 466))
#plt.plot(8.0554, 466, 'bo')

plt.annotate("Grey 3", (4.77357, 79))
plt.plot(4.77357, 79, 'bo')

plt.annotate("Grey 5", (24.3154, 28))
plt.plot(24.3154, 28, 'bo')

plt.annotate("Trans. block", (16.5583, 18))
plt.plot(16.5583, 18, 'bo')

plt.title('X-ray fluorescence of unknown materials')
plt.ylim(0)
plt.xlim(0)

plt.show()



#%%
plt.plot(dfu['energy'], dfu['count(copperlike)'], 'orange', label = 'Copper-like block (E = 8.06 keV)')
plt.annotate("Copper-like", (8.0554, 466))
plt.plot(8.0554, 466, 'bo')
plt.legend()
plt.ylim(0)
plt.xlim(0)
plt.title('Copper-coloured block x-ray fluorescence')
plt.show()

plt.plot(dfu['energy'], dfu['count(brass)'], 'gold', label = 'brass (E = 8.06 keV)')
plt.annotate("Brass", (8.0554, 466))
plt.plot(8.0554, 466, 'bo')
plt.legend()
plt.ylim(0)
plt.xlim(0)
plt.title('Brass block x-ray fluorescence')
plt.show()



#%%
plt.plot(dfu['energy'], dfu['count(grey5)'], 'dimgrey', label = 'Grey 5 (E = 24.31 keV')
plt.show()
plt.plot(dfu['energy'], dfu['count(grey5_600s)'], 'black', label = 'Grey 5 600s run')
plt.show()


#%%
plt.plot(dfu['energy'], dfu['count(brass)'], 'dimgrey', label = 'Grey 5 (E = 24.31 keV')


