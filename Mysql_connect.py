import mysql.connector

    
class Mysql_connect :
    
    def __init__(self):
        super().__init__()
    
    def connexion (self):
        cnx = mysql.connector.connect(user='root', password='damos02',
                            host='127.0.0.1',
                            database='bibliotheque')
        return cnx
        

