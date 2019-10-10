# Control de Flujo
    
##    Sentencias condicionales
los condicionales nos permiten comprobar condicionantes y hacer que nuestro programa se comporte de una forma u otra, que ejecute un fragmento de código u otro, dependiendo de esta condición.

### if
Aquí es donde utilizamos los tipos booleanos, operadores lógicos y relacionales. La forma más simple de una sentencia condicional es un 'if' ('si' esto, entonces: x) seguido de la condición a evaluar, dos puntos (:) y en la siguiente linea identando, el código a ejecutar en caso de que se cumpla dicha condición.

```python
    hola = 'hola mundo'

    if hola == 'hola mundo':
        hola = 'adios mundo'    
        print(hola)        
```

Ahora, en el mismo caso si la variable 'hola' no guardara la cadena "hola mundo" la condición no se cumpliría y el programa seguiría con su secuencia de ejecución predeterminada; en el caso en donde queramos que el programa ejecute alguna sentencia si no se cumple la condicionante utilizamos un 'else' al final del código de la sentencia, de esta forma:

```python
    hola = 'hola'

    if hola == 'hola mundo':
        hola = 'adios mundo'    
        print(hola)
    else:
        hola = 'hola mundo'
        print('se a asignado correctamente el saludo')
        print(hola)
```

Existe un caso más para la utilización del condicional 'if', este caso es cuando tenemos una serie de condicionales, es decir, cuando queremos que se haga algo si no lo otro, si no esto otro, entonces podemos utilizar 'elif' (contracción de 'else if'), haciendo lo que se conoce como anidacion de condicionales (if anidados), veamos un ejemplo:

```python
    hola = 'hola'

    if hola == 'hola mundo':
        hola = 'adios mundo'    
        print(hola)
    elif hola == 'adios mundo':
        hola = 'ya te vas?'
        print(hola)
    else:
        hola = 'hola mundo'
        print(hola)
```

##    Bucles
mientras que los condicionales nos permiten ejecutar distintos fragmentos de código dependiendo de ciertas condiciones, los bucles nos permiten ejecutar un mismo fragmento de código un cierto numero de veces, mientras se cumpla una determinada condición.

### while
El bucle while (mientras) ejecuta un fragmento de codigo mientras se cumpla una condicion:

```python
    edad = 0 # Inicializamos nuestra variable que servirá de contador

    while edad <= 18: # El bucle se cumplirá hasta que la variable sea mayor a 18
        print('la edad es de: '+ str(edad))
        edad += 1 # Si no aumentamos la variable el bucle sera infinito

    print('Felicidades llegaste a los '+ str(edad))
```

Existen casos en los que se necesita que el bucle infinito funciona de cierta manera, es decir, no finalice hasta que el usuario lo requiera:

```python
    nombres = []

    while True: # al poner True(cierto), el bucle continuara por 'siempre'
        nombre = input(ingresa un nombre (para salir introduce 'ya'): # funcion para introducir por teclado
        if nombre == 'ya':
            break # Esta declaracion nos sacara del bucle
        else:
            nombre.append(nombre)

    print(nombres)
```

En este bucle conocimos dos funciones necesarias pero no obligatorias en los bucles, en este caso creamos una lista de nombres a partir de introducir un nombre a la lista con la función input, dicha función sirve para introducir cadenas por teclado, normalmente se introducen en forma de Strings, pero podemos hacer un casting directo para que el tipo de dato sea entero, flotante o algún otro:

```python
    dato = input('introducir un string')

    dato2 = int(input('introducir dato casteado a entero'))

    dato3 = float(input('introducir dato casteado a flotante'))
```

Otra función que utilizamos en el bucle es break, esta función nos permite salir de cualquier tipo de bucle en la sentencia en donde lo declaremos, posiblemente (si no esta al final del bucle) sin terminar las instruciones restantes dentro del bucle.

De la misma forma existe una función mas que nos sirve en los bucles, hablamos de continue (continuar), esta función nos pasa a la siguiente iteracion del bucle interrumpiendo la ejecución del bucle a partir de donde la declaremos.

### For
La sentencia for (o función) funciona como una forma genérica de iterar sobre una secuencia. como tal intenta facilitar su uso para esta.

```python
    nombres = []

    while True: # al poner True(cierto), el bucle continuara por 'siempre'
        nombre = input(ingresa un nombre (para salir introduce 'ya'): # funcion para introducir por teclado
        if nombre == 'ya':
            break # Esta declaracion nos sacara del bucle
        else:
            nombre.append(nombre)

    print(nombres)

    for nombre in nombres:
        print(nombre)
```

en este caso la secuencia son la lista de nombres y con la función 'for' iteramos sobre cada nombre en este caso para mostrarlos en pantalla uno por uno.

Pero tambien podemos utilizar esta funcion con range, que nos permite ir de un numero a otro, es decir, en un rango especifico, pero esa funcionalidad la veremos en temas posteriores.

[Siguiente: Colecciones](/Colecciones/Colecciones.md)