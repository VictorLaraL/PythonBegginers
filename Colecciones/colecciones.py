# Colecciones en Python

# Listas: Pueden contener cualquier tipo de datos, incluido mas listas

li = [1,2.5,'hola',True] # Cada elemento es separado por una coma

# Para conocer el contenido de una lista podemos imprimirla con el metodo print
print(li) 

# Ademas tambien podemos imprimir algun valor dentro de la vista buscandolo de la siguiente forma:

print(li[0])

print(li[3])

# En este caso nuestra lista tiene 4 elementos por lo que iniciamos contando con 0 hasta 3

# Cuando tenemos una lista dentro de otra la manera de buscar algun elemento es la siguiente:

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [7,8,9]
lista_index = [lista1, lista2, lista3] # En este caso en especifico podemos ver esta estructura como una matriz

print(lista_index[0][0])
print(lista_index[0][1])
print(lista_index[0][2])

print(lista_index)

# Para modificar algun elemento de la lista igual podemos utilizar el operador []

l = [1,99]

print(l) # En este caso en la posicion 0 de la lista esta el elemento 1

l[0] = 100

print(l) # Ahora al asignarle otro valor el elemento 0 de la lista ahora es 100

# Tuplas: Todo lo explicado anteriormente aplica para las tuplas exxcepto la forma de definirlas mediante los  parentesis ()

tupla = (1,2.5,"Python", False)

print(tupla)

# Para las tuplas de un elemento es necesario utilizar la coma despues del elemento

tup = (1,)

print(type(tup))

# Esto ocurre por que el constructor de la tupla es la coma y no el parentesis.

# A diferencia de las listas las tuplas son inmutables y de un tamaño fijo lo que permite el ahorro de memoria

# Diccionarios: A diferencia de los dos tipos anteriores de colecciones los diccionarios no tienen un orden, estos cuentan con claves y valores, asociados entre si

dic = {"1":"hola", "2":"mundo"} # El primer valor se trata de la clave y el segundo del valor asociado a esta clave

print(dic)

# Para buscar un valor en especifico se llama a travez de su clave de esta forma:
print(dic["1"])
print(dic["2"])

# Al igual que las listas estos pueden ser modificados:

dic["1"] = "adios"
print(dic["1"])