# Crea un programa que pida introducir una dirección de email por teclado. El programa
# debe imprimir en consola si la dirección de email es correcta o no en función de si esta
# tiene el símbolo ‘@’. Si tiene una ‘@’ la dirección será correcta. Si tiene más de una o
# ninguna ‘@’ la dirección será errónea. Si la ‘@’ está al comienzo de la dirección de email
# o al final, la dirección también será errónea.

mail = input('Introduce tu mail: ')

if (mail.count('@') == 1 and mail.find('@') != 0 and mail.rfind('@') != (len(mail)-1)):
    print(f'Tu mail es: {mail}')
else:
    print('Mail Erroneo')
