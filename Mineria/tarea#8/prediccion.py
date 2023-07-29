# prediccion 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
# Leo el conjunto de datos
cd = pd.read_csv("tarea#8/datosJuegoLimpio.csv")

# juegos por año
def juegosFecha(fecha):
    fechaTexto = str(fecha)
    return str(fechaTexto[0])+str(fechaTexto[1])+str(fechaTexto[2])+str(fechaTexto[3])

# generar linea
def linea(x,w,b):
    return w*x+b

# cd_agrupacion["puntuacion usuarios"] = cd_agrupacion["puntuacion usuarios"].apply
cd["Año"] = cd["fecha lanzamiento"].apply(juegosFecha)

años = []
primeros5Años = []
ultimos5Años = []
juegosCantidad = []
primeros5JuegosCantidad = []
ultimos5JuegosCantidad = []

# filtro los juegos por año
for i in range(1995,2021):
    # todos los años
    numeroJuegos = len(cd[cd["Año"]==str(i)])
    años.append(i)
    juegosCantidad.append(numeroJuegos)
    # primero 5
    if i < 2000:
        primeros5Años.append(i)
        primeros5JuegosCantidad.append(numeroJuegos)
    # ultimos 5
    if i > 2015:
        ultimos5Años.append(i)
        ultimos5JuegosCantidad.append(numeroJuegos)


# convierto las listas en listas numpy
an = np.array(años)
an_p5 = np.array(primeros5Años)
an_u5 = np.array(ultimos5Años)

ju = np.array(juegosCantidad)
ju_p5 = np.array(primeros5JuegosCantidad)
ju_u5 = np.array(ultimos5JuegosCantidad)

print(an)
print(an_p5)
print(an_u5)

# se crea una instancia de regresion lineal
regresion_lineal_todos = LinearRegression()
regresion_lineal_primeros5 = LinearRegression()
regresion_lineal_ultimos5 = LinearRegression()

# le pasamos los datos
regresion_lineal_todos.fit(an.reshape(-1, 1), ju)
regresion_lineal_primeros5.fit(an_p5.reshape(-1, 1), ju_p5)
regresion_lineal_ultimos5.fit(an_u5.reshape(-1, 1), ju_u5)


# graficamos
plt.plot(años, [linea(x, regresion_lineal_todos.coef_,regresion_lineal_todos.intercept_) for x in años], color='green')
plt.plot(primeros5Años, [linea(x, regresion_lineal_primeros5.coef_,regresion_lineal_primeros5.intercept_) for x in primeros5Años], color='black')
plt.plot(ultimos5Años, [linea(x, regresion_lineal_ultimos5.coef_,regresion_lineal_ultimos5.intercept_) for x in ultimos5Años], color='red')
plt.scatter(años, juegosCantidad,s=150)
plt.ylabel("CANTIDAD DE JUEGOS")
plt.xlabel("AÑOS")
plt.savefig("tarea#8/Prediccion.png")
plt.show()

