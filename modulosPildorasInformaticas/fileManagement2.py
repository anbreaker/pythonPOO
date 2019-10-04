from io import open

archivoTexto = open('archivo.txt', 'r+')  # Lectura y escritura r+

# print(archivoTexto.readlines())

listaTexto = archivoTexto.readlines()

listaTexto[1] = "Esta linea ha sido incluida desde el exterior \n"

archivoTexto.seek(0)

archivoTexto.writelines(listaTexto)

archivoTexto.close()

# print(archivoTexto.read(10))  # Lectura hasta la posicion

# print(archivoTexto.read())

# Posicion donde se coloca el puntero en el fichero de texto
# archivoTexto.seek(11)

# archivoTexto.seek(len(archivoTexto.read()) / 2)
# archivoTexto.seek(len(archivoTexto.readline()))
# print(archivoTexto.read())
