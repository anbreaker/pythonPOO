import pickle


class Persona():
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print(f'Se ha creado una Persona nueva: {self.nombre}')

    def __str__(self):
        return f'{self.nombre} {self.genero} {self.edad}'


class ListaPersonas():
    personas = []

    def __init__(self):
        # agregar informacion binaria
        listaDePersonas = open('ficheroExternoPersonas', 'ab+')
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print(
                f'Se cargaron {len(self.personas)} personas del fichero externo')
        except:
            print('El fichero esta vacio')
        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, persona):
        self.personas.append(persona)
        self.guardarPersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        listaDePersonas = open('ficheroExternoPersonas', 'wb')
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print('Informacion del fichero externo: ')
        for p in self.personas:
            print(p)


listaDePersonas = ListaPersonas()

p1 = Persona('Sandra', 'Femenino', 29)
listaDePersonas.agregarPersonas(p1)
p2 = Persona('Jessica', 'Femenino', 26)
listaDePersonas.agregarPersonas(p2)
p3 = Persona('Javier', 'Masculino', 33)
listaDePersonas.agregarPersonas(p3)

listaDePersonas.mostrarInfoFicheroExterno()
