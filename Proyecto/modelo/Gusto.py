from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Gusto:

    def __init__(self):
        self.id = StringVar()
        self.nombre = StringVar()
        self.descripcion = StringVar()
        self.cedula = StringVar()
        self.lastUser = ""
        self.lastModification = StringVar()

    def limpiar(self):
        self.id = StringVar()
        self.nombre.set("")
        self.descripcion.set("")
        self.cedula = StringVar()

    def printInfo(self):
        print(f"ID:{self.id.get()}")
        print(f"Nombre:{self.nombre.get()}")
        print(f"Descripcion:{self.descripcion.get()}")
        print(f"Cedula:{self.cedula.get()}")