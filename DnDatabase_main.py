import mysql.connector
from mysql.connector import errorcode
import sys
from create_tables import table_creation

# This is to protect details that I use to access my personal MySQL server
# database_details.py is under .gitignore
try:
    import database_details
    
except:
    # This information you alter yourself, or if you want create a python file named database_details and have the following variables:
    # HOST
    # USERNAME
    # PASSWORD
    # DATABASE
    
    HOST = "localhost"
    USERNAME = "root"
    PASSWORD = ""
    DATABASE = "test_database"
    
else:
    HOST = database_details.HOST
    USERNAME = database_details.USERNAME
    PASSWORD = database_details.PASSWORD
    DATABASE = database_details.DATABASE


def yes_or_no_create():
    """
    This function handles the asking of whether or not the user wants to create a database since they entered in a non-existant database name.

    Args:
        dbname (str): Name of the database in question.

    Returns:
        user_input (str): yes/no
    """
    while True:
        user_input = str(input(f"\n{DATABASE} does not exist. Would you like to create a database named {DATABASE}? (yes or no) "))
        user_input.lower()
        
        if user_input != "yes" and user_input != "no":
            print("Invalid Input! Please try again. ")
        else:
            break
    
    return user_input == "yes"
            
def initialize_database():
    """
    Initializes the database
    Returns:
        DB_OBJ (mysql.connector): Database object
        MYCURSOR (DB_OBJ.cursor): Query tool for database object
    """
    
    while True:
        try:
            # Attempts to connect to the MySQL server and constructs the MYSQLCursor object
            DB_OBJ = mysql.connector.connect(host=HOST,user=USERNAME, password=PASSWORD, database=DATABASE)
            MYCURSOR = DB_OBJ.cursor()
            
            # Error handlers
        except mysql.connector.Error as err:
            
            # Unauthorized user/incorrect password
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                sys.exit(f"Access denied, check USERNAME ({USERNAME}) and PASSWORD ({PASSWORD}) ")
                
            # No password 
            elif err.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
                sys.exit(f"Access denied, have you entered a password? ")
                
            # Database does not exist
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                user_input = yes_or_no_create()
                
                # If user wants to create new database with the established database name
                if user_input:
                    DB_OBJ = mysql.connector.connect(host=HOST,user=USERNAME, password=PASSWORD)
                    MYCURSOR = DB_OBJ.cursor()
                    
                    MYCURSOR.execute(f"CREATE DATABASE {DATABASE} DEFAULT CHARACTER SET utf8mb4")
                    pass
                
                # If user does not want to create a new database.
                else:
                    sys.exit(f"Please enter in a valid database name ")
        else:
            return DB_OBJ, MYCURSOR
        




# Runs program
if __name__ == "__main__":
    DB_OBJ, MYCURSOR = initialize_database()
    print(type(MYCURSOR))
    table_creation(DATABASE, MYCURSOR)
    
    
    
    
    
"""
myCURSOR = mydb.CURSOR()

myCURSOR.execute("SELECT * FROM Country")

myresult = myCURSOR.fetchall()

for x in myresult:
    print(x)
    """
