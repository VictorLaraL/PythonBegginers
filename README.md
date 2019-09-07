# Python for Begginers

## Introduccion 

###    ¿Que es python?
Python es un lenguaje de alto nivel, con propósito general de script o interpretado. Fue creado por Van Rossum a principios de los años 90 cuyo nombre esta inspirado en el grupo de cómicos ingleses "Monty Python". Es un lenguaje similar a perle pero con una sintaxis limpia que favorece a un código legible.

###    Interpretado
Un lenguaje interpretado o de script es aquel que se ejecuta utilizando un programa intermedio llamado interprete, en lugar de compilar el código y arrojar un objeto (archivo ejecutable para el SO) el intérprete ejecuta el las ordenes o scrpts, dándonos un resultado lógico.

No obstante python tiene muchas de las caracteristicas de los lenguajes compilados, por lo que se podría decir que es semi interpretado. Al igual que en java y muchos otros lenguajes, el código fuente de python se traduce a un pseudocodigo maquina intermedio llamado bytecode la primera vez que se ejecuta, generando archivos .pyc o .pyo, que son los que se ejecutaran en repetidas ocasiones.

###    Tipado Dinámico
Esta característica se refiere a que no es necesario declarar el tipo de dato que va a contener una determinada variable, sino que su tipo se determinara en tiempo de ejecución según el tipo de valor al que se le asigne y el tipo de esta variable puede cambiar si se le asigna un valor de otro tipo.

###    Fuertemente tipado
No se permite tratar a una variable como si fuera de un tipo distinto al que tiene, es necesario convertir de forma explicita (casting) dicha variable al nuevo tipo previamente.

## Hello wolrd

Como primer acercamiento al lenguaje haremos que nos muestre por pantalla un texto "Hello world" primero desde el interprete en la caja de comandos (shell), lo activamos escribiendo el comando python y despues escribimos el codigo siguiente y oprimimos la tecla enter:

    print('Hello world')

Ahora para crear un fichero abrimos nuestro editor de texto o ID de preferencia y copiamos el código dentro del fichero guardando el fichero con el nombre que deseemos y la extensión .py (Como ejemplo podemos guardarlo con el nombre hola.py). Para ejecutarlo a través de la caja de comandos nos dirigimos a la ruta donde esta el archivo y bastara con escribir el nombre del archivo con su extensión y oprimir la tecla enter.

