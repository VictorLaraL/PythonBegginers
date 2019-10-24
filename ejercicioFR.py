''' 
Ejercicio para la creacion de una lista de alumnos con sus respectivas caificaciones del semestre: 
*   Ingresaremos el nombre de pila del alumno y su primer apellido, seguido de el numero de materias que llevo en el semestre. 
    [el numero de materias debe ser mayor a 0]
*   Pediremos la calificacion de cada materia y calcularemos su promedio de ese semestre si es mayor a 70
    almacenaremos TRUE y si es menor a 70 FALSE.[las calificaciones no pueden ser negativas ni estar por encima del 100, pero si 
    pueden ser 0] 
*   Los datos los almacenaremos en una lista (nombre, apellido, calificacion, A/R) y al final crearemos una lista de     
    alumnos. [la lista de alumnos debe estar en un dicionario y la clave de cada alumno sera su nombre] 
*   El main contendra el menu para agregar los alumnos que el usuario desee hasta que se interrumpa la ejecucion         
    ingresando xxx en el nombre del alumno.
*   Una vez dejemos de ingresar los datos el programa, se ejecutara la lista de alumnos con sus respectivos datos.
    [los datos que deben aparecer deben ser de esta forma: nombre    apellido    calificacion    A/R]
*   El ejercicio lo ejecutaremos en funciones:'''

listaAlumnos = {}

def agregarAlumno(alumno):
    listaAlumnos[alumno[0]] = alumno

def calculoPromedio(calificaciones):
    calTotal = 0
    for calificacion in calificaciones:
        calTotal += calificacion
    return calTotal/len(calificaciones)

while True:
    
    nombre = input('ingresa el primer nombre del alumno: \n>') 
    if nombre == 'xxx': # Comprobacion del parametro de salida
        break

    apellido = input('ingresa el primer apellido del alumno: \n>')
    
    matSemestre = int(input('ingresa la cantidad de materias del alumno: \n>'))
    if matSemestre <= 0 : # Comprobacion de materias
        print('Lo sentimos pero el alumno debe llevar por lo menos 1 materia!')
        continue
    
    calMaterias = []

    for x in range(1, matSemestre+1):
        calificacion = int(input('ingresa la calificacion de la materia {} : '.format(x)))
        calMaterias.append(calificacion)

    promedio = calculoPromedio(calMaterias)

    if promedio >= 70 :
        agregarAlumno([nombre, apellido, promedio, 'A'])
    elif promedio < 70 :
        agregarAlumno([nombre, apellido, promedio, 'R'])
    
for alumno in listaAlumnos.values(): 
    print('{} \t\t {} \t\t {} \t\t {}'.format(alumno[0], alumno[1], alumno[2], alumno[3])) 

