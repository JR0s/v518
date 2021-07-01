#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created June 2021

@author: jr
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from utils import χ_sq

def func(x, a, tau): #definiere Lebensdauerverteilung
    return a*np.exp(-x/tau)

#Anzahl an Start Signalen: 1156243
#Anzahl an Stopp Signalen: 2520522

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) #lese Daten aus Bild ab
y = np.array([941, 576, 369, 251, 164, 75, 56, 40, 16, 16]) - 3 #ziehe  Wert der  Zufallskoinzidenzen ab
y_err = np.sqrt(y) #Fehler durch Wurzel erhalten


#Anpassung an Lebensdauerverteilung
guess = np.array([1500, 2.2])

(popt, pcov) = curve_fit(func, x, y, p0=guess, sigma=y_err, absolute_sigma=True)

#Gebe Fit-Parameter aus
print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))
print("----------")

x_plot = np.array([]) #erstelle Array zur genaueren Darstellung der Anpassungsfunktion
for i in range(101):
    x_plot = np.append(x_plot, i*0.1)

# calculate χ² from the function + x values (for ŷ), y values and errors
χ_sq_val = χ_sq(func, x, popt, y, y_err)
print("χ² = {}".format(χ_sq_val))
dof = len(x) - len(popt)
print("χ²/dof = {}".format(χ_sq_val / dof))

#Plotte die Funktion und Anpassung
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = y_err, xerr= None, color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.plot(x_plot, func(x_plot, popt[0], popt[1]), color='tab:blue', linewidth = 0.5, label = 'Anpassung')
plt.legend(loc='best')
plt.xlabel('Zeit in ms')
plt.ylabel('Anzahl an Ereignissen')
# why set such a huge DPI? Just save as a PDF
plt.savefig('lebensdauer.pdf', bbox_inches = "tight")
plt.show()
