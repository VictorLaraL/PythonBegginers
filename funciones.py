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
    nombre_completo = input('ingresa un nombre y separado por un espacio el apellido: \n>')
    if nombre_completo != 'x' :
        nombre_ap = nombre_completo.split() # Regresa una lista [nombre, apellido]
        lista_nombres(nombre_ap[0],nombre_ap[1])
    else:
        break

print('\nla lista de nombres es: ')
for i in range(len(nombres)):
    for j in range(len(apellidos)):
        if i == j:
            print('nombre: {} |apellido: {}'.format(nombres[i],apellidos[j]))
        else:
            continue

    


