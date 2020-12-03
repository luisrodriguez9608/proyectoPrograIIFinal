import mysql.connector 

# para instalarlo -> pip3 install mysql-connector 
# Para el error de cifrado desintalar el mysql-connector con pip3 uninstall mysql-connector
# y luego instalar el mysql-connector-python con el pip3 install mysql-connector-python



class AmigoBO:

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
    def guardar(self, amigo):
        try:
            if(self.validar(amigo)):#se valida que tenga la información

                if(not self.exist(amigo)): #si no existe lo agrega
                    amigo.lastUser = "ChGari"
                    insertSQL = "INSERT INTO t_amigo (`PK_CEDULA_origen`, `PK_CEDULA_destino`, `Nivel_Amistad`,`lastUser`, `lastModification`) VALUES (%s, %s, %s, %s, %s, CURDATE())"
                    insertValores =  (amigo.cedulaOrigen.get(),amigo.cedulaDestino.get(),amigo.nivelAmitad.get(), amigo.lastUser)
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
    def exist(self , amigo):
        try:
            existe = False
            selectSQL = "Select * from Personas where PK_CEDULA_origen = " + amigo.cedulaOrigen.get()
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
    def validar (self, amigo):
        valido = True
        amigo.printInfo()
        if amigo.cedulaOrigen.get() == "" :
            valido = False
        
        if amigo.cedulaDestino.get() == "" :
            valido = False

        if amigo.nivelAmistad.get() == "" :
            valido = False

        return valido

    
     
    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select PK_CEDULA_origen as cedulaOrigen, \
                            PK_CEDULA_destino, Nivel_Amistad,\
                        from t_amigos" 
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
    def consultarAmigo(self, amigo):
        try:
            selectSQL = "Select * from t_amigos where PK_CEDULA_origen = " + amigo.cedulaOrigen.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            amigosDB = cursor.fetchone()
            if (amigosDB) : #Metodo obtiene un solo registro o none si no existe información
                amigo.cedulaOrigen.set(amigosDB[0]),
                amigo.cedulaDestino.set(amigosDB[1])
                amigo.nivelAmistad.set(amigosDB[2])
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
    def eliminar(self, amigo):
        try:
            deleteSQL = "delete  from t_amigos where PK_CEDULA_origen = " + amigo.cedulaOrigen.get()
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
    def modificar(self, amigo):
        try:
            if(self.validar(amigo)):#se valida que tenga la información

                if(self.exist(amigo)): #si  existe lo modifica
                    amigo.lastUser = "ChGari"
                    updateSQL = "UPDATE t_amigos  set `PK_CEDULA_destino` = %s, `Nivel_Amistad` = %s, `lastUser` = %s, `lastModification` = CURDATE() WHERE `PK_CEDULA_origen` =  %s"
                    updateValores =  (amigo.nombre.get(),amigo.apellido.get(), amigo.lastUser, amigo.cedula.get())
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