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

def func(x, a, n): #definiere Winkelverteilung
    return a*np.power(np.cos(np.radians(x)), n)

#Bestimme zunaechst die Winkel zum Zenit:
#1-13: 15 Grad
#2-14: 30 Grad
#3-15: 45 Grad
#4-16: 60 Grad
#5-17: 75 Grad
#6-18: 90 Grad
#7-19: -75 Grad
#8-20: -60 Grad
#9-21: -45 Grad
#10-22: -30 Grad
#11-23: -15 Grad
#12-24: 0 Grad


#Bestimme Zaehlraten und entsprechende Winkelwerte
x = np.array([-75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90])
y = np.array([357, 1470, 1102, 3785, 4100, 3038, 4828, 3947, 2196, 1022, 350, 1])
y_err = np.sqrt(y) #Fehler durch Wurzel erhalten

#Anpassung an Kosinus hoch n Funktion
guess = np.array([4800, 2])

popt, pcov = curve_fit(func, x, y, p0=guess, sigma=y_err, absolute_sigma=True)

#Gebe Fit-Parameter aus
print("Parameter mit Beruecksichtigung des 0 Grad Datenpunkts")
print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))
print("----------")


#Ignoriere Einkerbung bei 0 Grad
xFit = np.array([-75, -60, -45, -30, -15, 15, 30, 45, 60, 75, 90])
yFit = np.array([357, 1470, 1102, 3785, 4100, 4828, 3947, 2196, 1022, 350, 1])
y_errFit = np.sqrt(yFit) #Fehler durch Wurzel erhalten

#Anpassung an Kosinus hoch n Funktion
guessOhneN = np.array([4800, 2])

poptOhneN, pcovOhneN = curve_fit(func, xFit, yFit, p0=guess, sigma=y_errFit, absolute_sigma=True)

#Gebe Fit-Parameter aus
print("Parameter ohne Beruecksichtigung des 0 Grad Datenpunkts")
print(poptOhneN)
print(np.sqrt(pcovOhneN[0][0]))
print(np.sqrt(pcovOhneN[1][1]))
print("----------")

x_plot = np.array([]) #erstelle Array zur genaueren Darstellung der Anpassungsfunktion
for i in range(1651):
    x_plot = np.append(x_plot, i*0.1-75)


#Berechnung des Chi-Quadrats mit Datenpunkt  bei  0: nach X =  sum(gemessen-erwartet)^2/erwartet)/N_ges
χ_sq_val_full = χ_sq(func, x, popt, y, y_err)
print("Full:\n\tχ² = {}".format(χ_sq_val_full))
dof = len(x) - len(popt)
print("\tχ²/dof = {}".format(χ_sq_val_full / dof))

print("------------------------------")

χ_sq_val_wo_0 = χ_sq(func, xFit, poptOhneN, yFit, y_errFit)
print("\ 0 :\n\tχ² = {}".format(χ_sq_val_wo_0))
dof = len(x) - len(popt)
print("\tχ²/dof = {}".format(χ_sq_val_wo_0 / dof))


#Plotte die Funktion und Anpassung
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = y_err, xerr= None, color='tab:red', fmt = '.', markersize=6, label = 'Messdaten',zorder=0)
plt.plot(x_plot, func(x_plot, popt[0], popt[1]), color='tab:blue', linewidth = 0.5, label = 'Anpassung mit Datenpunkt bei 0$^\\circ$')
plt.plot(x_plot, func(x_plot, poptOhneN[0], poptOhneN[1]), color='tab:green', linewidth = 0.5, label = 'Anpassung ohne Datenpunkt bei 0$^\\circ$')
plt.legend(loc='best')
plt.xlabel('Winkel in $^\\circ$')
plt.ylabel('Anzahl an Ereignissen')
plt.savefig('winkelverteilung.pdf', bbox_inches = "tight")
plt.show()
