import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Volumes import Volumes
from Adherents import Adherents
from Mysql_connect import Mysql_connect


class Livres (Volumes):    

        
    id_livre=0
    id_adherent = 0
    id_volume=0
    connect = Mysql_connect()
    
    
    
    
    
    def __init__(self,id_livre,id_volume,auteur,id_document=0,titre=0,id_bibliotheque=0):
        super().__init__(id_volume,auteur,id_document,titre,id_bibliotheque)
        self.id_livre = id_livre
        
    
    def getId_livre(self):
        return self.id_livre
    
    def setId_livre (self, id_livre):
        self.id_livre = id_livre
    
    def getId_adherent(self):
        return self.id_adherent
    
    def setId_adherent (self, id_adherent):
        self.id_adherent = id_adherent
    
    def getId_volume(self):
        return self.id_volume
    
    def setId_volume (self, id_volume):
        self.id_volume = id_volume
    
    
    
    def creer_livre(self,id_livre,id_volume):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into livres (id_livre,id_volume) values (%s,%s);')        
            values = (id_livre,id_volume)
            print(requete,values)
            cursor.execute(requete,values)         

        
        
            cnx.commit()
            cursor.close()
            
            
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to insert record {}".format(error))

        
    
    def emprunter_livre(self,id_livre,id_adherent):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update volumes set id_adhe = %s where id_livre = %s;')        
            values = (id_adherent,id_livre)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to update record {}".format(error))

        
    
    def supprimer_livre(self,id_livre):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from livres where id_livre = %s;')        
            values = (id_livre)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to delete record {}".format(error))

        
    
    def liste_livres (self) :
        
        try :
            
            cnx = self.connect.connexion()  
            
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from livres;')
            
            
            row = cursor.fetchall()
            
            # result = pd.DataFrame(row)
            # print(result)
            
            cursor.close()  
            cnx.close()
            
                                     
                           
        
        except mysql.connector.Error as error:
            print("Failed to select record {}".format(error))

        
    
        liste = []
            
        for i in row :
            livres = Livres(i[0],i[1],i[2])
            liste.append(livres)
        return liste
            