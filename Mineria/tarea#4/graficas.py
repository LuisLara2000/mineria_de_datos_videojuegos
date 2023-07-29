# graficar la informacion 
from gzip import FNAME
import matplotlib.pyplot as plt
import numpy as np
import pandas

plt.style.use('_mpl-gallery-nogrid')

# Para la grafica pastel
cd = pandas.read_csv("tarea#4/datosJuegoLimpio.csv")

def clasificarConsolaConMarca(nombre):
    if (nombre == "PlayStation5" or nombre == "PlayStation" or nombre == "PlayStationVita" or nombre == "PSP" or nombre == "PlayStation3" or nombre == "PlayStation2" or nombre == "PlayStation4"):
        return "SONY"
    elif (nombre == "Xbox" or nombre == "XboxOne" or nombre == "XboxSeriesX" or nombre == "Xbox360"):
        return "MICROSOFT"
    elif (nombre == "Stadia"):
        return "GOOGLE"
    elif(nombre == "Dreamcast"):
        return "SEGA"
    elif(nombre == "PC"):
        return "NO APLICA"
    else:
        return "NINTENDO"
cd["marca"] = cd["plataforma"].apply(clasificarConsolaConMarca)
cd_marcas = cd[["nombre", "plataforma", "marca"]]
cd_marcas = cd_marcas.rename_axis("id")
cd_juegos_marcas = cd.groupby(["marca"]).size().reset_index(name="cantidad de juegos por marca")

# Para la grafica de barras #
cd_plataformas = cd.groupby(['plataforma']).size().reset_index(name="cantidad de juegos")
consolas = cd_plataformas.iloc[:, 0]
cd_plataformas.set_index("plataforma", inplace=True)


# ############################################# #
# Grafica pastel (cantidad de juegos por marca) #
# ############################################# #

valores = cd_juegos_marcas.iloc[:,1] # obtengo los valores del data frame
etiquetas = ["GOOGLE","MICROSOFT","NINTENDO",   "PC",    "SEGA",   "SONY"]
colores = ["#EE6055", "#60D394", "#AAF683", "#FFD97D", "#FF9B85", "#AAF683"]
desfase = (0, 0, 0, 0, 0, 0.2)
plt.pie(valores, labels=etiquetas, autopct="%0.1f %%", radius=3, center=(4, 4), colors=colores,explode=desfase)
plt.axis("equal")
plt.title("Porcentaje de la cantidad de juegos por marca")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

graficaMarcas = plt.gcf()
graficaMarcas.set_figheight(10)
graficaMarcas.set_figwidth(10)

graficaMarcas.savefig("tarea#4/Cantidad de juegos por marca (pastel).png")

# ################# #
# Grafica de barras #
# ################# #

cd_plataformas.plot(kind='bar', width=0.9)
cd_plataformas.plot = plt.gcf()
cd_plataformas.plot.set_figheight(10)
cd_plataformas.plot.set_figwidth(10)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
plt.title("Cantidad de juegos por consola")
cd_plataformas.plot.savefig("tarea#4/Cantidad de juegos por consola (barras).png")
plt.clf()

###############################
# Para las graficas multiples #
###############################

# Obtengo todos los nombres de las consolas
consolasLimpias = []
for i in range(len(consolas)):
    if consolas[i] != "PlayStation5" and consolas[i] != "Stadia" and consolas[i] != "XboxSeriesX" and consolas[i]:
       consolasLimpias.append(str(consolas[i]))

p_cd = pandas.read_csv("tarea#4/popularidad.csv")

for consola in consolasLimpias:
    cd_tem = p_cd[(p_cd["plataforma"] == consola)].sort_values("numero usuarios", ascending=False)
    cd_tem = cd_tem[["nombre", "numero usuarios"]]  
    nombres = cd_tem.head(10).iloc[:, 0]
    valores = cd_tem.head(10).iloc[:, 1]
    plt.plot(nombres, valores)
    plt.xticks(rotation='vertical')
    plt.subplots_adjust(left=0.075, right=0.9, top=0.9, bottom=0.5)
    plt.title("Top 10 juegos de "+str(consola)+" con mas usuarios ")
    cd_temp = plt.gcf()
    cd_temp.set_figheight(10)
    cd_temp.set_figwidth(10)
    cd_temp.savefig("tarea#4/Top 10 juegos de "+str(consola)+" (Lineas).png")
    cd_tem.pop("nombre")
    cd_tem.pop("numero usuarios")
    nombres = []
    valores = []
    plt.clf()

########################
# Para los histogramas #
########################

p_usuarios = cd.iloc[:,5]
plt.hist(p_usuarios,edgecolor="black")
plt.title("Puntuacion media dada por los usuarios")
plt.subplots_adjust(left=0.075, right=0.9, top=0.9, bottom=0.08)
plt_tem = plt.gcf()
plt_tem.set_figheight(15)
plt_tem.set_figwidth(15)
plt_tem.savefig("tarea#4/Puntuaciones medias dadas por los usuarios (histograma).png")

#######################
# Graficas de bigotes #
# DE LA TAREA 5       #
#######################

# puntuacion de los usuarios y consolas
datos = (cd.groupby("plataforma")["puntuacion usuarios"].agg(lambda x:list(x)))
labels = datos.index
fig, ax = plt.subplots()
ax.boxplot(datos)
ax.set_xticks(np.arange(1, len(labels) + 1), labels=labels)
plt.xlabel("Plataformas",size=14)
plt.ylabel("puntuacion promedio de usuarios",size=14)
plt.title("Plataforma y puntuacion promedio de usuarios",size=16)
plt.xticks(rotation='vertical')
plt.subplots_adjust(left=0.07, right=0.95, top=0.9, bottom=0.25)
plt_tem = plt.gcf()
plt_tem.set_figheight(15)
plt_tem.set_figwidth(15)
plt_tem.savefig("tarea#4/Plataforma y puntuacion promedio de usuarios(caja de bigotes).png",format='png', dpi=150)
