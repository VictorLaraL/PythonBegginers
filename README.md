# Python for Begginers

## Introduccion 

###    ¿Qué es python?
Python es un lenguaje de alto nivel de tipo interpretado utilizado comunmente para la creación de scripts. Fue creado por el científico de la computación Guido Van Rossum a principios de los años 90; el nombre del lenguaje está inspirado en el grupo de cómicos ingleses "Monty Python". Es un lenguaje similar a Perl pero se concentra más en una sintaxis limpia y en la fácil lectura del código.

###    Interpretado
Un lenguaje interpretado o de 'script' es aquel que se ejecuta utilizando un programa intermedio llamado intérprete; en lugar de compilar el código y retornar un objeto (archivo ejecutable para el SO) el intérprete ejecuta las ordenes o scripts, dándonos un resultado lógico.

Sin embargo, Python tiene muchas características de los lenguajes compilados, por lo que se podría decir que es 'semi-interpretado' dado que al igual que en Java y muchos otros lenguajes no interpretados el código fuente de Python se traduce a un pseudocódigo máquina intermedio llamado 'bytecode' que al ejecutarse por primera vez genera archivos .pyc o .pyo, que son los que se ejecutaran en repetidas ocasiones posteriores.

###    Tipado Dinámico
Esta característica se refiere a que no es necesario declarar el tipo de dato que va a contener una determinada variable, sino que su tipo se determinara en tiempo de ejecución según el tipo de valor que se le asigne. Adicionalmente, el tipo de esta variable puede cambiar si se le asigna un tipo de valor distinto.

###    Fuertemente tipado
No se permite tratar a una variable como si fuera de un tipo distinto al que tiene, es necesario convertir de forma explícita (casting) dicha variable al nuevo tipo previamente.

## Hello wolrd

Como primer acercamiento al lenguaje haremos que imprima el texto "Hello world" en pantalla. 

En primer lugar lo haremos desde el intérprete en la caja de comandos (shell).
Lo activamos escribiendo el comando 'python' y después escribimos el código siguiente:

    print('Hello world')

Al finalizar, presionamos la tecla 'enter'. 

Ahora para crear un fichero abrimos nuestro editor de texto o IDE de preferencia y copiamos el código dentro de él, guardando el fichero con el nombre que deseemos y la extensión '.py' (por ejemplo: 'hola.py'). Posteriormente, podemos ejecutar el código a través de la caja de comandos dirigiéndonos a la dirección donde está el archivo y bastará con escribir el nombre de este con su extensión y oprimir la tecla 'enter'.

Nota: Para agregar comentarios en python podemos usar "#" al inicio de la línea de comando y """al inicio y final de un comentario en el que se emplee más de una línea.

    #Ejemplo de un comentario en una sola línea

    """ Ejemplo de otro comentario
    en mas de una línea """

## Temas

[Tipos](/pythonBegginers/Tipos/Tipos.md)

[Operadores Aritmeticos](/pythonBegginers/OperadoresArit/Operadores.md)

[Control de Flujo](/pythonBegginers/ControlFlujo/ControlFlujo.md)

[Funciones](/pythonBegginers/Funciones/Funciones.md)

##   Material apoyo
* https://www.whoishostingthis.com/resources/programming/#python
* https://www.w3schools.com/python/default.asp


