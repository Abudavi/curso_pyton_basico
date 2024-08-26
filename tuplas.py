""" Una tupla es una estructura de datos inmutable y ordenada que permite almacenar una colección de elementos. 
Los elementos de una tupla se encierran entre paréntesis (), separados por comas. """

punto=(3,4)
print(punto[0])

""" A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas. 
No se pueden agregar, eliminar o cambiar elementos en una tupla existente. """


""" 
count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla. """

tupla=(0,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1)
print('cont(cuentas las veces que aparece un elemento)')
print(tupla.count(1))
print('index(la selecciona la posicion de el elemento)')
print(tupla.index(8))

print('len (cuenta los elementos de la tupla)')
print(len(tupla))