Nota: Para agregar comentarios en python podemos usar "#" al inicio de la linea de comando y """al inicio y final de un comentario en el que se emplee mas de una linea.

    #Ejemplo de un comentario en una sola linea

    """ Ejemplo de otro comentario
    en mas de una linea """

## Tipos Básicos

En python los tipos básicos se dividen en:
 
* Numeros: Como pueden ser enteros(1,2,3,...), de coma flotante(1.1,1.2,1.3,...) o complejos (7+5j)
* Cadenas de texto: Como "Hola mundo"
* Valores Booleanos: True (cierto), False (falso)

Probemos los tipos basicos con el siguiente codigo:

    #Tipos basicos en Python

    #Numeros: Enteros
    a = 3 # Asignacion de un valor enteroa una variable

    print("El valor de la variable a es: ", a)

    #Numeros: Coma flotante
    b = -1.5 # Asignacion de un entero con decimales o de coma flotante

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

    #Nota: Con la funcion type() podemos identificar el tipo de una variable

    print(type(a))

    print(type(cadena))

    print(type(x))

## Operadores aritméticos

Los operadores aritméticos binarios son aquellos que necesitan de dos números y al aplicarles una operación dan como resultado un tercer numero. 

###    Precedencia de operadores
El orden de presendencia de ejecucion de los operadores aritmeticos es:
1. Exponente: **
2. negacion: -
3. Multiplicacion, division, division entera, modulo: *,/,//,%
4. suma, resta: +,-}

VEamos como funciona la precedencia de operaciones con el codigo siguiente: 

    #Operadores en python

    a,b = 10,6 # Definimos dos variables para utilizar los operadores

    #Para mostrar por pantalla (imprimir) alguna operacion lo podemos hacer de dos maneras, la primera con la operacion suma:

    print(a+b)

    #O almacenandola en otra variable

    c = a+b
    print(c)

    #Resta

    print("la resta de {} menos {} es: {}".format(a,b,a-b))

    #Multiplicacion

    c = a*b
    print("La multiplicacion de las dos variables es: ", str(c))

    #Division

    c = a/b
    print(" la division de las variables es: ", str(c))

    #Exponente

    print(a**2)

    #Modulo: La operacion modulo devuelve el residuo de una dvision

    c = a%b 
    print("El modulo de {} entre {} es: {}".format(a,b,c))

    #Parentesis: Los parentesis sirven para modificar el orden de precedencia, esto por que lo primero en ejecutarse es lo que esta dentro de los parentesis.

    d = a+b*a
    c = (a+b)*a
    print("Si nosotros escribieramos la ecuacion a+b*a el resultado es: {} pero con los parentesis la operacion nos da: {}".format(d,c))

## Colecciones
Ya que en python todo son objetos, las colecciones resultan ser un tipo de dato en el que se almacena información de cierta forma estructurada, en python encontramos las 3 mas básicas: Listas, Tuplas y diccionarios.

###    Listas
Es un tipo de colección ordenada. Seria el equivalente a un array o vector en otros lenguajes.


    #Listas: Pueden contener cualquier tipo de datos, incluido mas listas

    li = [1,2.5,'hola',True] # Cada elemento es separado por una coma

    #Para conocer el contenido de una lista podemos imprimirla con el metodo print
    print(li)

    #Ademas tambien podemos imprimir algun valor dentro de la vista buscandolo de la siguiente forma:

    print(li[0])

    print(li[3])

    #En este caso nuestra lista tiene 4 elementos por lo que iniciamos contando con 0 hasta 3

    #Cuando tenemos una lista dentro de otra la manera de buscar algun elemento es la siguiente:

    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista3 = [7,8,9]
    lista_index = [lista1, lista2, lista3] # En este caso en especifico podemos ver esta estructura como una matriz

    print(lista_index[0][0])
    print(lista_index[0][1])
    print(lista_index[0][2])

    print(lista_index)

###    Tuplas
También es un tipo de colección ordenada al igual de las listas pero con las siguientes características.

    #Tuplas: Todo lo explicado anteriormente aplica para las tuplas exxcepto la forma de definirlas mediante los parentesis ()

    tupla = (1,2.5,"Python", False)

    print(tupla)

    #Para las tuplas de un elemento es necesario utilizar la coma despues del elemento

    tup = (1,)

    print(type(tup))

    #Esto ocurre por que el constructor de la tupla es la coma y no el parentesis.

    #A diferencia de las listas las tuplas son inmutables y de un tamaño fijo lo que permite el ahorro de memoria


###    Dicionarios
Los diccionarios funcionan asociando claves con valores


    #Diccionarios: A diferencia de los dos tipos anteriores de colecciones los diccionarios no tienen un orden, estos cuentan con claves y valores, asociados entre si

    dic = {"1":"hola", "2":"mundo"} # El primer valor se trata de la clave y el segundo del valor asociado a esta clave

    print(dic)

    #Para buscar un valor en especifico se llama a travez de su clave de esta forma:
    print(dic["1"])
    print(dic["2"])

    #Al igual que las listas estos pueden ser modificados:

    dic["1"] = "adios"
    print(dic["1"])


## Control de Flujo
    
###    Sentencias condicionales
los condicionales nos permiten comprobar condiciones y hacer que nuestro programa se comporte de una forma u otra, que ejecute un fragmento de código u otro, dependiendo de esta condición.

Aquí es donde utilizamos los tipos booleanos, operadores lógicos y relacionales. La forma mas simple de un estamento condicional es un if (del ingles si) seguido de la condición a evaluar, dos puntos (:) y en la siguiente linea identando, el código a ejecutar en caso de que se cumpla dicha condición.


    hola = 'hola mundo'

    if hola == 'hola mundo':
        hola = 'adios mundo'    
        print(hola)        

ahora en el mismo caso, si la variable hola no guardara 'hola mundo' la condición no se cumpliría y el programa seguiría con su secuencia de ejecución,en el caso de que querramos que el programa algo si no se cumple deberíamos utilizar un else al final del código de la sentencia, de esta forma:

    hola = 'hola'

    if hola == 'hola mundo':
        hola = 'adios mundo'    
        print(hola)
    else:
        hola = 'hola mundo'
        print('se a asignado correctamente el saludo')
        print(hola)

Existe un caso mas para la utilización del condicional if, este caso es cuando tenemos una serie de condicionales, es decir, cuando queremos que se haga algo sino lo otro sino esto otro, para ese caso podemos utilizar elif (contracción de else if), haciendo lo que se conoce como anidacion de condicionales (if anidados), veamos un ejemplo:

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

###    Bucles
mientras que los condicionales nos permiten ejecutar distintos fragmentos de código dependiendo de ciertas condiciones, los bucles nos permiten ejecutar un mismo fragmento de código un cierto numero de veces, mientras se cumpla una determinada condición.

while: el bucle while (mientras) ejecuta un fragmento de codigo mientras se cumpla una condicion:

    edad = 0 # Inicializamos nuestra variable que servirá de contador

    while edad <= 18: # El bucle se cumplirá hasta que la variable sea mayor a 18
        print('la edad es de: '+ str(edad))
        edad += 1 # Si no aumentamos la variable el bucle sera infinito

    print('Felicidades llegaste a los '+ str(edad))

Existen casos en los que se necesita que el bucle infinito funciona de cierta manera, es decir, no finalice hasta que el usuario lo requiera:

    nombres = []

    while True: # al poner True(cierto), el bucle continuara por 'siempre'
        nombre = input(ingresa un nombre (para salir introduce 'ya'): # funcion para introducir por teclado
        if nombre == 'ya':
            break # Esta declaracion nos sacara del bucle
        else:
            nombre.append(nombre)

    print(nombres)

En este bucle conocimos dos funciones necesarias pero no obligatorias en los bucles, en este caso creamos una lista de nombres a partir de introducir un nombre a la lista con la función input, dicha función sirve para introducir cadenas por teclado, normalmente se introducen en forma de Strings, pero podemos hacer un casting directo para que el tipo de dato sea entero, flotante o algún otro:

    dato = input('introducir un string')

    dato2 = int(input('introducir dato casteado a entero'))

    dato3 = float(input('introducir dato casteado a flotante'))

Otra función que utilizamos en el bucle es break, esta función nos permite salir de cualquier tipo de bucle en la sentencia en donde lo declaremos, posiblemente (si no esta al final del bucle) sin terminar lo restante del bucle.

De la misma forma existe una función mas que nos sirve en los bucles, hablamos de continúe (continuar), esta función nos pasa a la siguiente iteracion del bucle interrumpiendo la ejecución del bucle a partir de donde la declaremos.

For: La sentencia for (o función) funciona como una forma genérica de iterar sobre una secuencia. como tal intenta facilitar su uso para esta.

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

en este caso la secuencia son la lista de nombres y con la función for iteramos sobre cada nombre en este caso para mostrarlos en pantalla uno por uno.

Pero tambien podemos utilizar esta funcion con range, que nos permite ir de un numero a otro, es decir, en un rango especifico, pero esa funcionalidad la veremos despues del tema de funciones.

## Funciones
      
una función es un fragmento de código con un nombre asignado que realiza una serie de tareas y devuelve un valor. A los fragmentos de código que tienen un nombre asociado y no devuelven valores se les suele llamar procedimientos. En python no existen los procedimientos puesto que cuando a una función no le especificamos un valor de retorno la función devuelve un valor None (nada), equivalente a un Null.

Las funciones aportan características como la reutilizacion y ayudan en la depuración del código, al particionar nuestro código en diferentes funciones es mas fácil de leer y ayuda a encontrar posibles errores.

En python las funciones se declaran de la siguiente forma:

    def mi_funcion(param1, param2):
        print(param1)
        print(param2)

A la hora de declarar una función se comienza con la palabra reservada def seguido del nombre de nuestra función (en minúsculas como buena practica) y entre paréntesis los argumentos a pasar separados por comas. A continuación después de los dos puntos y con su debida identacion, en otra linea, escribimos el código que queremos que ejecute dicha función.

para poder utilizar dicha función la forma de utilizarla es llamarla:

    mi_funcion(param1, param2)

Podemos llamar a la función en cualquier parte del código siempre y cuando le pasemos los parámetros que nos pida.

el paso de parámetros es en el mismo orden en que la declaramos, aunque podríamos pasarlos desordenamos pero especificando el nombre del parámetro al que le asociamos el valor.

    mi_funcion(param2 = 2, param1 = 'hola'

veamos un ejemplo mas interesante utilizando lo ya aprendido

    nombres = []
    apellidos = []


    def lista_nombres(nombre, apellido):
        '''
        Funcion que recibe un nombre y un apellido, verifica
        que no sean vacios y los almacena en dos listas diferentes
        '''
        if nombre != None and apellido != None: # Deben cumplirse ambos casos
            nombres.append(nombre)
            apellidos.append(apellido)
        else:
            print('El nombre o apellido es vacio')


    print('para dejar de escribir nombres igresa la letra "x" \n') # Condicion de paro


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

En el ejemplo anterior primero tenemos una función que recibe dos parámetros y después de verificar que no sean vacíos los almacena en dos listas previamente declaradas. Después entramos a un bucle donde podemos ingresar nombres con apellidos separados por un espacio para enviarlos a la función, haciendo uso de la función split podemos separar el nombre del apellido y meterlo a una lista, una vez creada la lista sabemos que el primer elemento es el nombre y el segundo el apellido así que en ese orden lo mandamos a la función. en caso de escribir x nos saldremos del bucle. Fuera del bucle entramos a otro bucle for donde utilizamos la funcion range, esta funcion recibe un entero que toma como el numero a recorrer desde 0 hasta el numero que le asignamos, por eso utilizamos la funcion len, esta funcion nos devuelve el numero de elementos que tenemos en la lista, entonces la funcion range ira de 0 hasta lo que devuelva len y se le asignara a la variable i o j dependiendo el bucle en el que estemos.

en las funciones de igual manera podemos hacer que reciban un numero n de parametros utilizando el operador (*) antes del nombre, esto nos creara una tupla que almacenara los valores que le hayamos pasado a la función: 

    def funcion_nparam(*param):
        print(nparam)

    funcion_nparam(1,2,3,'hola')

o en otros casos podemos pasar una cantidad n de datos pero sujetos a una clave, de la misma forma que lo hacemos en un diccionario y de hecho se almacenan en un diccionario:

    def funcion_nparam(**param):
        print(param)

    funcion_nparam = (primero = 1, segindo = 2, tercero = 3)

Como ultimo aspecto a revisar en cuanto a las funciones, queda explicar el paso de parametros, si lo hacen por valor o por referencia. En el paso por referencia se hace paso de una referencia o puntero a la variable, es decir, la dirección de memoria donde se encuentra dicha variable y no su contenido en si. En el paso por valor, por el contrario, lo que se pasa como argumento es una copia del valor de dicha variable.

La diferencia entre estos dos conceptos radica en las variables locales y globales. Toda variable que se declare fuera de una función o clase se le considera global puesto que se puede utilizar en todo el código restante a partir de su aparición, a diferencia de las variables locales, estas se encuentran contenidas en las funciones o clases (para ser mas específicos en las instancias de las clases) y su funcionamiento se limita dentro de la misma función o clase.

Entonces volviendo al paso de parámetros, cuando hacemos un pase por referencia de la variable global esta se vera modificada en la función, mientras que si hacemos un paso por valor de la variable esta se clonara guardara en otro espacio de memoria, por tanto no se vera modificada por la función.

En python el paso de parámetros a una función es por un tipo de referencia, pero recordemos que existen objetos que son inmutables como las tuplas, por lo que si quisiéramos hacer un cambio en un elemento de la tupla, este no se modificaría. 

    def f(x,y):
        x = x+3
        y.append(23)
        print(x,y)

    x = 22
    y = [22]

    f(x,y)

    print(x,y)

    #El resultado de esta ejecución seria 25[22,23] y 22[22,23]

como vemos cundo salimos de la función la variable x no conserva los cambios una vez salimos de la función por que los enteros son inmutables en python, sin embargo la variable y si los conserva. 

## Fuentes / Material apoyo
* https://www.whoishostingthis.com/resources/programming/#python
* Python Para Todos - Raul Gonzales Duque.


