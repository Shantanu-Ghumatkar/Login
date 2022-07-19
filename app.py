import sys
from dbhelper import DBhelper


class services:
    def __init__(self):
        self.db = DBhelper()
        self.menu()
#  menu function
    def menu(self):
        user_input = input("""
                1. Enter 1 to register
                2. Enter 2 to login
                3. Enter 3 to ferget
                4. Anything else to to leave
                """
                           )
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        elif user_input == "3":
            self.fergot()
        else:
            sys.exit(100)
    
    def login_menu(self):
         user_input = input("""
                1. Enter 1 to see profile
                2. Enter 2 to to edit profile
                3. Enter 3 to delet profile
                4. Enter 4 to log out
                """
                           )
        #  if user_input == "1":
            
        #  elif user_input == "2":
            
        #  elif user_input == "3":
        #     self.fergot()
        #  else:
        #     sys.exit(100)

    def register(self):
        name = input("Enter name:")
        Email = input("Enter Email:")
        password = input("Enter password:")
        result = self.db.register(name, Email, password)
        if result:
            print("Registration Succesful ")
        else:
            print("Registration fail")
        self.menu()

    def login(self):
        email = input("Enter email:")
        password = input("Enter password:")
        data = self.db.search(email, password)
        if len(data) == 0:
            print("Incorrect email/password")
        else:
            print("Helow", data[0][1])
            self.login_menu()


obj = services()
