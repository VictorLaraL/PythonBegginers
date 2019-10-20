
# Funciones.
      
Una función es un fragmento de código con un nombre asignado que realiza una serie de tareas y devuelve un valor. A los fragmentos de código que tienen un nombre asociado y no devuelven valores se les suele llamar procedimientos. En python no existen los procedimientos puesto que cuando a una función no le específicamos un valor de retorno la función devuelve un valor None (nada), equivalente a un NULL.

Las funciones aportan características como la reutilización y ayudan en la depuración del código, al particionar nuestro código en diferentes funciones es más fácil de leer y ayuda a encontrar posibles errores.

En python las funciones se declaran de la siguiente forma:

```python
    def mi_funcion(param1, param2):
        print(param1)
        print(param2)
```

A la hora de declarar una función se comienza con la palabra reservada def seguido del nombre de nuestra función (en minúsculas como buena práctica) y entre paréntesis los argumentos a pasar separados por comas. A continuación después de los dos puntos y con su debida identación, en otra línea, escribimos el código que queremos que ejecute dicha función.

Para poder utilizar dicha función la forma de utilizarla es llamarla:

```python
    mi_funcion(param1, param2)
```
Podemos llamar a la función en cualquier parte del código siempre y cuando le pasemos los parámetros que nos pida.

El paso de parámetros es, en el mismo orden, en que la declaramos, aunque podríamos pasarlos desordenados, pero especificando el nombre del parámetro al que le asociamos el valor.

```python
    mi_funcion(param2 = 2, param1 = 'hola')
```

Veamos un ejemplo más interesante utilizando lo ya aprendido:

```python
    nombres = []
    apellidos = []


    def lista_nombres(nombre, apellido):
        '''
        Función que recibe un nombre y un apellido, verifica
        que no sean vacíos y los almacena en dos listas diferentes
        '''
        if nombre != None and apellido != None: # Deben cumplirse ambos casos
            nombres.append(nombre)
            apellidos.append(apellido)
        else:
            print('El nombre o apellido es vacío')


    print('para dejar de escribir nombres igresa la letra "x" \n') # Condición de paro.


    while True:
        nombre_completo = input('ingresa un nombre y separado por un espacio el         apellido: \n>')
        if nombre_completo != 'x' :
            nombre_ap = nombre_completo.split() # Regresa una lista [nombre, apellido]
            lista_nombres(nombre_ap[0],nombre_ap[1])
        else:
            break


    print('\nla lista de nombres es: ')
    for i in range(len(nombres)):
        for j in range(len(apellidos)):
            if i == j:
                print('nombre: {} | apellido: {}'.format(nombres[i],apellidos[j]))
            else:
                continue
```
[Código.](/Funciones/funciones.py)

En el ejemplo anterior primero tenemos una función que recibe dos parámetros y después de veríficar que no sean vacíos los almacena en dos listas previamente declaradas. Después entramos a un bucle donde podemos ingresar nombres con apellidos separados por un espacio para enviarlos a la función, haciendo uso de la función 'split' podemos separar el nombre del apellido y meterlo a una lista, una vez creada la lista sabemos que el primer elemento es el nombre y el segundo el apellido, así que, en ese orden lo mandamos a la función. En caso de escribir x nos saldremos del bucle. Fuera del bucle entramos a otro bucle, for, donde utilizamos la función 'range', esta función recibe un entero que toma como el número a recorrer desde 0 hasta el número que le asignamos, por eso utilizamos la función 'len', esta función nos devuelve el número de elementos que tenemos en la lista, entonces, la función 'range' irá de 0 hasta lo que devuelva 'len' y se le asignará a la variable i o j dependiendo el bucle en el que estemos.

En las funciones, de igual manera, podemos hacer que reciban un número n de parámetros utilizando el operador (*) antes del nombre, esto nos creará una tupla que almacenará los valores que le hayamos pasado a la función: 

```python
    def funcion_nparam(*param):
        print(nparam)

    funcion_nparam(1,2,3,'hola')
```

O en otros casos, podemos pasar una cantidad n de datos pero sujetos a una clave, de la misma forma que lo hacemos en un diccionario y de hecho se almacenan en un diccionario:

```python
    def funcion_nparam(**param):
        print(param)

    funcion_nparam = (primero = 1, segindo = 2, tercero = 3)
```

Como último aspecto a revisar en cuanto a las funciones, queda explicar el paso de parámetros, si lo hacen por valor o por referencia. En el paso por referencia se hace paso de una referencia o puntero a la variable, es decir, la dirección de memoria donde se encuentra dicha variable y no su contenido en sí. En el paso por valor, por el contrario, lo que se pasa como argumento es una copia del valor de dicha variable.

La diferencia entre estos dos conceptos radica en las variables locales y globales. Toda variable que se declare fuera de una función o clase se le considera global puesto que se puede utilizar en todo el código restante a partir de su aparición, a diferencia de las variables locales, estas se encuentran contenidas en las funciones o clases (para ser más específicos en las instancias de las clases) y su funcionamiento se limita dentro de la misma función o clase.

Entonces, volviendo al paso de parámetros, cuando hacemos un pase por referencia de la variable global, esta se vera modificada en la función, mientras que, si hacemos un paso por valor de la variable esta se clonará y guardará en otro espacio de memoria, por tanto, no se verá modificada por la función.

En python el paso de parámetros a una función es por un tipo de referencia, pero recordemos que existen objetos que son inmutables como las tuplas, por lo que, si quisiéramos hacer un cambio en un elemento de la tupla, este no se modificaría. 

```python
    def f(x,y):
        x = x+3
        y.append(23)
        print(x,y)

    x = 22
    y = [22]

    f(x,y)

    print(x,y)

    #El resultado de esta ejecución sería 25[22,23] y 22[22,23]
```

Como vemos, cundo salimos de la función, la variable x no conserva los cambios una vez que salimos de la función, porque los enteros son inmutables en python, sin embargo, la variable 'y' sí los conserva. 
