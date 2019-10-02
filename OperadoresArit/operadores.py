# Ejemplos de los operadores en python

a,b = 10,6 # Definimos dos variables para utilizar los operadores

# Para mostrar por pantalla (imprimir) alguna operacion lo podemos hacer de dos maneras, la primera con la operacion suma:

print(a+b)

# O almacenandola en otra variable

c = a+b
print(c)

# Resta

print("la resta de {} menos {} es: {}".format(a,b,a-b))

# Multiplicacion

c = a*b
print("La multiplicacion de las dos variables es: ", str(c))

# Division

c = a/b
print("la division de las variables es: ", str(c))

# Exponente

print(a**2)

# Modulo: La operacion modulo devuelve el residuo de una dvision

c = a%b
print("El modulo de {} entre {} es: {}".format(a,b,c))

# Parentesis: Los parentesis sirven para modificar el orden de precedencia, esto por que lo primero en ejecutarse es lo que esta dentro de los parentesis.

d = a+b*a
c = (a+b)*a
print("Si nosotros escribieramos la ecuacion a+b*a el resultado es: {} pero con los parentesis la operacion nos da: {}".format(d,c))