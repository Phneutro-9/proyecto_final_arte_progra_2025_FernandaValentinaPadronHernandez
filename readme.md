El programa realizado es una calculadora de perímetros y áreas de diferentes figuras, importando los datos de un '.csv'

NOTA: Primero se debe instalar 'python' y su librería 'pandas' para correr el códgigo y leer el documento 'figuras.csv'

Para hacer la instalación de ambos elementos desde la terminal, siga las siguientes instrucciones:

1.- Colocar comando 'brew install python@3.12' para instalar python
2.- Colocar comando 'python3 -m venv venv' para crear un ambiente virtual
3.- Colocar comando 'source venv/bin/activate' para activar el entorno virtual anteriormente creado en python
4.- Colocar comando 'pip install pandas' para instalar la librería de python llamada 'pandas'

El funcionamiento del archivo funciones.py es le siguiente:

1.- Colocar comando 'python3 figuras_principal.py' para iniciar el programa
Con este comando, el código correrá automáticamente, leyendo los datos del .csv
El programa arroja: número de figura, tipo de figura, perimetro y área

Los cálculos se realizan desde el archivo funciones.py.
NOTA IMPORTANTE: Se solicita NO editar este archivo ya que contiene las fórmulas correctas para cada figura.

Para los datos que se encuentran en el archivo .csv, se sigue esta lógica:
1.- En el caso de un círculo, Medida1 será únicamente el radio, mientras que Medida2 deberá de ser = 0 y no utilizará
2.- Para los triángulos, se considera que ÚNICAMENTe se trabaja con un triángulo equilátero. 
  - Medida1 será la medida de los lados, mientras que Medida2 será el valor de su altura.
3.- En el caso del rectángulo, Medida1 puede ser tanto base como altura, al igual que Medida2.
