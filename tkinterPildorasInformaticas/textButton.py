from tkinter import *

root = Tk()

root.title('Inteface')

# Creamos frame propio para trabajar con el y no la raiz
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

miNombre = StringVar()

# Cuadro entrada texto
cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=0, column=1, padx=2, pady=2)
cuadroNombre.config(fg='red')

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=2, pady=2)
cuadroPass.config(show='*')

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=2, pady=2)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=2, pady=2)

textoComentario = Text(miFrame, width=20, height=5)
textoComentario.grid(row=4, column=1, padx=2, pady=2)

scrolVertical = Scrollbar(miFrame, command=textoComentario.yview)
scrolVertical.grid(row=4, column=2, sticky='nsew')

textoComentario.config(yscrollcommand=scrolVertical.set)

nombreLabel = Label(miFrame, text='Nombre:')
nombreLabel.grid(row=0, column=0, sticky='e', padx=2, pady=2)

passLabel = Label(miFrame, text='Contraseña:')
passLabel.grid(row=1, column=0, sticky='e', padx=2, pady=2)

apellidoLabel = Label(miFrame, text='Apellido:')
apellidoLabel.grid(row=2, column=0, sticky='e', padx=2, pady=2)

direccionLabel = Label(miFrame, text='Direccion:')
direccionLabel.grid(row=3, column=0, sticky='e', padx=2, pady=2)

comentariosLabel = Label(miFrame, text='Comentarios:')
comentariosLabel.grid(row=4, column=0, sticky='e', padx=2, pady=2)


def codigoBoton():
    miNombre.set('Javier')


botonEnvio = Button(root, text='Enviar', command=codigoBoton)
botonEnvio.pack()


root.mainloop()
