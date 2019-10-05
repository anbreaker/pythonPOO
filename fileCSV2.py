import csv

personas = [
    ['Palacios', 'Rivas', 'Adam', 'CDMX'],
    ['Torres', 'Palacios', 'Sandra', 'Sinaloa'],
    ['Martines', 'Pizjuan', 'Andrea', 'Tijuana'],
]

with open('personas2.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(personas)
