from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Amigo:

    def __init__(self):
        self.cedulaOrigen = StringVar()
        self.cedulaDestino = StringVar()
        self.nivelAmistad = StringVar()
        self.lastUser = ""
        self.lastModification = StringVar()

    def limpiar(self):
        self.cedulaOrigen = StringVar()
        self.cedulaDestino.set("")
        self.nivelAmistad.set("")

    def printInfo(self):
        print(f"Cedula Origen:{self.cedulaOrigen.get()}")
        print(f"Cedula Destino:{self.cedulaDestino.get()}")
        print(f"Nivel de Amistad:{self.nivelAmistad.get()}")

    
        