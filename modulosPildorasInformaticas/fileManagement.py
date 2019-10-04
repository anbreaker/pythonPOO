from io import open


archivoTexto = open('archivo.txt', 'w')
frase = 'Estupendo día para estudiar Python \nen viernes'
# Para escribir en el fichero
archivoTexto.write(frase)
archivoTexto.close()

archivoTexto = open('archivo.txt', 'r')
texto = archivoTexto.read()
archivoTexto.close()

archivoTexto = open('archivo.txt', 'a')  # append
archivoTexto.write('\nHay que aprender a porgramar!')
archivoTexto.close()

archivoTexto = open('archivo.txt', 'r')
lineasTexto = archivoTexto.readlines()
archivoTexto.close()

print(lineasTexto[2])
