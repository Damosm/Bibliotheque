import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Bibliotheque import Bibliotheque


class Documents (Bibliotheque):    

        
    id_document=0
    titre = ""
    
    def __init__(self,id_document,titre,id_bibliotheque):
        super().__init__(id_bibliotheque)
        self.id_document = id_document
        self.titre = titre

    def getId_document(self):
        return self.id_document
    
    def setId_document (self, id_document):
        self.id_document = id_document
    
    def getTitre(self):
        return self.titre
    
    def setTitre (self, titre):
        self.titre = titre
    
    def creer_document(self,id_doc,id_biblio,titre):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into documents values (%s,%s,%s);')        
            values = (id_doc,id_biblio,titre)
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
    
    def modifier_document(self,id_doc,titre):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update documents set titre = %s where id_doc = %s;')        
            values = (titre,id_doc)
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
    
    def supprimer_document(self,id_doc):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from documents where id_doc = %s;')        
            values = (id_doc)
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
    
    def liste_documents (self) :
        
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                        host='127.0.0.1',
                                        database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from documents;')

            
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