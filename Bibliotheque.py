import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


class Bibliotheque :    

        
    id_bibliotheque=0
        
    def __init__(self,id_bibliotheque):
        self.id_bibliotheque = id_bibliotheque

    def getId_bibliotheque(self):
        return self.id_bibliotheque
    
    def setId_bibliotheque (self, id_bibliotheque):
        self.id_bibliotheque = id_bibliotheque
    
    def creer_bibliotheque(self,id_bibliotheque):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('insert into bibliotheque (id_biblio) values (%s);')        
            values = (id_bibliotheque)
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
    
    def modifier_bibliotheque(self,id,new_id):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('update bibliotheque set id_biblio = %s where id_biblio = %s;')        
            values = (new_id,id)
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
    
    def supprimer_bibliotheque(self,id):
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                    host='127.0.0.1',
                                    database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')
            
            cursor = cnx.cursor()
        
            
            requete = ('delete from bibliotheque where id_biblio = %s;')        
            values = (id)
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
    
    def liste_bibliotheques (self) :
        
        try :
  
            cnx = mysql.connector.connect(user='root', password='damos02',
                                        host='127.0.0.1',
                                        database='bibliotheque')
            if (cnx.is_connected()):
                print('is connected')

            cursor = cnx.cursor()

            cursor.execute('select * from bibliotheque;')

            
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