#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created June 2021

@author: jr
"""

import numpy as np
import matplotlib.pyplot as plt

#Werte für Diskriminator 12
schwelle1 = np.array([-50, -55, -60, -65, -70, -75, -80, -85, -90, -95, -100, -105, -110,  -115, -120,  -125, -130, -135, -140, -145, -150, -155, -160, -165, -170, -175, -180, -185, -190, -195, -200])
orsignal = np.array([145417, 162735,  176293, 186093, 193261, 196411, 197458, 195789, 198485, 201353, 201508, 200998, 201972, 202966, 203828, 203720, 203877, 204121, 205018, 205112, 204869, 205846, 205010, 204765, 204302, 204129, 203744,  203072, 202834, 202661,  202095])    
koinz = np.array([98, 82, 73, 73, 73, 78, 70, 74, 73, 61, 67, 51, 55, 55, 47, 44, 49, 41, 49, 29, 42, 28, 32, 25, 31, 27, 21, 25, 20, 16, 12])
d12 = np.array([2674, 2371,  2158, 1987, 1824, 1734, 1501, 1429, 1284, 1218, 1147, 1068, 933, 928, 881, 769, 731, 712, 681, 650, 601,  558, 510,  530,  462, 430, 389, 378, 391, 327, 305])
d25 = np.array([6417, 6381, 6456, 6374, 6374, 6582, 6425, 6696, 6492, 6644, 6562, 6462, 6459, 6479,  6485, 6435, 6537, 6491, 6561, 6524, 6467, 6526,  6415, 6485, 6566, 6563, 6539, 6452, 6661, 6549, 6412])
koinz_err = np.sqrt(koinz)

re = np.zeros(len(koinz))


#Re-Bin das Array
schwelleRe =  np.array([-50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150, -160, -170, -180, -190])
koinzRe = np.array([98 + 82, 73 + 73, 73 + 78, 70 + 74, 73 + 61, 67 + 51, 55 + 55, 47 + 44, 49 + 41, 49 + 29, 42 + 28, 32 + 25, 31 + 27, 21 + 25, 20 + 16])
koinzRe_err = np.sqrt(koinzRe)



#Plot 1
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.axvline(x=-120, ymin=0.0, ymax=2.5,color="grey",label="Schwelle",  zorder=0) #Schwelle einzeichnen
plt.errorbar(schwelle1, koinz, yerr = koinz_err, xerr= None,color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=1)
plt.legend(loc='best')
plt.xlabel('Schwelle in mV', fontsize = 20)
plt.ylabel('Anzahl Koinzidenzen', fontsize = 20)
plt.savefig('schwelle_szinti1.png', dpi=1000, bbox_inches = "tight")
plt.show()


#Plot 1 mit Re-Bin
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.axvline(x=-120, ymin=0.0, ymax=2.5,color="grey",label="Schwelle",  zorder=0) #Schwelle einzeichnen
#plt.errorbar(schwelle1, koinz, yerr = None, xerr= None,color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.errorbar(schwelleRe, koinzRe, yerr = koinzRe_err, xerr= None,color='tab:blue', fmt = '.', markersize=6, label = 'Messdaten',zorder=1)
plt.legend(loc='best')
plt.xlabel('Schwelle in mV', fontsize = 20)
plt.ylabel('Anzahl Koinzidenzen', fontsize = 20)
plt.savefig('schwelle_szinti1_Re.png', dpi=1000, bbox_inches = "tight")
plt.show()
