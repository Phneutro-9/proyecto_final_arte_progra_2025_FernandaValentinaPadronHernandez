#Importar librería pandas para leer el csv
import pandas as pd

#Importar del archivo funciones.py las funciones a ocupar para las figuras del csv
from funciones import triangulo, rectangulo, circulo

#Leer y guardar contenido del csv en la variable df
dfile = pd.read_csv("figuras.csv")

#Matriz perímetros
perimetros = []

#Matriz áreas
areas = []

#Mensaje de inicio
print("---Procesando Figuras---")

#Iterar cada fila de la variable con los datos de las medidas: df
for index, row in dfile.iterrows():
	#Acceder a cada valor en cada columna de la fila
	print(f"Fila {index}: Figura={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
