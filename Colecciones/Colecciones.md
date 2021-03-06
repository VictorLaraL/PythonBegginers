# Colecciones.
Las colecciones resultan ser un tipo de dato en el que se almacena información, de cierta forma estructurada, en python encontramos las 3 mas básicas: Listas, Tuplas y diccionarios.

## Listas.
Es un tipo de colección ordenada. Sería el equivalente a un array o vector en otros lenguajes.

```python
    #Listas: Pueden contener cualquier tipo de datos, incluyendo otras listas.

    li = [1,2.5,'hola',True] # Cada elemento es separado por una coma.

    #Para conocer el contenido de una lista podemos imprimirla con el metodo print
    print(li).

    #Además, también, podemos imprimir algún valor dentro de la vista buscándolo de la siguiente forma:

    print(li[0])

    print(li[3])

    #En este caso, nuestra lista tiene 4 elementos, por lo que, iniciamos contando con 0 hasta 3

    #Cuando tenemos una lista dentro de otra la manera de buscar algún elemento es la siguiente:

    lista1 = [1,2,3]
    lista2 = [4,5,6]
    lista3 = [7,8,9]
    lista_index = [lista1, lista2, lista3] # En este caso en específico podemos ver esta estructura como una matriz.

    print(lista_index[0][0])
    print(lista_index[0][1])
    print(lista_index[0][2])

    print(lista_index)
```

## Tuplas.
También es un tipo de colección ordenada al igual que las listas, pero con las siguientes características.

```python
    #Tuplas: Todo lo explicado anteriormente aplica para las tuplas, excepto la forma de definirlas mediante los paréntesis ()

    tupla = (1,2.5,"Python", False)

    print(tupla)

    #Para las tuplas de un elemento es necesario utilizar la coma después del elemento

    tup = (1,)

    print(type(tup))

    #A diferencia de las listas, las tuplas son inmutables y de un tamaño fijo lo que permite el ahorro de memoria.
```

## Dicionarios.
Los diccionarios funcionan asociando claves con valores.

```python
    #Diccionarios: A diferencia de los dos tipos anteriores de colecciones los diccionarios no tienen un orden, estos cuentan con claves y valores, asociados entre sí.

    dic = {"1":"hola", "2":"mundo"} # El primer valor se trata de la clave y, el segundo, del valor asociado a esta clave.

    print(dic)

    #Para buscar un valor en específico se llama a través de su clave de esta forma:
    print(dic["1"])
    print(dic["2"])

    #Al igual que las listas estos pueden ser modificados:

    dic["1"] = "adios"
    print(dic["1"])
```

## Funciones para Listas
Dentro de las colecciones (listas y en algunos casos tuplas), nos encontramos con una serie de metodos especiales que nos siren para un mejor manejo de estas estructuras de datos.

### len()
Este metodo nos regresa la canitidad de elementos en nuestra lista o tupla en forma de un entero.

```python
lista = [1,2,3,'hola','adios']

print('la cantidad de elementos en nuestra lista son: ', len(lista))
```

### append()
Metodo que nos sirve para agregar elementos a nuestra lista o tupla

```python
lista = [1,2,3,hola,adios]

hola = 4

lista.append(hola)

lista.append('buenos dias')
```

### split()
Metodo que nos sirve para dividir una cadena de texto de acuerdo al parametro que usemos para dividirla, el parametro se pasa por el operador () y nos devuelve una lista con la cadena separada, es decir, cada valor de la lista es una parte de la cadena.

```python
hola = 'hola, mundo, maldito'
palabras = hola.split(,)

print(palabras)

for palabra in palabras:
    print(palabra)
```

[Codigo](/Colecciones/colecciones.py)

[Siguiente: Control de Flujo](/ControlFlujo/ControlFlujo.md)