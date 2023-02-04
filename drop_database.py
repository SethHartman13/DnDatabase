# Main mysql library
import mysql.connector

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


# Creates database and cursor object
try:
    db_obj = mysql.connector.connect(
        host=host, user=username, password=password, database=database)
    db_obj.autocommit = True
    mycursor = db_obj.cursor()
except:
    print("f{database} does not exist")
    
else:

    # Drops schema by querying the server.
    mycursor.execute(f"DROP SCHEMA {database}")
