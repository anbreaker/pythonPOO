""" KC_EJ31
Crear una clase Alumno con los siguientes atributos: 
numeroMatricula, nombre, apellido, email, estatusInscrito. 
La matrícula deberá ser numérica, mientras que email, nombre y apellido como textos. 
El atributo estatusInscrito deberá ser un valor booleano. 
"""
class Alumno:
    #Atributos con Valores iniciales:
    numeroMatricula = 0
    nombre = ''
    apellido = ''
    email = ''
    estatusInscrito = False



    #constructores
	def __init__(self, numeroMatricula, nombre, apellido, email, estatusInscrito):
        self.numeroMatricula = numeroMatricula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.estatusInscrito = estatusInscrito

	