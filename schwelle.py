#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created June 2021

@author: jr
"""

import numpy as np
import matplotlib.pyplot as plt

#Werte für Diskriminator 1
schwelle1 = np.array([-50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150, -160, -170, -180, -190, -199])
d1d2mess1 = np.array([1449, 1442, 1395, 1386, 1408, 1311, 1383, 1381, 1365, 1297, 1303, 1313, 1230, 1280, 1319, 1256])
d11mess1 = np.array([99566, 82172, 67553, 55876, 44865, 36090, 29172, 23328, 18868, 15648, 12990, 11318, 9695, 8746, 7853, 7325])
d1d2mon1 = np.array([885, 931, 917, 930, 967, 892, 939, 940, 902, 875, 830, 900, 817, 872, 896, 846])
d11mon1 = np.array([37325, 37581, 37312, 37633, 36973, 36561, 36725, 36293, 36277, 36282, 36201, 36387, 35538, 35939, 35870, 35717])      


#print(len(d1d2mess1))
#print(len(d11mess1))
#print(len(d1d2mon1))
#print(len(d11mon1))

#Werte für Diskriminator 2
schwelle2 = np.array([-50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150, -160, -170, -180, -190, -200])
d1d2mess2 = np.array([1534, 1408, 1260, 1227, 1104, 1007, 907, 773, 604, 514, 338, 201, 114, 42, 22, 16])
d11mess2 = np.array([222335, 63472, 14796, 4419, 2801, 2333, 2008, 1590, 1211, 945, 571, 329, 187, 76, 50, 26])
d1d2mon2 = np.array([919, 872, 875, 941, 887, 906, 932, 918, 859, 965, 880, 933, 936, 896, 864, 901])
d11mon2 = np.array([2043, 2031, 1993, 2114, 2091, 2134, 2180, 2062, 2054, 2262, 2079, 2097, 2143, 2060, 2071, 2085])


#Gaußsche Fehlerfortpflanzung der Fehler
err1 = np.sqrt((np.sqrt(d1d2mess1)/d1d2mon1)**2 + ((np.sqrt(d1d2mon1)*d1d2mess1)/d1d2mon1**2)**2)

err2 = np.sqrt((np.sqrt(d11mess1)/d11mon1)**2 + ((np.sqrt(d11mon1)*d11mess1)/d11mon1**2)**2)

err3 = np.sqrt((np.sqrt(d1d2mess2)/d1d2mon2)**2 + ((np.sqrt(d1d2mon2)*d1d2mess2)/d1d2mon2**2)**2)

#Plot 1
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.axvline(x=-155, ymin=0.0, ymax=2.5,color="grey",label="Schwelle",  zorder=0) #Schwelle einzeichnen
plt.errorbar(schwelle1, d1d2mess1/d1d2mon1, yerr = err1, xerr= None,color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.legend(loc='best')
plt.xlabel('Schwelle in mV', fontsize = 20)
plt.ylabel('Verhältnis Zählrate', fontsize = 20)
plt.savefig('schwelle_szinti1_falsch.png', dpi=1000, bbox_inches = "tight")
plt.show()

#Plot 1 mit anderen y-Werten: 
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.axvline(x=-155, ymin=0.0, ymax=2.5, color="grey",label="Schwelle",  zorder=0) #Schwelle einzeichnen
plt.errorbar(schwelle1, d11mess1/d11mon1, yerr = err2, xerr= None,color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.legend(loc='best')
plt.xlabel('Schwelle in mV', fontsize = 20)
plt.ylabel('Verhältnis Zählrate', fontsize = 20)
plt.savefig('schwelle_szinti1_anders.png', dpi=1000, bbox_inches = "tight")
plt.show()


#Plot 2
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.axvline(x=-85, ymin=0.0, ymax=1.75, color="grey",label="Schwelle",  zorder=0) #Schwelle einzeichnen
plt.errorbar(schwelle2, d1d2mess2/d1d2mon2, yerr = err3, xerr= None,color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.legend(loc='best')
plt.xlabel('Schwelle in mV', fontsize = 20)
plt.ylabel('Verhältnis Zählrate', fontsize = 20)
plt.savefig('schwelle_szinti2.png', dpi=1000, bbox_inches = "tight")
plt.show()

