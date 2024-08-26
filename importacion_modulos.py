""" Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import.
Podemos importar un módulo completo o funciones específicas de un módulo. """

import math
resultado= math.sqrt(25)
print(resultado)
""" 
En este ejemplo, se importa el módulo math utilizando la declaración import. Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25.

También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función. """

from math import sqrt

resultado= math.sqrt(25)
print(resultado)

import datetime
import random

numero_aleatorio= random.randint(1,10) # numero random del 1 al 10
print(numero_aleatorio)

fecha_actual=datetime.datetime.now()
print(fecha_actual)



