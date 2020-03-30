import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Bibliotheque import Bibliotheque
# from Livres import Livres
from Mysql_connect import Mysql_connect


class Adherents (Bibliotheque):    

        
    id_adherent=0
    nom = ""
    prenom = ""
    inscrit = True
    Date = ""
    connect = Mysql_connect()
    
    def __init__(self,id_adherent,nom,prenom,inscrit,date,id_bibliotheque=0):
        super().__init__(id_bibliotheque)
        self.id_adherent = id_adherent
        self.nom = nom
        self.prenom = prenom
        self.inscrit = inscrit
        self.date = date
    
    def getId_adherent(self):
        return self.id_adherent
    
    def setId_adherent (self, id_adherent):
        self.id_adherent = id_adherent
    
    def getNom(self):
        return self.nom
    
    def setNom (self, nom):
        self.nom = nom
    
    def getPrenom(self):
        return self.prenom
    
    def setPrenom (self, prenom):
        self.prenom = prenom
    
    def getInscrit(self):
        return self.inscrit
    
    def setInscrit (self, inscrit):
        self.inscrit = inscrit
    
    def getDate(self):
        return self.date
    
    def setNom (self, date):
        self.date = date
    
    def creer_adherent(self,id_adherent,id_biblio,nom,prenom,inscrit,date):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into adherents values (%s,%s,%s,%s,%s,%s);')        
            values = (id_adherent,id_biblio,nom,prenom,inscrit,date)
            print(requete,values)
            cursor.execute(requete,values)         

        
        
            cnx.commit()
            cursor.close()
            
            
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to insert record {}".format(error))

        
    
    def modifier_adherent(self,id_adherent,nom,prenom,inscrit,date):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update adherents set nom = %s, prenom = %s, inscrit = %s, date = %s where id_adhe = %s;')        
            values = (nom,prenom,inscrit,date,id_adherent)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to update record {}".format(error))

        
    
    def supprimer_adherent(self,id_adherent):
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from adherents where id_adhe = %s;')        
            values = (id_adherent)
            print(requete,values)
            cursor.execute(requete,values)         

            cnx.commit()
            cursor.close()
           
            cnx.close()

        except mysql.connector.Error as error:
            print("Failed to delete record {}".format(error))

        
    
    def liste_adherents (self) :
        
        try :
  
            cnx = self.connect.connexion()
            
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from adherents;')

            
            row = cursor.fetchall()
            result = pd.DataFrame(row)

            print(result)
            
            cursor.close()  
            cnx.close()
        
        except mysql.connector.Error as error:
            print("Failed to select record {}".format(error))

        