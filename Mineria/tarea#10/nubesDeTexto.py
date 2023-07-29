from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random

textoGeneros = ""
textoDesarrollador=""

# leo el dataframe
cd = pd.read_csv("tarea#10/datosJuegoLimpio.csv")
print("filtrando...")

# guardamos el texto de todas las filas en un archivo txt
def filtrarGenero(renglon):
    global textoGeneros
    textoGeneros += renglon
def filtrarDesarollador(renglon):
    global textoDesarrollador
    textoDesarrollador += str(renglon+" ")

cd["desarrollador"].apply(filtrarDesarollador)
cd["genero"].apply(filtrarGenero)

archivo = open("tarea#10/GenerosDeVideojuegos.txt", mode="w")
archivo.write(textoGeneros)
archivo.close()
archivo = open("tarea#10/DesarolladoresDeVideojuegos.txt", mode="w")
archivo.write(textoDesarrollador)
archivo.close()


# Recupero el texto
archivo = open("tarea#10/GenerosDeVideojuegos.txt", mode="r")
textoGeneros = archivo.read()
archivo.close()
archivo = open("tarea#10/DesarolladoresDeVideojuegos.txt", mode="r")
textoDesarrollador = archivo.read()
archivo.close()

print("generando nubes...")

# Muestro y guardo el imagen de la nube de texto

# Para los generos 
mascaraGen = np.array(Image.open("tarea#10/Megaman.png"))
nubeGen = WordCloud(max_words=1000, mask=mascaraGen, margin=10,random_state=1).generate(textoGeneros)
default_colors = nubeGen.to_array()
plt.figure()
plt.axis("off")
plt.title("NUBE DE LOS GENEROS DE VIDEOJUEGOS")
plt.imshow(default_colors, interpolation="bilinear")
#plt.show()
nubeGen.to_file("tarea#10/MegaNube_Generos.png")

# Para los desarrolladores
mascaraDes = np.array(Image.open("tarea#10/AmongUs.png"))
nubeDes = WordCloud(max_words=2000, mask=mascaraDes,margin=10, random_state=1).generate(textoDesarrollador)
default_colors = nubeDes.to_array()
plt.figure()
plt.axis("off")
plt.title("NUBE DE LOS DESARROLLADORES DE VIDEOJUEGOS")
plt.imshow(default_colors, interpolation="bilinear")
#plt.show()
nubeDes.to_file("tarea#10/AmongUsNube_Desarrolladores.png")
print("finalizado...")

