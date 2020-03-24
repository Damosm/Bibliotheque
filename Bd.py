import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Volumes import Volumes


class Bd (Volumes):    

        
    id_bd=0
    destinataire = ""
    
    def __init__(self):
        super().__init__()

    def getId_bd(self):
        return self.id_bd
    
    def setId_bd (self, id_bd):
        self.id_bd = id_bd
    
    def getDestinataire(self):
        return self.destinataire
    
    def setDestinataire (self, destinataire):
        self.destinataire = destinataire
    
    def creer_bd(self,id_volume,destinataire):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into bd (id_volume,destinataire) values (%s,%s);')        
            values = (id_volume,destinataire)
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
    
    def modifier_bd(self,id_bd,destinataire):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update bd set destinataire = %s where id_bd = %s;')        
            values = (destinataire,id_bd)
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
    
    def supprimer_bd(self,id_bd):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from bd where id_bd = %s;')        
            values = (id_bd)
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
    
    def liste_bd (self) :
        
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                        host='127.0.0.1',
                                        database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from bd;')

            
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