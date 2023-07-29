# agrupacion

# librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier



# Leo el conjunto de datos
cd = pd.read_csv("tarea#7/datosJuegoLimpio.csv")

# filtro dos nombres de plataformas y en lugar de sus nombres pongo el valor de 0 o 1
cd_agrupacion = cd.query('plataforma == "PlayStation" or plataforma == "Nintendo64"')
def traduccirPlataformas(nombre):
    if nombre == "PlayStation":
        return 0
    else:
        return 1
def escalar(numero):
    return numero*10
cd_agrupacion = cd_agrupacion.drop(cd_agrupacion[cd_agrupacion["puntuacion usuarios"] == 0].index)
cd_agrupacion["plataforma"] = cd_agrupacion["plataforma"].apply(traduccirPlataformas)
cd_agrupacion["puntuacion usuarios"] = cd_agrupacion["puntuacion usuarios"].apply(escalar)
# separo los datos
playStation = cd_agrupacion[cd_agrupacion["plataforma"] == 0]
nintendo64 = cd_agrupacion[cd_agrupacion["plataforma"] == 1]

# procesar los datos
datos = cd_agrupacion[["puntuacion", "puntuacion usuarios"]]
clase = cd_agrupacion["plataforma"]  # debe estar en 0 y 1
escalador = preprocessing.MinMaxScaler()
datos = escalador.fit_transform(datos)

# creacion del modelo
clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(datos, clase)

# uso del clasificador
criticos = 60
usuarios = 50

# escalamos los datos
nuevoJuego = escalador.transform([[criticos, usuarios]])
nuevoJuego = [[criticos,usuarios]]
print("CLASE ", clasificador.predict(nuevoJuego))
print("PORBABILIDAD POR CLASE", clasificador.predict_proba(nuevoJuego))

# graficamos
plt.scatter(playStation["puntuacion"], playStation["puntuacion usuarios"],
            marker="*", s=150, color="skyblue", label="PlayStation(Clase: 1)")
plt.scatter(nintendo64["puntuacion"], nintendo64["puntuacion usuarios"],
            marker="*", s=150, color="red", label="Nintendo64 (Clase: 0)")
plt.scatter(criticos, usuarios, marker=".", s=150,
            color="green", label="Nuevo Juego")
plt.ylabel("Usuarios")
plt.xlabel("Criticos")
plt.legend(bbox_to_anchor=(1, 0.2))
plt.savefig("tarea#7/Agrupacion.png")
plt.show()
