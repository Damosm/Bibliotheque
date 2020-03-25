import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Volumes import Volumes
from Mysql_connect import Mysql_connect


class Dictionnaires (Volumes):    

        
    id_dictionnaire=0
    connect = Mysql_connect()
    
    def __init__(self,id_dictionnaire,id_volume=0,auteur=0):
        super().__init__(id_volume,auteur)
    

    def getIdDictionnaire(self):
        return self.id_dictionnaire
    
    def setIdDictionnaire (self, id_dictionnaire):
        self.id_dictionnaire = id_dictionnaire
    
    
    
    def creer_dictionnaire(self,id_volume):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into dictionnaires (id_volume) values (%s);')        
            values = (id_volume)
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
    
    # def modifier_dictionnaire(self,id_journaux,date_de_parution):
    #     try :
  
    #         cnx = self.connect.connexion()
    
    #         if (cnx.is_connected()):
    #             print('is connected')
            
    #         cursor = cnx.cursor()
        
            
    #         requete = ('update journaux set date_de_parution = %s where id_journ = %s;')        
    #         values = (date_de_parution,id_journaux)
    #         print(requete,values)
    #         cursor.execute(requete,values)         

    #         cnx.commit()
    #         cursor.close()
           
    #         cnx.close()

    #     except mysql.connector.Error as error:
    #         print("Failed to update record {}".format(error))

    #     finally:
    #         if (cnx.is_connected()):
    #             cnx.close()
    #             print("MySQL connection is closed")
    
    # def supprimer_journaux(self,id_journaux):
    #     try :
  
    #         cnx = self.connect.connexion()
    
    #         if (cnx.is_connected()):
    #             print('is connected')
            
    #         cursor = cnx.cursor()
        
            
    #         requete = ('delete from journaux where id_journ = %s;')        
    #         values = (id_journaux)
    #         print(requete,values)
    #         cursor.execute(requete,values)         

    #         cnx.commit()
    #         cursor.close()
           
    #         cnx.close()

    #     except mysql.connector.Error as error:
    #         print("Failed to delete record {}".format(error))

    #     finally:
    #         if (cnx.is_connected()):
    #             cnx.close()
    #             print("MySQL connection is closed")
    
    def liste_dictionnaires (self) :
        
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from dictionnaires;')

            
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
