#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime
''' KC_EJ32
Crear una clase Módulo con los siguientes atributos: 
    ListadoAlumnos, fechaInicio, fechaFin. 

El listado de alumnos deberá ser tipo Lista y contener objetos de tipo Alumno creado en el ejercicio KC_EJ31.

En la misma clase Módulo deberá implementar métodos para 
    agregar objetos Alumno a la Lista
    buscar un alumno 
    mostrar todos los alumnos con estatusInscrito == True.
'''

class Alumno():
    #Atributos con Valores iniciales:
    numeroMatricula = 0
    nombre = ''
    apellido = ''
    email = ''
    estatusInscrito = False


    #constructores
    def __init__(self, numMatricula, nombre, apellido, email, estatusInscrito):
        self.numMatricula = numMatricula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.estatusInscrito = estatusInscrito

class Modulo(Alumno):
    #Atributos
    listadoAlumnos = []
    fechaInicio = datetime.now() #Fecha actual
    fechaFin = datetime(2019, 2, 28) #Año, mes, dia


    #constructores
    def __init__(self, listadoAlumnos, fechaInicio, fechaFin):
        #constructor por default, iniciliza el listado de alumnos 
        # (10 objetos ahora fijos, se asume que se leerán de una BD, o un servicio)
        for a in range(0, 10):
            self.listadoAlumnos.append(Alumno(a, 'Alumno ' + str(a), 'Apellido ' + str(a), 'correo'+str(a)+'@gmail.com', True))

        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin

    #método para agregar nuevos alumnos
    def agregarAlumno(self,alumno):
        self.listadoAlumnos.append(alumno)

    #Metodo para mostrar todos los alumnos con estatusInscrito == True
    def inscritosTrue(self,inscritos):
        apuntados = True


    #método para buscar alumnos por matrícula
    def busarAlumByMatricula(self,matricula):
        encontradaMatricula = False
        for a in self.listadoAlumnos:
            if a.numMatricula == matricula:
                print('Encontrada Matricula: su nombre es {}  y su email: {}').format(a.matricula,a.email)
                encontradaMatricula = True
                break
        if encontradaMatricula == False:
            print('No se encontro alumno con esa matricula')

    #Metodo para mostrar todos los alumnos con estatusInscrito == True
    def inscritosTrue(self,inscritos):
        for a in self.listadoAlumnos:
            if a.estatusInscrito == True:
                print('Matricula: {}, Nombre: {}, Apellido: {}, email: {}'.format(a.numMatricula, a.nombre, a.apellido, a.email))

#Creacion de Objetos (self, numMatricula, nombre, apellido, email, estatusInscrito):
al1 = Modulo(15,'Javier', 'Antúnez', 'antunez19@gmail.com', True)
al2 = Modulo(16,'Ramon', 'Maldonado', 'maldonado@gmail.com', False)
al3 = Modulo(18,'Jessica', 'Neves', 'antunez19@gmail.com', True)

lista=[al1,al2,al3]

al1.busarAlumByMatricula()

'''
%Debug z.py
Traceback (most recent call last):
  File "/home/anbreaker/Escritorio/z.py", line 77, in <module>
    al1 = Modulo(15,'Javier', 'Antúnez', 'antunez19@gmail.com', True)
TypeError: __init__() takes 4 positional arguments but 6 were given
>>> 
'''