#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created June 2021

@author: jr
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, tau): #definiere Lebensdauerverteilung
    return a*np.exp(-x/tau)


#Anzahl an Start Signalen: 1156243
#Anzahl an Stopp Signalen: 2520522

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #lese Daten aus Bild ab
y = np.array([941, 576, 369, 251, 164, 75, 56, 40, 16, 16]) - 3 #ziehe  Wert der  Zufallskoinzidenzen ab
y_err = np.sqrt(y) #Fehler durch Wurzel erhalten


#Anpassung an Lebensdauerverteilung
guess = np.array([1500, 2.2])

popt, pcov = curve_fit(func, x, y, p0=guess, sigma=y_err, absolute_sigma=True)

#Gebe Fit-Parameter aus
print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))
print("----------")

x_plot = np.array([]) #erstelle Array zur genaueren Darstellung der Anpassungsfunktion
for i in range(101):
    x_plot = np.append(x_plot, i*0.1)
    

#Berechnung des Chi-Quadrats: nach X =  sum(gemessen-erwartet)^2/erwartet)/N_ges

chi2 = 0
yer = 0

for i in range(len(x)):
    yer = func(x[i], popt[0], popt[1])
    chi2 =  chi2 + (y[i] - yer)**2/yer/2474

print(chi2)

    

#Plotte die Funktion und Anpassung
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = y_err, xerr= None, color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.plot(x_plot, func(x_plot, popt[0], popt[1]), color='tab:blue', linewidth = 0.5, label = 'Anpassung')
plt.legend(loc='best')
plt.xlabel('Zeit in ms', fontsize = 20)
plt.ylabel('Anzahl an Ereignissen', fontsize = 20)
plt.savefig('lebensdauer.png', dpi=1000, bbox_inches = "tight")
plt.show()

