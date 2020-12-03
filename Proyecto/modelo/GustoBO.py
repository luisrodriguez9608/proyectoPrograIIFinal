import mysql.connector 

# para instalarlo -> pip3 install mysql-connector 
# Para el error de cifrado desintalar el mysql-connector con pip3 uninstall mysql-connector
# y luego instalar el mysql-connector-python con el pip3 install mysql-connector-python



class GustoBO:

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
    def guardar(self, gusto):
        try:
            if(self.validar(gusto)):#se valida que tenga la información

                if(not self.exist(gusto)): #si no existe lo agrega
                    gusto.lastUser = "ChGari"
                    insertSQL = "INSERT INTO t_gustos (`PKA_ID`, `Nombre`, `Descripcion`,`FK_Cedula`,`lastUser`, `lastModification`) VALUES (%s, %s, %s, %s, %s, CURDATE())"
                    insertValores =  (gusto.id.get(),gusto.nombre.get(),gusto.descripcion.get(),gusto.cedula.get(),gusto.descripcion.get(), gusto.lastUser)
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
    def exist(self , gusto):
        try:
            existe = False
            selectSQL = "Select * from t_gustos where PKA_ID = " + gusto.id.get()
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
    def validar (self, gusto):
        valido = True
        gusto.printInfo()
        if gusto.id.get() == "" :
            valido = False
        
        if gusto.nombre.get() == "" :
            valido = False

        if gusto.descripcion.get() == "" :
            valido = False

        if gusto.cedula.get() == "" :
            valido = False

        return valido

    
     
    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select PKA_ID as id, \
                            Nombre, Descripcion,\
                            FK_Cedula,\
                        from t_gustos" 
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
    def consultarGusto(self, gusto):
        try:
            selectSQL = "Select * from t_gustos where PKA_ID = " + gusto.id.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            gustoDB = cursor.fetchone()
            if (gustoDB) : #Metodo obtiene un solo registro o none si no existe información
                gusto.id.set(gustoDB[0]),
                gusto.nombre.set(gustoDB[1])
                gusto.descripcion.set(gustoDB[2])
                gusto.cedula.set(gustoDB[3])
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
    def eliminar(self, gusto):
        try:
            deleteSQL = "delete  from t_gustos where PKA_Cedula = " + gusto.id.get()
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
    def modificar(self, gusto):
        try:
            if(self.validar(gusto)):#se valida que tenga la información

                if(self.exist(gusto)): #si  existe lo modifica
                    gusto.lastUser = "ChGari"
                    updateSQL = "UPDATE t_gustos  set `Nombre` = %s, `Descripcion` = %s, `FK_Cedula` = %s,`lastUser` = %s, `lastModification` = CURDATE() WHERE `PKA_ID` =  %s"
                    updateValores =  (gusto.nombre.get(), gusto.descripcion.get(),gusto.cedula.get(), gusto.lastUser, gusto.id.get())
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