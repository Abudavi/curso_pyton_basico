nombre=input('ingresa tu nombre:')#input solo maneja String
edad= int(input('ingresa tu edad:'))# si se desea trabajar con numeros antes del input int() o float()

print(f'tu nombre es: {nombre} y tienes {edad} años ')

if edad<18:
    print(f'Tu edad es: {edad} por lo tanto eres menor de edad')
else:print(f'Tu edad es de {edad} por lo tanto eres mayor de edad')