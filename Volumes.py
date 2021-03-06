import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Documents import Documents
from Mysql_connect import Mysql_connect


class Volumes (Documents):    

        
    id_volume=0
    auteur = ""
    connect = Mysql_connect()
    
    def __init__(self,id_volume,auteur,id_document=0,titre=0,id_bibliotheque=0):
        super().__init__(id_document,titre,id_bibliotheque)
        self.id_volume = id_volume
        self.auteur = auteur

    def getId_volume(self):
        return self.id_volume
    
    def setId_volume (self, id_volume):
        self.id_volume = id_volume
    
    def getAuteur(self):
        return self.auteur
    
    def setAuteur (self, auteur):
        self.auteur = auteur
    
    def creer_volume(self,id_volume,id_doc,auteur):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into volumes values (%s,%s,%s);')        
            values = (id_volume,id_doc,auteur)
            print(requete,values)
            cursor.execute(requete,values)         

        
        
            cnx.commit()
            cursor.close()
            
            
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to insert record {}".format(error))

        
    
    def modifier_volume(self,id_volume,auteur):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update volumes set auteur = %s where id_volume = %s;')        
            values = (auteur,id_volume)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to update record {}".format(error))

        
    
    def supprimer_volume(self,id_volume):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from volumes where id_volume = %s;')        
            values = (id_volume)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to delete record {}".format(error))

        
    
    def liste_volumes (self) :
        
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from volumes;')

            
            row = cursor.fetchall()
            result = pd.DataFrame(row)

            print(result)
            
            cursor.close()  
            cnx.close()
        
        except mysql.connector.Error as error:
            print("Failed to select record {}".format(error))

        