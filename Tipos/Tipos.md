# Tipos Básicos.

En python los tipos básicos se dividen en:
 
* Números: Como pueden ser enteros(1,2,3,...), de coma flotante(1.1,1.2,1.3,...) o complejos (7+5j)
* Cadenas de texto: Como "Hola mundo"
* Valores Booleanos: True (cierto), False (falso)

Probemos los tipos básicos con el siguiente código:

```python

    #Tipos básicos en Python

    #Números: Enteros
    a = 3 # Asignación de un valor entero a una variable

    print("El valor de la variable a es: ", a)

    #Números: Coma flotante
    b = -1.5 # Asignación de un entero con decimales o de coma flotante

    print('El valor de la vareiable b es: ', str(b))

    #Cadenas de texto
    cadena = "Hola mundo"

    print(cadena)

    cadena2 = 'Hola adios'

    print(cadena2)

    #Valores Booleanos

    x = True

    y = False

    print("El valor de 'x' es: {} y el de 'y' es: {}".format(x,y))

    #Nota: Con la función type() podemos identificar el tipo de una variable

    print(type(a))

    print(type(cadena))

    print(type(x))

```
[codigo](/Tipos/tipos.py)

Como pudimos ver en el codigo anterior existen muchas formas de imprimir por pantalla utilizando la funcion 'print', podemos utilizar la coma seguido de la variable a imprimir, utilizar tambien el simbolo '+' seguido de un casting o la funcion format() como se muestra en los ejemplos. 

[Siguiente: Operadores Aritmeticos](/OperadoresArit/Operadores.md)
