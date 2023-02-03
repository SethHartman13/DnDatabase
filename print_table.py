import threading
import mysql.connector.cursor_cext
import mysql.connector.connection_cext

cursor = mysql.connector.cursor_cext.CMySQLCursor
database = mysql.connector.connection_cext.CMySQLConnection
database_str = ""
table_name = ""

# def print_tables():
#     global database
#     global cursor
    
#     sql_script = f"""
#     SELECT *
#     FROM information_schema.tables
#     WHERE table_schema = '{database_str}';
#     """
#     cursor.execute(sql_script)
    
    
#     table_list = cursor.fetchall()
    
#     for line in table_list:
#         print(line)
        
# def print_table():
#     global table_name
    
#     while_bool = True
#     while while_bool:
#         table_name = str(input("What is the name of your table? "))
        
#         sql_script = f"""
#         SHOW TABLES LIKE '{table_name}';
#         """
        
#         cursor.execute(sql_script)
        
#         table_name_test = cursor.fetchall()
        
#         if table_name_test[0] == "":
#             print("That table does not exist, try again. ")
#         elif table_name_test[0] == table_name:
#             while_bool = False
#         else:
#             print("An error has occured! ")
    
#     sql_script = f"""
#     SELECT *
#     FROM '{table_name}';
#     """
    
#     cursor.execute(sql_script)
        
#     table_contents = cursor.fetchall()
    
#     for line in table_contents:
#         print(line)
        
# def update_table():
#     global table_name
    
#     print_table()
    
#     user_input = str("")
    
    
        
    
# def user_input(input:int):
#     if input != (1 or 2 or 3):
#         print(f"Please enter a valid input, you entered '{input}'")
#     elif input == 1:
#         print_tables()
#     elif input == 2:

def print_table_data(cursor_obj: mysql.connector.cursor_cext.CMySQLCursor, database_obj: mysql.connector.connection_cext.CMySQLConnection, database_name):
    global database
    global cursor
    global database_str
    global searching
    
    cursor = cursor_obj
    database = database_obj
    database_str = database_name
    # searching = True
    
    # while searching:
    
    
    #     print("""
    #         Hello! What would you like to do?
            
    #         1. Check table names
    #         2. Update table 
    #         3. Search table
    #         4. Exit program
            
    #         """)
        
    #     user_input(int(input( )))
    
    print("\nPrinting the player_character table joined with the player roster\n")
    
    sql_script = f"""
    SELECT player_fname AS 'First Name:', player_lname AS 'Last Name:', IFNULL(character_fname,' ') AS 'Character Fname:', IFNULL(character_lname,' ') AS 'Character Lname:', IFNULL(character_nickname,' ') AS 'Nickname:'
    FROM player
    INNER JOIN player_character ON player.player_id = player_character.player_id
    """
    cursor.execute(sql_script)
    columns = cursor.column_names
    results = cursor.fetchall()

       
    print('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}'.format(*columns))
    
    for line in results:
        pfname, plname, cfname, clname, cnname = line
        print('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}'.format(str(pfname), str(plname), str(cfname), str(clname), str(cnname)))
    
    
        
    
    
