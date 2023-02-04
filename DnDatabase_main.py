# Main mysql library
import mysql.connector

# Error checking codes
from mysql.connector import errorcode

# Exits the program
from sys import exit

# Modules
from create_tables import table_creation
from insert_tables import table_insert
from print_table import print_table_data
from update_tables import update_table_data

# Allows the defining of datatypes for parameters
import mysql.connector.cursor_cext
import mysql.connector.connection_cext


# This is to protect details that I use to access my personal MySQL server,
# database_details.py is under my .gitignore
try:
    import database_details

except:
    exit("You need to create a database_details.py file, see database_details_example.py")
else:
    host = database_details.HOST  # ip address of SQL server
    username = database_details.USERNAME  # username
    password = database_details.PASSWORD  # password
    database = database_details.DATABASE  # database/schema name

    
def yes_or_no_create() -> bool:
    """
    This function handles the asking of whether or not the user wants to create a database since they entered in a non-existant database name.
    
    Returns:
        user_input (bool): TRUE/FALSE
    """
    while True:
        # While loop to get proper input, used to ask the user if it is okay to create a schema/database
        user_input = str(input(
            f"\n{database} does not exist. Would you like to create a database named {database}? (yes or no) "))
        user_input = "yes"
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
        db_obj (mysql.connector): Database object
        mycursor (db_obj.cursor): Query tool for database object
    """

    while True:
        try:
            # Attempts to connect to the MySQL server and constructs the MYSQLCursor object
            db_obj = mysql.connector.connect(
                host=host, user=username, password=password, database=database)
            db_obj.autocommit = True
            mycursor = db_obj.cursor()

            # Error handlers
        except mysql.connector.Error as err:

            # Unauthorized user/incorrect password
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                exit(
                    f"Access denied, check username ({username}) and password ({password}) ")

            # No password
            elif err.errno == errorcode.ER_ACCESS_DENIED_NO_PASSWORD_ERROR:
                exit(f"Access denied, have you entered a password? ")

            # Database does not exist
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                user_input = yes_or_no_create()

                # If user wants to create new database with the established database name, creates the database and goes back to the main portion of the while loop.
                if user_input:
                    db_obj = mysql.connector.connect(
                        host=host, user=username, password=password)
                    db_obj.autocommit = True
                    mycursor = db_obj.cursor()

                    mycursor.execute(
                        f"CREATE database {database} DEFAULT CHARACTER SET utf8mb4")
                    pass

                # If user does not want to create a new database, exits the program.
                else:
                    exit(f"Please enter in a valid database name ")
        else:
            return db_obj, mycursor


# Runs program
if __name__ == "__main__":

    # Creates Database and Cursor objects
    db_obj, mycursor = initialize_database()

    # Creates tables, skips if they already exist
    table_creation(database, mycursor)

    # Inserts initial information, should be commented out once completed
    table_insert(db_obj, mycursor, database)

    # Prints out requested criteria
    print_table_data(mycursor, database)

    # Updates requested criteria
    update_table_data(mycursor, db_obj)

    # Prints out requested criteria
    print_table_data(mycursor, database)
