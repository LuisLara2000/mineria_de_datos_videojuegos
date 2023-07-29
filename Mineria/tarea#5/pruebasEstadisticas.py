# pruebas estadisticas
from scipy.stats import shapiro
import numpy as np
import pandas
import pingouin as pg

cd = pandas.read_csv("tarea#5/datosJuegoLimpio.csv")
p_usuarios = cd.head(4500).iloc[:, 5]

# Prueba de shapiro para saber si los datos son normalizados
estadistico,p_value = shapiro(p_usuarios)
if p_value<0.05:
    print("LOS DATOS NO SIGUEN UNA DISTRIBUCION NORMAL")
else:
    print("LOS DATOS SIGUEN UNA DISTRIBUCION NORMAL")        
print(" ")

# Comparar que grupo sale mejor puntuado en 
cd_SONY_NINTENDO = pandas.read_csv("tarea#5/puntaje_SONY_NINTENDO.csv")

print(pg.homoscedasticity(data=cd_SONY_NINTENDO,dv="puntuacion usuarios", group="marca", method='levene'))

cd_SONY = cd_SONY_NINTENDO[cd_SONY_NINTENDO["marca"] == "SONY"]
valores_SONY = cd_SONY.iloc[:,0]
cd_NINTENDO = cd_SONY_NINTENDO[cd_SONY_NINTENDO["marca"] == "NINTENDO"]
valores_NINTENDO = cd_NINTENDO .iloc[:, 0]

print(pg.mwu(x=valores_SONY, y=valores_NINTENDO, alternative='two-sided'))
