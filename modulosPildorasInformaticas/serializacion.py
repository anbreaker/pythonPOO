import pickle

listaNombres = ['Javier', 'Jessica', 'Curro', 'Simão']

ficheroBinario = open('listaNombres', 'wb')

# Volcamos la lista en el fichero binario.

pickle.dump(listaNombres, ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)  # Borro de la memoria le fichero


fichero = open('listaNombres', 'rb')

lista = pickle.load(fichero)

print(lista)
