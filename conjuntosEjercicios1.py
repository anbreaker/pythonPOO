# Ejercicio 2 Conjutos
# Escribe un programa que tenga dos listas y que, a continuacion, cree
# las siguientes listas (en las que no debe haber repeticiones):
#   Lista de palabras que aparecen en las dos listas
#   Lista de palabras que aparecen en la primeram pero no en la segunda.
#   Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#   Lista de palabras que aparecen en ambas.


lista1 = ['hola', 'mundo', 'Elvas', 'Badajoz', 1, 2, 3]
lista2 = []

conjunto = set()
conjuto = {}
for i in range(5):
    conjunto.add(i)

conjunto.add('hola')

print(1 not in conjunto)
