import mysql.connector

try:
    import database_details
    
except:
    # This information you alter yourself, or if you want create a python file named database_details and have the following variables:
    # host
    # username
    # password
    # database
    
    host = str("localhost")
    username = str("root")
    password = str("")
    database = str("test_database")
    
else:
    host = database_details.HOST
    username = database_details.USERNAME
    password = database_details.PASSWORD
    database = database_details.DATABASE





db_obj = mysql.connector.connect(host=host,user=username, password=password, database=database)
db_obj.autocommit = True
mycursor = db_obj.cursor()

mycursor.execute(f"DROP SCHEMA IF EXISTS {database}")