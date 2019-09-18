class Vehiculos():
    def __init__(self, marca, modelo):
        #Atributos
        self.marca = marca
        self.modelo = modelo
        #Metodos
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancarVehiculo(self):
        print ('esta acelrando')
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
        

    #Parecido al "metodo toString de java"
    def estadoVehiculo(self):
        print("Marca: {} \nModelo: {} \nenMarcha: {} \nAcelerando: {} \nFrenando: {}".format(self.marca, self.modelo, self.enMarcha, self.acelera, self.frena))

class Moto(Vehiculos):

    def hacerCaballito(self):
        self.hacerCaballito = "Estoy haciendo un caballito"

    #Se sobreescribe el Metodo del padre con EL MISMO NOMBRE!!
    def estadoVehiculo(self):
        print("Marca: {} \nModelo: {} \nenMarcha: {} \nAcelerando: {} \nFrenando: {} \nCaballito: {}".format(self.marca, self.modelo, self.enMarcha, self.acelera, self.frena, self.hacerCaballito))


miMoto1 = Moto('Kawasaki', 'Vulcan S')
#miMoto1.hacerCaballito()
miMoto1.estadoVehiculo()

'''
Marca: Kawasaki 
Modelo: Vulcan S 
enMarcha: False 
Acelerando: False 
Frenando: False 
Caballito: <bound method Moto.hacerCaballito of <__main__.Moto object at 0x7f74e8b5b340>>
'''