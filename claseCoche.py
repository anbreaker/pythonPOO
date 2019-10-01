class Coche():

    # Constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()

        if (self.__enMarcha and chequeo):
            return 'El coche esta en Marcha'
        elif(self.__enMarcha and chequeo == False):
            return "Algo fue mal en el chequeo, no se puede arrancar"
        else:
            return 'El cocheesta esta Parado'

    def estado(self):
        print(
            f'El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} y un largo de {self.__largoChasis}')

    def __chequeoInterno(self):
        print('\n Realizando Chequeo Interno \n')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False


# Creando instancias de la clase

miCoche = Coche()
# print(f'El largo del chasis de mi coche es: {miCoche.__largoChasis} cms')
# print(f'El coche tiene: {miCoche.ruedas} ruedas')
print(miCoche.arrancar(True))
miCoche.estado()

print('\n-------- Creo una Segunda Instancia --------\n')

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
