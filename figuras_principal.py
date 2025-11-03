#Importar librería pandas para leer el csv
import pandas as pd
#Importar del archivo funciones.py las funciones a ocupar para las figuras del csv
from funciones import triangulo, rectangulo, circulo
#Leer y guardar contenido del csv en la variable df
df = pd.read_csv("Figuras.csv")
#Mensaje de inicio
print("---Procesando Figuras---")
#Iterar cada fila de la variable con los datos de las medidas: df
for index, row in df.iterrows():
	#Acceder a cada valor en cada columna de la fila
	print(f"Fila {index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA']}")
