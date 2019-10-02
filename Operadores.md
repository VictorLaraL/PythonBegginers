# Operadores aritméticos

Los operadores aritméticos binarios son aquellos que necesitan de dos números y al aplicarles una operación dan como resultado un tercer número. 

##    Precedencia de operadores
El orden de presendencia de ejecución de los operadores aritméticos es:
1. Exponente: **
2. Negación: -
3. Multiplicación, Division, División Entera, Módulo: *,/,//,%
4. Suma, Resta: +,-}

Veamos cómo funciona la precedencia de operaciones con el código siguiente: 

    #Operadores en python

    a,b = 10,6 # Definimos dos variables para utilizar los operadores

    #Para mostrar por pantalla (imprimir) alguna operación lo podemos hacer de dos maneras, la primera con la operación suma:

    print(a+b)

    #O almacenandola en otra variable

    c = a+b
    print(c)

    #Resta

    print("la resta de {} menos {} es: {}".format(a,b,a-b))

    #Multiplicación

    c = a*b
    print("La multiplicacion de las dos variables es: ", str(c))

    #División

    c = a/b
    print(" la division de las variables es: ", str(c))

    #Exponente

    print(a**2)

    #Módulo: La operación módulo devuelve el residuo de una dvisión

    c = a%b 
    print("El modulo de {} entre {} es: {}".format(a,b,c))

    #Paréntesis: Los paréntesis sirven para modificar el orden de precedencia, esto por que lo primero en ejecutarse es lo que está dentro de los parentesis.

    d = a+b*a
    c = (a+b)*a
    print("Si nosotros escribieramos la ecuación a+b*a el resultado es: {} pero con los paréntesis la operación nos da: {}".format(d,c))
