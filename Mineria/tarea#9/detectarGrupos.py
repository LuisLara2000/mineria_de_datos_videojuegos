# librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, k_means
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def MetodoDelCodoParaValorDeK():
    # encontrar el mejor valor para "K" en base al metodo del codo
    SSE_k = []
    valor_i = []
    for i in range(1,11):
        kmeans = KMeans(init="random",n_clusters=i, n_init=10, max_iter=100, random_state=40)
        kmeans.fit(datosEscalados)
        SSE_k.append(kmeans.inertia_)
        valor_i.append(i)
    plt.title("NUMERO DE AGRUPACIONES (solo en juegos de PlayStation)")
    plt.ylabel("INERCIA (SSE)")
    plt.xlabel("NUMERO DE GRUPOS")
    plt.plot(valor_i, SSE_k)
    plt.savefig("tarea#9/Determinar numero k.png")


# Leo el conjunto de datos
cd = pd.read_csv("tarea#9/datosJuegoLimpio.csv")
cd_playStation = cd[cd["plataforma"] == "PlayStation"]

# preparo los datos
datos = cd_playStation[["puntuacion", "numero criticas"]]

# escalo los datos
escalador = MinMaxScaler().fit(datos.values)
datosEscalados = pd.DataFrame(escalador.fit_transform(datos.values), columns=["puntuacion", "numero criticas"])

# escogo el valor de 5 en base a la grafica, adjunta en esta carpeta
k_valor = 3

kmeans = KMeans(init="random",n_clusters=k_valor, n_init=10, max_iter=100, random_state=40)
kmeans.fit(datosEscalados)


# resultados
#print("El valor mas bajo de SSE = "+str(kmeans.inertia_))
#print("Numero de iteraciones para converger = "+str(kmeans.n_iter_))

# la lista que dice a que grupo pertenece cada valor lo ingreso a el data frame
datosEscalados_agrupados = datosEscalados.assign(Grupo=kmeans.labels_)

# filtro los grupos y los muestro graficamente
colores = ["green", "orange", "blue", "red", "black", "purple", "skyblue"]
nombresGrupos = ["grupo1", "grupo2", "grupo3", "grupo4", "grupo5", "grupo6", "grupo7"]
for i in range(k_valor):
    cd_temp = datosEscalados_agrupados[datosEscalados_agrupados["Grupo"] == i]
    plt.scatter(kmeans.cluster_centers_[i][0], kmeans.cluster_centers_[i][1],s=350,marker="*",color=colores[i])
    plt.scatter(cd_temp["puntuacion"],cd_temp["numero criticas"], color=colores[i])
plt.title("Grupos en juegos de playStation")
plt.ylabel("Puntuacion de los criticos")
plt.xlabel("Numero de criticos")
plt.savefig("tarea#9/juegosDePlayStationAgrupados.png")


