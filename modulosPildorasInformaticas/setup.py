from setuptools import setup

setup(
    name='paqueteCalculos',
    version='1.0',
    description='Paquete de redondeo y potencia',
    author='anbreaker',
    url='https://github.com/anbreaker',
    packages=['calculos', 'calculos.redondeoPotencia']
)

# Crear el paquete:
# python3 setup.py sdist
# -->(Paquete distribuible)
# Nos crea dos directorios, una caperta paqueteCalculos.egg-info
# y otra con el nombre dist, esta contiene el paquete instalable en el sistema
# entramos al directorio dist, donse se aloja nuestro paquete e
# instalamos el paquete en nuestra distribuion y podremos usarlo.
# pip3 install "nombreDelPaquete.tar.gz"
