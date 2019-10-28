from tkinter import *

root = Tk()

root.title('Inteface')

# Creamos frame propio para trabajar con el y no la raiz
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

# Cuadro entrada texto
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=2, pady=2)
cuadroNombre.config(fg='red')

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=2, pady=2)
cuadroPass.config(show='*')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=2, pady=2)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=2, pady=2)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='e', padx=2, pady=2)

passLabel = Label(miFrame, text='Contraseña:')
passLabel.grid(row=1, column=0, sticky='e', padx=2, pady=2)

apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='e', padx=2, pady=2)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=3, column=0, sticky='e', padx=2, pady=2)


root.mainloop()
