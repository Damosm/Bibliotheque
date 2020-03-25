import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Documents import Documents
from Mysql_connect import Mysql_connect


class Journaux (Documents):    

        
    id_journaux=0
    date_de_parution = ""
    connect = Mysql_connect()
    
    def __init__(self,id_journaux,date_de_parution,id_document=0,titre=0):
        super().__init__(id_document,titre)
        self.id_journaux=id_journaux
        self.date_de_parution=date_de_parution

    def getId_journaux(self):
        return self.id_journaux
    
    def setId_journaux(self, id_journaux):
        self.id_journaux = id_journaux
    
    def getDateDeParution(self):
        return self.date_de_parution
    
    def setDateDePaution (self, date_de_parution):
        self.date_de_parution = date_de_parution
    
    def creer_journaux(self,id_journaux,id_doc,date_de_parution):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into journaux (id_journ,id_doc,date_de_parution) values (%s,%s,%s);')        
            values = (id_journaux,id_doc,date_de_parution)
            print(requete,values)
            cursor.execute(requete,values)         

        
        
            cnx.commit()
            cursor.close()
            
            
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to insert record {}".format(error))

        finally:
            if (cnx.is_connected()):
                cnx.close()
                print("MySQL connection is closed")
    
    def modifier_journaux(self,id_journaux,date_de_parution):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update journaux set date_de_parution = %s where id_journ = %s;')        
            values = (date_de_parution,id_journaux)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to update record {}".format(error))

        finally:
            if (cnx.is_connected()):
                cnx.close()
                print("MySQL connection is closed")
    
    def supprimer_journaux(self,id_journaux):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from journaux where id_journ = %s;')        
            values = (id_journaux)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to delete record {}".format(error))

        finally:
            if (cnx.is_connected()):
                cnx.close()
                print("MySQL connection is closed")
    
    def liste_journaux (self) :
        
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from journaux;')

            
            row = cursor.fetchall()
            result = pd.DataFrame(row)

            print(result)
            
            cursor.close()  
            cnx.close()
        
        except mysql.connector.Error as error:
            print("Failed to select record {}".format(error))

        finally:
            if (cnx.is_connected()):
                cnx.close()
                print("MySQL connection is closed")