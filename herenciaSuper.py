class Persona():
    def __init__(self,  nombre, edad, lugarResidencia):
        self.nombre = nombre
        self.edad = edad
        self.lugarResidencia = lugarResidencia

    def descripcion(self):
        print(
            f'Nombre: {self.nombre} Edad: {self.edad}, Residencia: {self.lugarResidencia}')


class Empleado(Persona):
    def __init__(self, salario, antiqueness, nombreEmpleado, edadEmpleado, residenciaEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
        self.salario = salario
        self.antiqueness = antiqueness

    def descripcion(self):
        super().descripcion()
        print(f'Salario: {self.salario}€ Antigüedad: {self.antiqueness} años')


Javier = Empleado(1100, 4, 'Javier', 33, 'Badajoz')

Javier.descripcion()

# Para comprobar si es una instancia heredada "isinstance(object, type) --> True"
print(isinstance(Javier, Persona))

Jessica = Persona('Jessica', 26, 'Elvas')
Jessica.descripcion()

# Devuelve Falso porque es persona pero no empleado
print(isinstance(Jessica, Empleado))
