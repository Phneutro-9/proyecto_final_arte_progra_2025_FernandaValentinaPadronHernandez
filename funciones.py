#Crear funciones de cada figura para perimetro y area

#importar libreria math para operaciones
import math

#Función para el triangulo
def triangulo():
	#Obtener perimetro triangulo
	perimetro = Medida1 + Medida2
	#Obtener area triangulo
	area = (Medida1*Medida2)/2
	#Regresar ambos valores al archivo .py principal
	return perimetro, area
#Función para el rectángulo
def rectangulo():
        #Obtener perimetro rectangulo
        perimetro = 2 * (Medida1 + Medida2)
        #Obtener area rectangulo
        area = Medida1 * Medida2
        #Regresar ambos valores al archivo .py principal
        return perimetro, area
#Función para el círculo
def circulo():
#La medida del círculo será tomada como el radio del mismo
        #Obtener perimetro círculo
        perimetro = 2 * math.pi * Medida1
        #Obtener area círculo
        area = math.pi * (Medida1)**2
        #Regresar ambos valores al archivo .py principal
        return perimetro, area
