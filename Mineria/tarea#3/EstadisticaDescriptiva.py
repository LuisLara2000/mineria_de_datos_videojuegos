# ESTADISTICA DESCRIPTIVA #
from re import A
import re
import pandas
"""
nombre : El nombre del juego
plataforma : Plataforma en la que fue lanzado
r-date : fecha de lanzamiento
puntuación : puntuación media dada por los críticos (metascore)
puntuación de usuario : puntuación media dada por los usuarios en el sitio web
desarrollador : desarrollador de juegos
género : género del juego (puede ser múltiple)
jugadores : Número de jugadores (algunos juegos no tienen esta información)
críticos : número de críticos que opinan sobre el juego
usuarios : número de usuarios metacríticos que revisaron el juego
Todos los datos se recopilaron el 10 de noviembre de 2020.

Informe del proyecto aquí .

Breve descripción en el sitio de Portfolio aquí ."""
# Lee el conjunto de datos
cd = pandas.read_csv("tarea#3/datosJuegoLimpio.csv")

print("La puntuancion media más BAJA dada por los usuarios: " , end="")
print(cd["puntuacion usuarios"].min())
print("La puntuancion media más ALTA dada por los usuarios: ", end="")
print(cd["puntuacion usuarios"].max())
print("La puntuacion media de los usuarios dada más repetida: ", end="")
print(cd["puntuacion usuarios"].mode())
print(cd[cd["puntuacion usuarios"] >= 7.7]["nombre"].count())
print("Cantidad de usuarios que dieron una puntuacion a un juego: ", end="")
print(cd["numero usuarios"].sum())

print("La puntuancion media más BAJA dada por los CRITICOS: ", end="")
print(cd["puntuacion"].min())
print("La puntuancion media más ALTA dada por los CRITICOS: ", end="")
print(cd["puntuacion"].max())
print("La puntuacion media de los CRITICOS dada más repetida: ", end="")
print(cd["puntuacion"].mode())
print(cd[cd["puntuacion"] >= 80]["nombre"].count())
print("Cantidad de CRITICOS que dieron una puntuacion a un juego: ", end="")
print(cd["puntuacion"].sum())

print("Numero de juegos que tienen una puntuacion media dada por los usuarios mayor o igual que 9.5: ", end="")
print(cd[cd["puntuacion usuarios"] >= 9.5]["nombre"].count())

print("Numero de juegos que tienen una puntuacion media dada por los CRITICOS mayor o igual que 9.5: ", end="")
print(cd[cd["puntuacion"] >= 95]["nombre"].count())

cd = cd.sort_values("fecha lanzamiento")
print("El juego mas antiguo")
print(cd.head(1))

print("El juego mas recien")
print(cd.tail(1))

cd = cd.sort_values("numero usuarios")
print("El juego con mas reseñas de usuarios")
print(cd.tail(1))
print("El juego con menos reseñas de usuarios")
print(cd.head(1))

cd = cd.sort_values("numero criticas")
print("El juego con mas reseñas de criticos")
print(cd.tail(1))
print("El juego con menos reseñas de criticos")
print(cd.head(1))

cd = cd.sort_values("puntuacion usuarios")
print("El juego con mejor puntuacion usuarios")
print(cd.tail(3))
cd = cd.sort_values("puntuacion")
print("El juego con mejor puntuacion criticos")
print(cd.tail(3))

print("MODA de usuarios que dieron una puntuacion a un juego: ", end="")
print(int(cd["numero usuarios"].mode()))
print(cd[cd["numero usuarios"] >= 5]["nombre"].count())
print("MODA de criticos  que dieron una puntuacion a un juego: ", end="")
print(int(cd["numero criticas"].mode()))
print(cd[cd["numero criticas"] >= 7]["nombre"].count())
print("La desviacion media de la cantidad de usuarios que criticaron un juego es: ", end="")
print(cd["numero usuarios"].mad())
print("La varianza en la cantidad de usuarios que criticaron un juego es: ", end="")
print(cd["numero usuarios"].var())
print("calculamos la asimetria de la cantidad de usuarios que criticaron un juego es: ", end="")
print(cd["numero usuarios"].skew())
print("calculamos la kurtosis de la cantidad de usuarios que criticaron un juego es: ", end="")
print(cd["numero usuarios"].kurt())
print("\n")

