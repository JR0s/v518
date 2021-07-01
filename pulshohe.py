#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created June 2021

@author: jr
"""

#Dauer der Messung: 511053 s
#Anzahl an Ereignissen: 14322

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from utils import χ_sq

def func(x, a, mu, sigma): #naehere Landau-Verteilung durch folgenden Ausdruck an
    lambd = (x-mu)/sigma
    return a/(np.sqrt(2*np.pi))*np.exp(-0.5*(lambd+np.exp(-lambd)))

def func2(x, a, mu, sigma):  #Gauß-Verteilung
    return a/(np.sqrt(2*np.pi*sigma**2))*np.exp(-((x-mu)**2)/(2*sigma**2))



lines = np.array([]) #definiere leere Arrays zum Daten schreiben
x = np.array([])
y = np.array([])
y_err = np.array([])

file = open("alpha_211.txt", "r", encoding='windows-1252') #importiere Daten aus txt-Datei

lines = file.readlines()

lines = [item.replace('\n', '') for item in lines] #verarbeite Daten zu sinnvollen Arrays
lines = [item.replace('\t', ',') for item in lines]


for i in range(len(lines)):
    text = lines[i]
    head, sep, tail = text.partition(',')
    x = np.append(x,float(head))
    y = np.append(y,float(tail))


y_err = np.sqrt(y) #erzeuge y-Fehler durch Wurzel nehmen

#Plotte die Funktion der gesamnten Daten (einbegriffen des Rauschens)
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = y_err, xerr= None,color='tab:red', fmt = '.', markersize=1, label = 'Messdaten',zorder=0)
plt.legend(loc='best')
plt.xlabel('Kanäle')
plt.ylabel('Anzahl der Ereignisse N')
plt.savefig('alpha_211_fit.pdf', bbox_inches = "tight")
plt.show()

x = x[90:1000] #schraenke Messdaten auf interessantes Intervall ein
y = y[90:1000] #Stoerung nahe Kanal 0, sowie Nullen bei Kanaelen >800 werden rausgenommen
y_err = y_err[90:1000]

#Anpassung an Landau-Verteilung
guess = np.array([1, 320, 30])
popt, pcov = curve_fit(func, x, y, p0=guess, sigma=None, absolute_sigma=True)

#Gebe erhaltene Fit-Parameter aus
print(popt)
print(np.sqrt(pcov[0][0]))
print(np.sqrt(pcov[1][1]))
print(np.sqrt(pcov[2][2]))
print("----------")

#Anpassung an Gauß-Verteilung
guess1 = np.array([320, 70, 40])
popt1, pcov1 = curve_fit(func2, x, y, p0=guess1, sigma=None, absolute_sigma=False)

#Gebe erhaltene Fit-Parameter aus
print(popt1)
print(np.sqrt(pcov1[0][0]))
print(np.sqrt(pcov1[1][1]))
print(np.sqrt(pcov1[2][2]))
print("----------")

#Berechnung des Chi-Quadrats Landau: nach X =  sum(gemessen-erwartet)^2/erwartet)/N_ges
# fix y errors. If 0 set to 1
y_err[y_err == 0.0] = 1.0
χ_sq_landau = χ_sq(func, x, popt, y, y_err)
print("Landau:\n\tχ² = {}".format(χ_sq_landau))
dof = len(x) - len(popt)
print("\tχ²/dof = {}".format(χ_sq_landau / dof))

print("---")

χ_sq_gauss = χ_sq(func2, x, popt, y, y_err)
print("Gauß:\n\tχ² = {}".format(χ_sq_gauss))
dof = len(x) - len(popt)
print("\tχ²/dof = {}".format(χ_sq_gauss / dof))


#Plotte die Funktion des eingeschraenkten Intervalls sowie den Fit mit y-Fehlern
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = y_err, xerr= None,color='tab:red', fmt = '.', markersize=1, label = 'Messdaten',zorder=0)
plt.plot(x, func(x, popt[0], popt[1], popt[2]), color='tab:blue', linewidth = 0.5, label = 'Landau-Verteilung')
plt.plot(x, func2(x, popt1[0], popt1[1], popt1[2]), color='tab:green', linewidth = 0.5, label = 'Gauß-Verteilung')
plt.legend(loc='best')
plt.xlabel('Kanäle')
plt.ylabel('Anzahl der Ereignisse N')
plt.savefig('alpha_211_fit_intervall_fehler.pdf', bbox_inches = "tight")
plt.show()

#Plotte die Funktion des eingeschraenkten Intervalls sowie den Fit ohne y-Fehler
plt.figure()
plt.grid(color='grey', linestyle='-', linewidth=0.1)
plt.errorbar(x, y, yerr = None, xerr= None,color='tab:red', fmt = '.', markersize=1, label = 'Messdaten',zorder=0)
plt.plot(x, func(x, popt[0], popt[1], popt[2]), color='tab:blue', linewidth = 0.5, label = 'Landau-Verteilung')
plt.plot(x, func2(x, popt1[0], popt1[1], popt1[2]), color='tab:green', linewidth = 0.5, label = 'Gauß-Verteilung')
plt.legend(loc='best')
plt.xlabel('Kanäle')
plt.ylabel('Anzahl der Ereignisse N')
plt.savefig('alpha_211_fit_intervall.pdf', bbox_inches = "tight")
plt.show()

file.close()
