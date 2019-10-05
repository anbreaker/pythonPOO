import csv

with open('personas.csv') as f:
    reader = csv.reader(f, delimiter='$')
    for row in reader:
        print(
            f'Ap paterno: {row[0]}, Ap Materno: {row[1]}, Nombre: {row[2]}, Ciudad: {row[3]}')
