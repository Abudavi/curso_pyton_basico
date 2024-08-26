""" Un diccionario es una estructura de datos mutable y no ordenada que permite almacenar pares de clave-valor. 
Cada elemento en un diccionario consiste en una clave única y su valor correspondiente. 
Los diccionarios se encierran entre llaves {}, y los pares clave-valor se separan por comas. """

persona={'nombre':'Juan','Edad':'25','Ciudad':'Mexico'}

print(persona)
print(persona['nombre'])
print(persona['Edad'])
print(persona['Ciudad'])
""" 
keys(): devuelve una vista de todas las claves del diccionario.
values(): devuelve una vista de todos los valores del diccionario.
items(): devuelve una vista de todos los pares clave-valor del diccionario.
update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
pop(): elimina por medio de la key ejemplo persona.pop('edad')
"""

print('keys() todas las claves')
print(persona.keys())
print('values() todos los valores')
print(persona.values())
print('items() imprime en pares (clave,valor)')
print(persona.items())
print('update() actualiza el diccionario con otro diccionario')
persona.update({'profecion':'ingeniero'})
print(persona)
print('pop() elimina por medio del keys')
print(persona.pop('profecion'))
print(persona)