# Colecciones.
Las colecciones resultan ser un tipo de dato en el que se almacena información, de cierta forma estructurada, en python encontramos las 3 mas básicas: Listas, Tuplas y diccionarios.

##    Listas.
Es un tipo de colección ordenada. Sería el equivalente a un array o vector en otros lenguajes.

```python
    #Listas: Pueden contener cualquier tipo de datos, incluyendo otras listas.

    li = [1,2.5,'hola',True] # Cada elemento es separado por una coma.

    #Para conocer el contenido de una lista podemos imprimirla con el metodo print
    print(li).

    #Ademas también podemos imprimir algún valor dentro de la vista buscándolo de la siguiente forma:

    print(li[0])

    print(li[3])

    #En este caso nuestra lista tiene 4 elementos por lo que iniciamos contando con 0 hasta 3

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

##    Tuplas.
También es un tipo de colección ordenada al igual de las listas pero con las siguientes características.

```python
    #Tuplas: Todo lo explicado anteriormente aplica para las tuplas excepto la forma de definirlas mediante los parentesis ()

    tupla = (1,2.5,"Python", False)

    print(tupla)

    #Para las tuplas de un elemento es necesario utilizar la coma después del elemento

    tup = (1,)

    print(type(tup))

    #A diferencia de las listas, las tuplas son inmutables y de un tamaño fijo lo que permite el ahorro de memoria
```

##    Dicionarios.
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

[Codigo](/Colecciones/colecciones.py)

[Siguiente: Funciones](/Funciones/Funciones.md)
