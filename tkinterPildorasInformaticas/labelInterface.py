from tkinter import *

root = Tk()

root.title('Inteface')

# Creamos frame propio para trabajar con el y no la raiz
miFrame = Frame(root, width=500, height=400)

# Color del fondo miFrame
miFrame.config(bg='#FFF273')

# Empaquetamos el frame para montarlo y trabajr con el.
miFrame.pack()

# Colocando una imagen
miImagen = PhotoImage(file='icono.gif')

# Colocamos texto
miLabel = Label(miFrame, text='Empezando con label', fg='#FF6672', font=(22))
miImagen = Label(miFrame, image=miImagen)


# Label en:
miLabel.place(x=25, y=20)
miImagen.place(x=50, y=100)


# Loop de repeticion mantiene la ventana
root.mainloop()
