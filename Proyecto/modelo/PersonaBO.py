import mysql.connector 

# para instalarlo -> pip3 install mysql-connector 
# Para el error de cifrado desintalar el mysql-connector con pip3 uninstall mysql-connector
# y luego instalar el mysql-connector-python con el pip3 install mysql-connector-python



class PersonaBO:

    #*************************************************************************
    #El constructor de la clase persona BO crea un objeto de conexion a la base de datos
    #*************************************************************************
    def __init__(self):
        #se crea la conexión con la base de datos
        self.db = mysql.connector.connect(host ="localhost", 
                                     user = "root", 
                                     password = "root", 
                                     db ="mydb") 

    #*************************************************************************
    #Cuando el objeto es destruido por el interprete realiza la desconexion con la base de datos
    #*************************************************************************
    def __del__(self):
        self.db.close() #al destriurse el objeto cierra la conexion 
  
    #*************************************************************************
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def guardar(self, persona):
        try:
            if(self.validar(persona)):#se valida que tenga la información

                if(not self.exist(persona)): #si no existe lo agrega
                    persona.lastUser = "ChGari"
                    insertSQL = "INSERT INTO t_personas (`PK_Cedula`, `Nombre`, `Apellido`,`FechaNac`, `Descripcion`,Estado,`lastUser`, `lastModification`) VALUES (%s, %s, %s, %s, %s, %s, %s, CURDATE())"
                    insertValores =  (persona.cedula.get(),persona.nombre.get(),persona.apellido.get(),persona.fecNacimiento.get(), persona.descripcion.get(), persona.estado.get(), persona.lastUser)
                    print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(insertSQL, insertValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 
    
    #*************************************************************************
    #Metodo que verifica en la base de datos si la persona existe por cédula
    #*************************************************************************
    def exist(self , persona):
        try:
            existe = False
            selectSQL = "Select * from Personas where PK_Cedula = " + persona.cedula.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            if (cursor.fetchone()) : #Metodo obtiene un solo registro o none si no existe información
                existe  = True

            return existe
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para validar al información que proviene de la vista
    #*************************************************************************
    def validar (self, persona):
        valido = True
        persona.printInfo()
        if persona.cedula.get() == "" :
            valido = False
        
        if persona.nombre.get() == "" :
            valido = False

        if persona.apellido.get() == "" :
            valido = False

        if persona.fecNacimiento.get() == "" :
            valido = False
        
        if persona.descripcion.get() == "" :
            valido = False
        
        if persona.estado.get() == "" :
            valido = False

        return valido

    
     
    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select PK_Cedula as cedula, \
                            Nombre, Apellido,\
                            FechaNac, Descripcion,Estado \
                        from t_personas" 
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            myresult = cursor.fetchall()
            final_result = [list(i) for i in myresult]
            return final_result
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para consultar la información de una persona
    #*************************************************************************
    def consultarPersona(self, persona):
        try:
            selectSQL = "Select * from Personas where PK_Cedula = " + persona.cedula.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            personaDB = cursor.fetchone()
            if (personaDB) : #Metodo obtiene un solo registro o none si no existe información
                persona.cedula.set(personaDB[0]),
                persona.nombre.set(personaDB[1])
                persona.apellido1.set(personaDB[2])
                persona.apellido2.set(personaDB[3])
                persona.fecNacimiento.set(personaDB[4])
                persona.sexo.set(personaDB[5])
                persona.observaciones.set(personaDB[6])
            else:
                raise Exception("La cédula consultada no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar a una persona de la base de datos
    #*************************************************************************
    def eliminar(self, persona):
        try:
            deleteSQL = "delete  from Personas where PK_Cedula = " + persona.cedula.get()
            cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
            cursor.execute(deleteSQL) #ejecuta el SQL con las valores
            self.db.commit() #crea un commit en la base de datos
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 



    #*************************************************************************
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def modificar(self, persona):
        try:
            if(self.validar(persona)):#se valida que tenga la información

                if(self.exist(persona)): #si  existe lo modifica
                    persona.lastUser = "ChGari"
                    updateSQL = "UPDATE t_personas  set `Nombre` = %s, `Apellido` = %s, `FechaNac` = %s, `Descripcion` = %s, `Estado` = %s, `lastUser` = %s, `lastModification` = CURDATE() WHERE `PK_Cedula` =  %s"
                    updateValores =  (persona.nombre.get(),persona.apellido.get(), persona.fecNacimiento.get(), persona.descripcion.get(), persona.estado.get(), persona.lastUser, persona.cedula.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e))    