from tkinter import * 
from tkinter import font
from tkinter import messagebox as msg
from tkinter import ttk 

from tksheet import Sheet # para instalarlo -> pip3 install tksheet

from tkcalendar import Calendar, DateEntry # para instalarlo -> pip3 install tkcalendar

#Incluye el objeto de persona
from modelo import Amigo

#Incluye el objeto de logica de negocio
from modelo import AmigoBO

class Aplicacion:
    

    def __init__(self):
        #*************************************************************************
        #Crea un objeto TK
        #*************************************************************************
        self.raiz = Tk()
        self.raiz.title ("Mantenimiento de Amigos")
        self.raiz.geometry('900x600') 

        #*************************************************************************
        #crea el menu de la pantalla
        #*************************************************************************
        menubar = Menu(self.raiz)
        self.raiz.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Acerca de..")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.quit)

        mantmenu = Menu(menubar, tearoff=0)
        mantmenu.add_command(label="Persona")
        mantmenu.add_command(label="Amigo")
        mantmenu.add_command(label="Gusto")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Mantenimiento", menu=mantmenu)

        #*************************************************************************
        #crea un objeto tipo fuenta
        #*************************************************************************
        self.fuente = font.Font(weight="bold")

        #*************************************************************************
        #se crean atributos de la clase
        #*************************************************************************
        self.amigo = Amigo.Amigo() #se crea el objeto de dominio para guardar la información
        self.insertando = True
    
        #*************************************************************************
        #se crean los campos de la pantalla
        #*************************************************************************

        #Se coloca un label del titulo
        self.lb_tituloPantalla = Label(self.raiz, text = "MANTENIMIENTO DE AMIGOS", font = self.fuente)
        self.lb_tituloPantalla.place(x = 320, y = 20) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y
        
        #coloca en el formulario el campo y el label de cedula
        self.lb_cedulaOrigen = Label(self.raiz, text = "Cedula Origen:")
        self.lb_cedulaOrigen.place(x = 240, y = 60)
        self.txt_cedulaOrigen = Entry(self.raiz, textvariable=self.amigo.cedulaOrigen, justify="right")
        self.txt_cedulaOrigen.place(x = 370, y = 60)

        #coloca en el formulario el campo y el label de nombre
        self.lb_cedulaDestino = Label(self.raiz, text = "Cedula Destino:")
        self.lb_cedulaDestino.place(x = 240, y = 90)
        self.txt_cedulaDestino = Entry(self.raiz, textvariable=self.amigo.cedulaDestino, justify="right", width=30)
        self.txt_cedulaDestino.place(x = 370, y = 90)

        #coloca en el formulario el campo y el label de apellido1
        self.lb_nivelAmistad = Label(self.raiz, text = "Nivel Amistad:")
        self.lb_nivelAmistad.place(x = 240, y = 120)
        self.txt_nivelAmistad = Entry(self.raiz, textvariable=self.amigo.nivelAmistad, justify="right", width=30)
        self.txt_nivelAmistad.place(x = 370, y = 120)

        #coloca los botones enviar y borrar
        self.bt_borrar = Button(self.raiz, text="Limpiar", width=15, command = self.limpiarInformacion)
        self.bt_borrar.place(x = 370, y = 310)

        self.bt_enviar = Button(self.raiz, text="Enviar", width=15, command = self.enviarInformacion)
        self.bt_enviar.place(x = 510, y = 310)

        #Se coloca un label del informacion
        self.lb_tituloPantalla = Label(self.raiz, text = "INFORMACIÓN INCLUIDA", font = self.fuente)
        self.lb_tituloPantalla.place(x = 350, y = 355) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y

        #*************************************************************************
        #tabla con informacion
        #*************************************************************************
        
        self.sheet = Sheet(self.raiz,
                           page_up_down_select_row = True,
                           #empty_vertical = 0,
                           column_width = 120,
                           startup_select = (0,1,"rows"),
                           #row_height = "4",
                           #default_row_index = "numbers",
                           #default_header = "both",
                           #empty_horizontal = 0,
                           #show_vertical_grid = False,
                           #show_horizontal_grid = False,
                           #auto_resize_default_row_index = False,
                           #header_height = "3",
                           #row_index_width = 100,
                           #align = "center",
                           #header_align = "w",
                            #row_index_align = "w",
                            #data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(1000)], #to set sheet data at startup
                            headers = ['Cédula Origen', 'Cedula Destino', 'NIvel de Amistad.'],
                            #row_index = [f"Row {r}\nnewline1\nnewline2" for r in range(2000)],
                            #set_all_heights_and_widths = True, #to fit all cell sizes to text at start up
                            #headers = 0, #to set headers as first row at startup
                            #headers = [f"Column {c}\nnewline1\nnewline2" for c in range(30)],
                           #theme = "light green",
                            #row_index = 0, #to set row_index as first column at startup
                            #total_rows = 2000, #if you want to set empty sheet dimensions at startup
                            #total_columns = 30, #if you want to set empty sheet dimensions at startup
                            height = 195, #height and width arguments are optional
                            width = 720 #For full startup arguments see DOCUMENTATION.md
                            )
        #self.sheet.hide("row_index")
        #self.sheet.hide("header")
        #self.sheet.hide("top_left")
        self.sheet.enable_bindings(("single_select", #"single_select" or "toggle_select"
                                        
                                         "column_select",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         #"row_width_resize",
                                         #"column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "right_click_popup_menu",
                                         "rc_select",
                                         "rc_insert_column",
                                         "rc_delete_column",
                                         "rc_insert_row",
                                         "rc_delete_row"))
        #self.sheet.disable_bindings() #uses the same strings
        #self.sheet.enable_bindings()

        self.sheet.place(x = 20, y = 390)
        
        #coloca los botones cargar y eliminar
        self.bt_cargar = Button(self.raiz, text="Cargar", width=15, command = self.cargarInformacion)
        self.bt_cargar.place(x = 750, y = 385)

        self.bt_eliminar = Button(self.raiz, text="Eliminar", width=15, command = self.eliminarInformacion)
        self.bt_eliminar.place(x = 750, y = 425)
        
        self.cargarTodaInformacion()


        #*************************************************************************
        #se inicial el main loop de la pantalla
        #*************************************************************************
        self.raiz.mainloop()


    #*************************************************************************
    #Metodo para consultar la información de la base de datos para 
    #cargarla en la tabla
    #*************************************************************************
    def cargarTodaInformacion(self):
        try:
            self.amigoBO = AmigoBO.AmigoBO() #se crea un objeto de logica de negocio
            resultado = self.amigoBO.consultar()

            self.sheet.set_sheet_data(resultado)
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar informacion
    #*************************************************************************
    def cargarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedulaOrigen = (self.sheet.get_cell_data(datoSeleccionado[0],0))
            self.amigo.cedulaOrigen.set(cedulaOrigen)
            self.amigoBO = AmigoBO.AmigoBO() #se crea un objeto de logica de negocio
            self.amigoBO.consultarAmigo(self.amigo) #se envia a consultar
            self.insertando = False
            msg.showinfo("Acción: Consultar Amigo", "La información de la amigo ha sido consultada correctamente") # Se muestra el mensaje de que todo esta correcto
            
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar eliminar la informacion
    #*************************************************************************
    def eliminarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedulaOrigen = (self.sheet.get_cell_data(datoSeleccionado[0],0))

            resultado = msg.askquestion("Eliminar",  "¿Desear eliminar a "+cedulaOrigen+" de la base de datos?")
            if resultado == "yes":
                self.amigo.cedulaOrigen.set(cedulaOrigen)
                self.amigoBO = AmigoBO.AmigoBO() #se crea un objeto de logica de negocio
                self.amigoBO.eliminar(self.amigo) #se envia a consultar
                self.cargarTodaInformacion()
                self.amigo.limpiar()
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error


    #*************************************************************************
    #Metodo para enviar la información a la base de datos
    #*************************************************************************
    def enviarInformacion(self):
        try:
            self.amigoBO = AmigoBO.AmigoBO() #se crea un objeto de logica de negocio
            if(self.insertando == True):
                self.amigoBO.guardar(self.amigo)
            else:
                self.amigoBO.modificar(self.amigo)
            
            self.cargarTodaInformacion()
            self.amigo.limpiar() #se limpia el formulario

            if(self.insertando == True):
                msg.showinfo("Acción: Agregar amigo", "La información de la persona ha sido incluida correctamente") # Se muestra el mensaje de que todo esta correcto
            else:
                msg.showinfo("Acción: Agregar modificar", "La información de la persona ha sido modificada correctamente") # Se muestra el mensaje de que todo esta correcto
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para limpiar el formulario
    #*************************************************************************
    def limpiarInformacion(self):
        self.amigo.limpiar() #llama al metodo de la clase persona para limpiar los atritudos de la clase
        self.insertando = True
        msg.showinfo("Acción del sistema", "La información del formulario ha sido eliminada correctamente") # muestra un mensaje indicando que se limpio el formulario


    #*************************************************************************
    #Metodo para mostrar un contro tipo datepicker
    #*************************************************************************
    '''def mostrarDatePicker(self):
        self.top = Toplevel(self.raiz)
        self.cal = Calendar(self.top, font="Arial 14", selectmode='day', locale='en_US',
                   year=2019, month=6, day=16)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="Seleccionar", command = self.seleccionarFecha).pack()'''

    #*************************************************************************
    #Evento para obtener la fecha del datepicker
    #*************************************************************************
    #def seleccionarFecha(self):
        #self.persona.fecNacimiento.set(self.cal.selection_get())


def main():
    Aplicacion()
    return 0

if __name__ == "__main__":
    main()
