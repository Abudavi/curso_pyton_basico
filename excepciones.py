try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

""" 
El bloque except especifica el tipo de excepción que se desea capturar y manejar. 
Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones """
try:
    # Código que puede generar una excepción
    resultado = 10 / -0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
"""     
El bloque finally es opcional y se ejecuta siempre, 
independientemente de si ocurrió una excepción o no. 
Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos. """
try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción

