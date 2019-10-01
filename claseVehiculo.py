class Vehiculos():
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


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return 'La Furgoneta esta cargada'
        else:
            return 'La Furgoneta NO esta cargada'


class Moto(Vehiculos):
    caballito = ""

    def hacerCaballito(self):
        self.caballito = "Estoy haciendo un caballito"

    # Se sobreescribe el Metodo del padre con EL MISMO NOMBRE!!
    def estadoVehiculo(self):
        print("Marca: {} \nModelo: {} \nenMarcha: {} \nAcelerando: {} \nFrenando: {} \n{}".format(
            self.marca, self.modelo, self.enMarcha, self.acelera, self.frena, self.caballito))


class VehiculosElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.recargando = True


class BicicletaElectrica(Vehiculos, VehiculosElectricos):
    pass


miMoto1 = Moto('Kawasaki', 'Vulcan S')
# miMoto1.hacerCaballito()
miMoto1.estadoVehiculo()


miMoto2 = Moto('Honda', 'CBR')
miMoto2.acelerar()
miMoto2.arrancarVehiculo()
miMoto2.hacerCaballito()
miMoto2.estadoVehiculo()

miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.arrancarVehiculo()
miFurgoneta.estadoVehiculo()
print(miFurgoneta.carga(True))


miBici = BicicletaElectrica('Orbea', 'Wild FS')
