# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:18:49 2020

@author: Proyecto "Novela Visual con IA"
"""
#se importan todas las librerias necesarias
import random
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

#Formula
values = []
for x in range(50):
    values.append(random.randint(1, 5))

k=0
F1=0
F2=0
F3=0
F4=0
F5=0
for x in range(9):
    F1=values[k+1]+F1
    F2=values[k+2]+F2
    F3=values[k+3]+F3
    F4=values[k+4]+F4
    F5=values[k+5]+F5
    k=k+5

F1=F1/10
F2=F2/10
F3=F3/10
F4=F4/10
F5=F5/10

extroversion=math.trunc((0.1435*(pow(F1, 6)))-(1.8247*(pow(F1, 5)))+(7.3386*(pow(F1, 4)))-((90045/10000)*(pow(F1, 3)))+(3.7692*(pow(F1, 2)))+(1.2185*F1)-(354/10000))
estabilidad_emocional=math.trunc((0.2163*pow(F2, 6))-(2.7549*pow(F2, 5))+(11.572*pow(F2, 4))-(17.3*pow(F2, 3))+(10.891*pow(F2, 2))-(1.2324*2)-0.0239+1)
amabilidad=math.trunc((0.3832*pow(F3, 6))-(6.8086*pow(F3, 5))+(45.159*pow(F3, 4))-(137.91*pow(F3, 3))+(197.41*pow(F3, 2))-(107.13*F3)-0.0028)
conciencia=math.trunc((0.6434*pow(F4, 6))-(10.271*pow(F4, 5))+(61.407*pow(F4, 4))-(170.29*pow(F4, 3))+(224.94*pow(F4, 2))-(114.56*F4)-0.0023)
intelecto_imaginacion=math.trunc((1.391386165*pow(F5, 6))-(26.43986331*pow(F5, 5))+(197.1863751*pow(F5, 4))-(730.1871814*pow(F5, 3))+(1401.003617*pow(F5, 2))-(1282.44321*(F5))+400.3471777)

if extroversion<1:
    extroversion=10

if estabilidad_emocional<1:
    estabilidad_emocional=10

if amabilidad<1:
    amabilidad=10

if conciencia<1:
    conciencia=10

if intelecto_imaginacion<1:
    intelecto_imaginacion=10

Personalidad = [extroversion, estabilidad_emocional, amabilidad, conciencia, intelecto_imaginacion]

#Red Neuronal

#se lee el dataset
data=pd.read_csv('CaraBocas.csv', delimiter=';')
#se separan los datos de entrada de los datos de salida  de dataset
#x= entradas , y = salidas(el primer digito son los ojos y los otoros dos son la boca)
x=data.iloc[:,0:5].dropna(axis=0)
y=data.iloc[:,5: 6].dropna(axis=0)
#se define el modelo SVC
procesoSVC =  SVC(kernel='poly',degree=3)
#se establece la semilla
seedSVC = 2
#se distribuye los porcentajes de entrenamiento y prediccion 20% prediccion y 80% fit
validation_size = 0.20
#se seleccionan variables de entrenamiento y testeo
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=validation_size,random_state=seedSVC)
#se inicia entreanimeto
procesoSVC.fit(x_train, y_train)
#reporte
scoreSVC=procesoSVC.score(x_test, y_test)
prediccionSVC = procesoSVC.predict(x_test)
matrizConfusionSVC=confusion_matrix(y_test, prediccionSVC)
#reporteSVC=classification_report(y_test, prediccionSVC)

Prediccion=procesoSVC.predict(np.array(Personalidad).reshape(1, -1))

#Imagen
##Recolección de variables
genero = 0#random.randint(0,1)
if genero == 0:
    cuerpo = random.randint(1,9)
    pelo = 1
    ojos = int(Prediccion/100)
    boca = int(Prediccion - (ojos*100))
else:
    cuerpo = random.randint(1,7)
    if cuerpo == 2 or cuerpo == 5 or cuerpo == 6:

        pelo = 0
    else:
        pelo = random.randint(1,2)
    ojos = int(Prediccion/100)
    boca = int(Prediccion - (ojos*100))
    
#Organización de las imagenes
if genero == 0:
    direccion = 'Personajes\Cuerpos' + '\F' + str(cuerpo) + '.png'
    imagenCuerpo = plt.imread(direccion)
    direccion = 'Personajes\Pelo' + '\F' + str(pelo) + '.png'
    imagenPelo = plt.imread(direccion)
    direccion = 'Personajes\Ojos' + '\F' + str(ojos) + '.png'
    imagenOjos = plt.imread(direccion)
    direccion = 'Personajes\Bocas' + '\F' + str(boca) + '.png'
    imagenBoca = plt.imread(direccion)
else:
    direccion = 'Personajes\Cuerpos' + '\M' + str(cuerpo) + '.png'
    imagenCuerpo = plt.imread(direccion)
    if pelo != 0:   
        direccion = 'Personajes\Pelo' + '\M' + str(pelo) + '.png'
        imagenPelo = plt.imread(direccion)
    direccion = 'Personajes\Ojos' + '\M' + str(ojos) + '.png'
    imagenOjos = plt.imread(direccion)
    direccion = 'Personajes\Bocas' + '\M' + str(boca) + '.png'
    imagenBoca = plt.imread(direccion)

tam = np.shape(imagenOjos)
for i in range(0,tam[0]):
    for j in range(0,tam[1]):
        for k in range(0,tam[2]):
            if imagenOjos[i,j,3] != 0:
                imagenCuerpo[i+220,j+570,k] = imagenOjos[i,j,k] 

tam = np.shape(imagenBoca)
for i in range(0,tam[0]):
    for j in range(0,tam[1]):
        for k in range(0,tam[2]):
            if imagenBoca[i,j,3] != 0:
                imagenCuerpo[i+250,j+570,k] = imagenBoca[i,j,k] 

if pelo != 0:
    tam = np.shape(imagenPelo)
    for i in range(0,tam[0]):
        for j in range(0,tam[1]):
            for k in range(0,tam[2]):
                if imagenPelo[i,j,3] != 0:
                    imagenCuerpo[i-130,j+320,k] = imagenPelo[i,j,k] 

plt.imshow(imagenCuerpo)   
