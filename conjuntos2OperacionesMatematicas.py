# Conjuntos, operaciones matematicas:
# Union

a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2, 3, 5}
d = frozenset({7, 8, 9})  # Conjunto Inmutable!

union = a | b   # Union de dos conjutos simbolo |
interseccion = a & b   # Interseccion simbolo & (Elementos en ambos conjuntos)
diferenciaAB = a - b  # Elementos de a que no estan en b simbolo -
diferenciaBA = b - a  # Elementos de a que no estan en b simbolo -
# Elementos que estan en a y en b pero no en ambos simbolo ^
diferenciaSimetrica = a ^ b


print(f'Union --> {union}')
print(f'Interseccion -- > {interseccion}')
print(f'Diferencia AB -- > {diferenciaAB}')
print(f'Diferencia BA -- > {diferenciaBA}')
print(f'diferencia Simetrica -- > {diferenciaSimetrica}')
print(f'Es a un subconjtuo de C --> {a.issubset(c)}')  # Comprobar subconjutos
print(f'Es b un subconjtuo de C --> {b.issubset(c)}')  # Comprobar subconjutos
print(f'Es c Superconjtuo de A --> {c.issuperset(a)}')  # Superconjuto
print(f'Es c Superconjtuo de B --> {c.issuperset(b)}')  # Superconjuto
print(f'Es c Superconjtuo de B --> {c.issuperset(b)}')  # Superconjuto
print(f'Conjuntos disconexos --> {a.isdisjoint(d)}')  # Conjuntos disconexos
