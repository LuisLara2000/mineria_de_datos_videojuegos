# Probar si hay correlacion entre la puntuacion promedio dada por los usuarios y la puntuacion promedio dada por los criticos #
import matplotlib.pyplot as plt
import pandas
import numpy as np
#
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf


# Leo el conjunto de datos
cd = pandas.read_csv("tarea#6/datosJuegoLimpio.csv")

def convertirPuntuacionUsuarios(puntuacion):
    return puntuacion*10
cd["puntuacion usuarios"] = cd["puntuacion usuarios"].apply(convertirPuntuacionUsuarios)
#df = df.drop(df[df['C']==True].index)
cd = cd.drop(cd[cd["puntuacion usuarios"] == 0].index)
#cd_100 = cd.head(100)
# Cuarta columna puntuacion criticos
criticos = cd.iloc[:, 4]
# Quinta columna puntuacion usuarios
usuarios = cd.iloc[:, 5]

criticosArray = np.array(criticos)
usuariosArray = np.array(usuarios)


pruebaCorrelacion = pearsonr(criticos,usuarios)
print("Coeficiente de correlación de Pearson: ", pruebaCorrelacion[0])
print("P-value: ",pruebaCorrelacion[1])

# se crea una instancia de regresion lineal
regresion_lineal = LinearRegression()
# le pasamos los datos
regresion_lineal.fit(criticosArray.reshape(-1, 1), usuariosArray)
# vemos los parámetros que ha estimado la regresión lineal
print('w = ' + str(regresion_lineal.coef_) +', b = ' + str(regresion_lineal.intercept_))

# y=wx+b
def linea(x):
    return 0.58932828*x+28.064891797469734
# pyplot.plot(x, [f1(i) for i in x])


# Creamos el grafico
plt.plot(criticos, [linea(i) for i in criticos], color='green')
plt.scatter(criticos, usuarios, label='data', color='blue')
plt.xlabel("criticos", size=14)
plt.ylabel("usuarios", size=14)
plt.title('puntuacion de criticos vs puntuacion de usuarios')
plt.savefig("tarea#6/RegresionLineal.png")
plt.show()
