#Importar librería pandas para leer el csv
import pandas as pd

#Importar del archivo funciones.py las funciones a ocupar para las figuras del csv
from funciones import triangulo, rectangulo, circulo

#Leer y guardar contenido del csv en la variable df
dfile = pd.read_csv("figuras.csv")

#Counter para número de figura
counter = 0

#Counter para número de triángulos
tri = 0

#Counter para número de rectángulos
rec = 0

#Counter para número de círculos
cir = 0

#Matriz perímetros
perimetros = []

#Matriz áreas
areas = []

#Mensaje de inicio
print("---Procesando Figuras---")

#Iterar cada fila de la variable con los datos de las medidas: df
for index, row in dfile.iterrows():
	#Acceder e imprimir cada valor en cada columna de la fila
	#print(f"Fila {index}: Figura={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")
	
	#Guardar Figura, Medida1 y Medida2 en una variable temporal
	figura = row['FIGURA']
	medida1 = row['MEDIDA1']
	medida2 = row['MEDIDA2']

	#Comenzar llamando a cada función dependiento a la figura indicada en el archivo csv
	
	#Si figura es "c", llamar función del círculo
	if figura == "c":
		#Aumentar 1 para indicar número de figura
		counter += 1

		#Indicar que figura es
		print(f"Figura {counter} = círculo")

		#Guardar perimetro y area econtradas
		perimetro, area = circulo(medida1)
		perimetros.append(perimetro)
		areas.append(area)

		#Imprimir perimetro y area conseguidos
		print(f"Perimetro = {perimetro:.4f}\nArea = {area:.4f}\n")
		
		#Aumentar en 1 el número de círculos
		cir += 1
		
	#Si figura es "t", llamar función del triángulo
	elif figura == "t":
		#Aumentar 1 para indicar número de figura
		counter += 1

		#Indicar que figura es
		print(f"Figura {counter}  = triángulo")

		#Guardar perimetro y area econtradas
		perimetro, area = triangulo(medida1,medida2)
		perimetros.append(perimetro)
		areas.append(area)
		
		#Imprimir  perimetro y area conseguidos
		print(f"Perimetro = {perimetro:.4f}\nArea = {area:.4f}\n")

		#Aumentar en 1 el número de triángulos
		tri +=1

	#Si figura es "r", llamar función del rectángulo
	elif figura == "r":
		#Aumentar 1 para indicar número de figura
		counter += 1

		#Indicar que figura es
		print(f"Figura {counter}  = rectángulo")
		
		#Guardar perimetro y area econtradas
		perimetro, area = rectangulo(medida1,medida2)
		perimetros.append(perimetro)
		areas.append(area)

		#Imprimir  perimetro y area conseguidos
		print(f"Perimetro = {perimetro:.4f}\nArea = {area:.4f}\n")
		
		#Aumentar en 1 el número de rectángulos
		rec += 1

#print(perimetro,areas)

print("¡Todas las figuras han sido procesadas con éxito!")

#Mostrar total de triángulos, rectángulos y círculos
print(f"Total círculos = {cir}\nTotal triángulos = {tri}\nTotal rectángulos = {rec}")

print("\nFin del código.\n")

