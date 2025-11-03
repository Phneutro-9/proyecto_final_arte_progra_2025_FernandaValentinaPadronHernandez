#Crear funciones de cada figura para perimetro y area

#importar libreria math para operaciones
import math

#Función para el triangulo
def triangulo(medida1,medida2):
	#Obtener perimetro triangulo
	perimetro = medida1 + medida2

	#Obtener area triangulo
	area = (medida1*medida2)/2

	#Regresar ambos valores al archivo .py principal
	return perimetro, area

#Función para el rectángulo
def rectangulo(medida1,medida2):
        #Obtener perimetro rectangulo
        perimetro = 2 * (medida1 + medida2)

        #Obtener area rectangulo
        area = medida1 * medida2

        #Regresar ambos valores al archivo .py principal
        return perimetro, area

#Función para el círculo
def circulo(medida1):
#La medida del círculo será tomada como el radio del mismo
        #Obtener perimetro círculo
        perimetro = 2 * math.pi * medida1

        #Obtener area círculo
        area = math.pi * (medida1)**2

        #Regresar ambos valores al archivo .py principal
        return perimetro, area
