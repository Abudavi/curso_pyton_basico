def calcular_media(*numeros):#el * permite ingresar cantidad indefinidad de numeros
    suma=sum(numeros)
    cantidad=len(numeros)
    media=suma/cantidad
    return media

print('la media es:',calcular_media(1,2,3,4,5))

sumar= lambda x:x+3

print(sumar(5))