""" Una lista es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos.
Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes [], separados por comas. """

frutas=['manzana','platano','pera']
""" 
append(elemento): agrega un elemento al final de la lista.
insert(indice, elemento): inserta un elemento en una posición específica de la lista.
remove(elemento): elimina la primera aparición de un elemento en la lista.
pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
sort(): ordena los elementos de la lista en orden ascendente.
reverse(): invierte el orden de los elementos en la lista. """
print('append')
frutas.append('naranja')
print(frutas)

print('insert')
frutas.insert(0,'uva')
print(frutas)

print('remove')
frutas.remove('uva')
print(frutas)

print ('pop')
frutas.pop(1)
print(frutas)

print('sort')
frutas.sort()
print(frutas)

print('reverse')
frutas.reverse()
print(frutas)