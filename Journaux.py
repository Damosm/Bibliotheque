import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from Documents import Documents


class Journaux (Documents):    

        
    id_journaux=0
    date_de_parution = ""
    
    def __init__(self):
        super().__init__()

    def getId(self):
        return self.id_journaux
    
    def setId (self, id_journaux):
        self.id_journaux = id_journaux
    
    def getDateDeParution(self):
        return self.date_de_parution
    
    def setDateDePaution (self, date_de_parution):
        self.date_de_parution = date_de_parution
    
    def creer_journaux(self,id_doc,date_de_parution):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into journaux (id_doc,date_de_parution) values (%s,%s);')        
            values = (id_doc,date_de_parution)
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
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
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
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
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
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                        host='127.0.0.1',
                                        database='bibliotheque')
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