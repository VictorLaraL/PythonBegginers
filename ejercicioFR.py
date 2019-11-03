https://www.evernote.com/l/AkCI-zSv-oxCS4uaehwJ3wAeaW8P5HmX4v8/

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
    
for alumno in listaAlumnos.values(): # llamamos a los valores del diccionario que en este caso son listas por eso accedemos en indices
    print('{} \t\t {} \t\t {} \t\t {}'.format(alumno[0], alumno[1], alumno[2], alumno[3])) 

