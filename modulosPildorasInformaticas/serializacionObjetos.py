import pickle


class Vehiculo():
    def __init__(self, marca, modelo):
        # Atributos
        self.marca = marca
        self.modelo = modelo
        # Metodos
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancarVehiculo(self):
        # print('esta acelerando')
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    # Parecido al "metodo toString de java"
    def estadoVehiculo(self):
        print("Marca: {} \nModelo: {} \nenMarcha: {} \nAcelerando: {} \nFrenando: {}".format(
            self.marca, self.modelo, self.enMarcha, self.acelera, self.frena))


# Creo tres objetos para despues serializarlos

coche1 = Vehiculo('Toyota', 'Auris')
coche2 = Vehiculo('Opel', 'Corsa')
coche3 = Vehiculo('Ford', 'Fiesta')

coches = [coche1, coche2, coche3]

# Trabajo con el fichero
fichero = open('losCoches', 'wb')
# Volcamos la lista en el fichero binario.
pickle.dump(coches, fichero)
fichero.close()
del(fichero)

abriendoFichero = open('losCoches', 'rb')

misCoches = pickle.load(abriendoFichero)
abriendoFichero.close()

for c in misCoches:
    print(c.estadoVehiculo())
