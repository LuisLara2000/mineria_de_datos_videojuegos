# PROBANDO COMANDOS EN EL CONJUNTO DE DATOS ESCOGIDO EN LA TAREA #1

# Libreria necesarias
import pandas
from datetime import datetime

print("----------------------------------------------------- IMPORTACION DE LOS DATOS -----------------------------------------------------")

print("\nCOMANDO -> pandas.read_csv()")
# Lee el conjunto de datos
conjuntoDeDatos = pandas.read_csv("tarea#2/datosJuegos.csv")
# Imprime todos los datos, todas las columnas
print(conjuntoDeDatos)


print("\nCOMANDO -> pandas.date_range()")
# Imprime los dias que hay entre dos fechas
print(pandas.date_range("2017-01-01", "2017-02-01"))
# Imprime los 10 dias siguientes al de la fecha inicial
print(pandas.date_range("2017-01-01", periods=10))


print("\n\n\n---------------------------------------------------------- DATA CLEANING -----------------------------------------------------")
# elimino los datos nulos
print("\nAntes del [dropna] filas = 17944     despues del [dropna] filas = 17922")
print(conjuntoDeDatos.dropna())

# Renombro todos los encabezados de las columnas
conjuntoDeDatos.columns = ["nombre", "plataforma", "fecha lanzamiento", "puntuacion", "puntuacion usuarios",
                           "desarrollador", "genero", "numero jugadores", "numero criticas", "numero usuarios"]

# convierto las fechas
def formatoFechas(fecha):
    fechaSeparada = fecha.split()
    tem = ""
    if(fechaSeparada[0] == "January"):
        fechaSeparada[0] = "01"
    elif(fechaSeparada[0] == "February"):
        fechaSeparada[0] = "02"
    elif(fechaSeparada[0] == "March"):
        fechaSeparada[0] = "03"
    elif(fechaSeparada[0] == "April"):
        fechaSeparada[0] = "04"
    elif(fechaSeparada[0] == "May"):
        fechaSeparada[0] = "05"
    elif(fechaSeparada[0] == "June"):
        fechaSeparada[0] = "06"
    elif(fechaSeparada[0] == "July"):
        fechaSeparada[0] = "07"
    elif(fechaSeparada[0] == "August"):
        fechaSeparada[0] = "08"
    elif(fechaSeparada[0] == "September"):
        fechaSeparada[0] = "09"
    elif(fechaSeparada[0] == "October"):
        fechaSeparada[0] = "10"
    elif(fechaSeparada[0] == "November"):
        fechaSeparada[0] = "11"
    elif(fechaSeparada[0] == "December"):
        fechaSeparada[0] = "12"
    for i in range(len(fechaSeparada[1])-1):
        tem += fechaSeparada[1][i]
    fechaSeparada[1] = tem
    fechaFormateada = str(
        fechaSeparada[1]+"/"+fechaSeparada[0]+"/"+fechaSeparada[2])
    return datetime.strptime(str(fechaFormateada), "%d/%m/%Y")
conjuntoDeDatos["fecha lanzamiento"] = conjuntoDeDatos["fecha lanzamiento"].map(formatoFechas)

# Ordena los datos en base a la fecha de estreno, de las recien a la mas antigua
print("\nCOMANDO -> conjuntoDeDatos.sort_values()")
print(conjuntoDeDatos.sort_values("fecha lanzamiento"))

print("\nCOMANDO -> conjuntoDeDatos.groupby()")
print(conjuntoDeDatos.groupby("plataforma"))

# Elimino los juego con un promedio de 0
condicion = conjuntoDeDatos[conjuntoDeDatos["numero usuarios"] == 0].index
conjuntoDeDatos = conjuntoDeDatos.drop(condicion)
condicion = conjuntoDeDatos[conjuntoDeDatos["numero criticas"] == 0].index
conjuntoDeDatos = conjuntoDeDatos.drop(condicion)

# limpio los valores basura
condicion = conjuntoDeDatos[conjuntoDeDatos["puntuacion usuarios"] == "tbd"].index
conjuntoDeDatos = conjuntoDeDatos.drop(condicion)

conjuntoDeDatos = conjuntoDeDatos.sort_values("puntuacion usuarios")
print("\nCOMANDO -> conjuntoDeDatos.to_csv()")
conjuntoDeDatos.to_csv("tarea#2/datosJuegoLimpio.csv")


print("\n\n\n----------------------------------------------------- ESTADISTICAS DE LOS DATOS --------------------------------------------")

# Imprime los 15 primeros datos, todas las columnas
print("\nCOMANDO -> conjuntoDeDatos.head(15)")
print(conjuntoDeDatos.head(15))
# Imprime los 15 ultimos datos, todas las columnas
print("\nCOMANDO -> conjuntoDeDatos.tail(15)")
print(conjuntoDeDatos.tail(15))
# Informacion del dataframe
print("\nCOMANDO -> conjuntoDeDatos.info()")
print(conjuntoDeDatos.info())
# Obtiene datos estadisticos 
print("\nCOMANDO -> conjuntoDeDatos.describe()")
print(conjuntoDeDatos.describe())
# Obtiene la media de todas las columnas numericas
print("\nCOMANDO -> conjuntoDeDatos.mean(numeric_only=True)")
print(conjuntoDeDatos.mean(numeric_only=True))
# Obtiene el valor medio de todas las columnas numericas
print("\nCOMANDO -> conjuntoDeDatos.median(numeric_only=True)")
print(conjuntoDeDatos.median(numeric_only=True))
# Obtinene la desviacion estandar
print("\nCOMANDO -> conjuntoDeDatos.std(numeric_only=True)")
print(conjuntoDeDatos.std(numeric_only=True))
# Obtinene una matriz de correlacion 
print("\nCOMANDO -> conjuntoDeDatos.corr()")
print(conjuntoDeDatos.corr())
# Cuenta todos los valores diferentes Nan
print("\nCOMANDO -> conjuntoDeDatos.count(numeric_only=True)")
print(conjuntoDeDatos.count(numeric_only=True))
# Obtinene el valor maximo 
print("\nCOMANDO -> conjuntoDeDatos.max(axis=0, numeric_only=True)")
print(conjuntoDeDatos.max(axis=0, numeric_only=True))
# Obtinene el valor minimo
print("\nCOMANDO -> conjuntoDeDatos.min(axis=0, numeric_only=True)")
print(conjuntoDeDatos.min(axis=0, numeric_only=True))



