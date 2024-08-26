import mi_modulo

mi_modulo.hola()
suma= mi_modulo.suma(1,2)
print(suma)

import operaciones
import utilidades

resultado=operaciones.suma(5,3)
utilidades.imprimir_mensaje(f'El resultado de la suma es: {resultado}')
username=utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(username)