import os
from tkinter import *
from tkinter.ttk import *

raiz = Tk()

raiz.title('Ventana de pruebas')

raiz.iconbitmap('@icono.xbm')

logo = PhotoImage(file='icono.gif')
raiz.call('wm', 'iconphoto', raiz._w, logo)

raiz.geometry('640x480')

raiz.config(bg='blue')

raiz.mainloop()
