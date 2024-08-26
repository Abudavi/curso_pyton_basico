""" Las funciones son bloques de código reutilizables que nos permiten encapsular tareas específicas y ejecutarlas cuando sea necesario.
Las funciones nos ayudan a organizar nuestro código,
evitar la repetición y hacer que nuestros programas sean más modulares y fáciles de mantener. """
#Ejemplo

def saludo():
    print('hola desde la funcion saludo')

saludo()
#parametros y argumentos
def nombre(nombre):
    print('Hola'+nombre)
    print(f'Hola! {nombre}')
    

nombre('juan')

#valores de retornio

def suma(a,b):
    return a+b

resultado=suma(1,2)
print(f'el resultado es: {resultado}')

print(f'hola, el resultado es: {suma(1,4)}')

#funciones anonimas(lambda)

cuadrado= lambda x:x**2
print(cuadrado(5))