""" KC_EJ30
Crear un programa que simule una máquina expendedora de gaseosas con las siguientes características:
Las bebidas disponibles son: Kas, Pepsi, 7Up. 
    Todas las bebidas tienen un costo de €1,0
    La máquina recibe monedas de 10, 20 y 50 cent, y €1,0

El programa deberá permitir que el usuario seleccione una bebida e ingrese una a una las monedas. 
El programa deberá detenerse cuando el importe de la gaseosa haya sido completado 
y, de ser necesario, determinar el sobrante.
"""
bebidas = {"1":"Kas", "2":"Pepsi", "3":"7up"}

#función únicamente de selección de bebidas. Se asegura que la ingresada sea válida
def seleccionar_bebida():
    while True:
        bebida = input('1)Kas' + '\n2) Pepsi' + '\n3) 7up\n-Elige tu bebida: ')
        if bebida == '1' or bebida == '2' or bebida == '3':
            return bebidas.get(bebida)
        else:
            print ('no tengo esa bebida')

#función para validar la moneda recibida
def importe_valido(importe):
    if importe != 1 and importe != 10 and importe != 20 and importe != 50:
        print ('Solo acepto monedas de 1, 10c, 20c y 50c')
        return False
    else:
        return True

#función para soltar la bebida
def entrega(bebida, acumulado):
    print ('Disfruta tu ', bebida)
    print ('Tu cambio es de ' + str((acumulado-100)))

#función para acumular el importe ingresado
def pagar(bebida):
    acumulado = 0;
    while True:
        pagado = int(input('Ingrese moneda: '))
        if(importe_valido(pagado)):
            if pagado == 1:             
                acumulado = acumulado + (pagado * 100)  
            else:
                acumulado = acumulado + pagado
            if acumulado >= 100:
                entrega(bebida, acumulado)
                break
            else:
                print ('Te faltan ' + str(100 - acumulado))
            
bebida = seleccionar_bebida()
pagar(bebida)