# creamos una nueva tabla sobre la popularidad de los juegos 
print(" dataFrame sobre la popularidad de los juegos ")
def popularidad(numeroDeUsuarios):
    if(numeroDeUsuarios>=300):
        return "popular"
    elif(numeroDeUsuarios >= 200 and numeroDeUsuarios<=299):
        return "conocido"
    elif(numeroDeUsuarios >= 100 and numeroDeUsuarios <= 199):
        return "poco conocido"
    else:
        return "desconocido"
cd["popularidad"] = cd["numero usuarios"].apply(popularidad)
cd_popularidad = cd[["nombre", "numero usuarios", "popularidad"]]
cd_popularidad = cd_popularidad.rename_axis("id")
print(cd_popularidad[["nombre", "numero usuarios", "popularidad"]].head(25))
cd_popularidad.to_csv("tarea#3/popularidad.csv")
print("\n")

# creamos una nueva columna con que tendra el valor de las marcas
print(" dataFrame con columna de marcas ")
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
        return "PC"
    else:
        return "NINTENDO"
cd["marca"] = cd["plataforma"].apply(clasificarConsolaConMarca)
cd_marcas = cd[["nombre", "plataforma", "marca","puntuacion usuarios"]]
cd_marcas = cd_marcas.rename_axis("id")
print(cd_marcas.head(25))
cd_marcas.to_csv("marcas_puntaje.csv")
print("\n")


# agrupo los juegos por plataforma 
print(" dataFrame con la cantidad de juegos por plataforma ")
cd_plataformas = cd.groupby(['plataforma']).size().reset_index(name="cantidad de juegos")
print(cd_plataformas.sort_values("cantidad de juegos"))
cd_plataformas.to_csv("tarea#3/plataformas.csv")
print("\n")

# agrupamos por marca
print(" dataFrame con la cantidad de juegos por marca ")
cd_juegos_marcas = cd.groupby(["marca"]).size().reset_index(name="cantidad de juegos por marca")
print(cd_juegos_marcas.sort_values("cantidad de juegos por marca"))
cd_juegos_marcas.to_csv("tarea#3/juegos_marcas.csv")
print("\n")


# unimos dos dataframes, marca y popularidad
print(" dataFrame con la popularidad y la marca de las plataformas de los juegos ")
cd_marcas_popularidad = cd_marcas.join(cd_popularidad,lsuffix='', rsuffix='2')
cd_marcas_popularidad = cd_marcas_popularidad.drop(['nombre2'], axis=1)
cd_marcas_popularidad.to_csv("tarea#3/popularidad.csv")
print(cd_marcas_popularidad.head(20))
print("\n")

# se escogieron los mejores 400 juegos puntuados por los usuarios
cd_marcas_puntaje = pandas.read_csv("marcas_puntaje.csv")
cd_SONY = cd_marcas_puntaje[cd_marcas_puntaje["marca"]=="SONY"]
cd_SONY = cd_SONY[["puntuacion usuarios", "marca"]].sort_values("puntuacion usuarios",ascending=False).head(4000)

cd_NINTENDO = cd_marcas_puntaje[cd_marcas_puntaje["marca"]=="NINTENDO"]
cd_NINTENDO = cd_NINTENDO[["puntuacion usuarios", "marca"]].sort_values("puntuacion usuarios", ascending=False).head(4000)

cd_SONY_NINTENDO = pandas.concat([cd_SONY,cd_NINTENDO])
cd_SONY_NINTENDO.to_csv("tarea#3/puntaje_SONY_NINTENDO.csv")
