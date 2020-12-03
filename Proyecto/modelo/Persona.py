from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Persona:

    def __init__(self):
        self.cedula = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.fecNacimiento = StringVar()
        self.descripcion = StringVar()
        self.estado = StringVar()
        self.lastUser = ""
        self.lastModification = StringVar()

    def limpiar(self):
        self.cedula.set("")
        self.nombre.set("")
        self.apellido.set("")
        self.fecNacimiento.set("")
        self.descripcion.set("")
        self.estado.set("")

    def printInfo(self):
        print(f"Cedula:{self.cedula.get()}")
        print(f"Nombre:{self.nombre.get()}")
        print(f"Apellido:{self.apellido.get()}")
        print(f"Fecha Nacimiento:{self.fecNacimiento.get()}")
        print(f"Descripcion:{self.descripcion.get()}")
        print(f"Estado:{self.estado.get()}")

    
        