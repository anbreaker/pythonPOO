import os
from tkinter import *

raiz = Tk()

raiz.title('Ventana de pruebas')

# raiz.iconbitmap('@icono.xbm')
# logo = PhotoImage(file='icono.gif')
# raiz.call('wm', 'iconphoto', raiz._w, logo)

# raiz.resizable(True, True)
# raiz.geometry('640x480')
raiz.config(bg='blue')


miFrame = Frame()
# Diferentes formas de redimensionar las ventanas y sus opciones
# miFrame.pack(side='left', anchor='n')
# Redimensionado de X
# miFrame.pack(fill='x')
# Redimensionado de y
# miFrame.pack(fill='y', expand='True')
# Redimensionado total
# cambiar el borde de ventana
miFrame.config(bd=5)
# Bordes en la ventana:
# miFrame.config(relief='groove')
# miFrame.config(relief='sunken')
# Cambio del cursor al entrar en la ventana
miFrame.config(cursor='hand2')
# Para ajustar el frame a la ventana si se expande (respecto al raiz)
miFrame.pack(fill='both', expand='True')
# Tamaño de la ventana por defecto
miFrame.config(width='650', height='350')
# Color de la ventana
miFrame.config(bg='green')

raiz.mainloop()
