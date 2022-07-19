from atexit import register
import mysql.connector
import sys
class DBhelper:
    def __init__(self) :
        try:
            self.conn = mysql.connector.connect(host ="localhost", user="root", 
            password="",database="log_in")
            self.mycursor = self.conn.cursor()
        except:
            print("Some error occured. could not connect")
            sys.exit(0)
        else:
            print("-----Connected to database------- ")

    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            INSERT INTO users (ID, Name, Email, Password) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()

        except:
            return -1
        else:
            return 1
    
    def search(self,email,password):

            self.mycursor.execute("""
            SELECT * FROM `users` WHERE Email like '{}' and Password like '{}';
            """.format(email,password))
            data = self.mycursor.fetchall()
            # print(data)
            return data




































