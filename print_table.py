# Allows the defining of datatypes for parameters
import mysql.connector.cursor_cext
cursor = mysql.connector.cursor_cext.CMySQLCursor
database = str()
table_name = str()


# This is going to be apart of a future endeavor to make it so that it can be used by more than just me.
# def print_tables():
#     global cursor

#     sql_script = f"""
#     SELECT *
#     FROM information_schema.tables
#     WHERE table_schema = '{database}';
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

def print_table_data(cursor_obj: mysql.connector.cursor_cext.CMySQLCursor, database_name: str):
    """
    Prints table data by querying the server.

    Args:
        cursor_obj (CMySQLCursor): cursor object
        database_name (str): Name of the database/schema
    """
    global cursor
    cursor = cursor_obj

    # global database_str
    # global searching

    # database = database_name
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

    # Start of the printing process
    print("\nPrinting the player_character table joined with the player roster\n")

    # SQL script
    sql_script = f"""
    SELECT player_fname AS 'First Name:', player_lname AS 'Last Name:', IFNULL(character_fname,' ') AS 'Character Fname:', IFNULL(character_lname,' ') AS 'Character Lname:', IFNULL(character_nickname,' ') AS 'Nickname:'
    FROM player
    INNER JOIN player_character ON player.player_id = player_character.player_id
    """

    # Executes SQL script
    cursor.execute(sql_script)

    # Gets column names
    columns = cursor.column_names

    # Gets results
    results = cursor.fetchall()

    # Prints column names with formatting
    print('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}'.format(*columns))

    # Prints results with formatting
    for line in results:
        pfname, plname, cfname, clname, cnname = line
        print('{0:<20}{1:<20}{2:<20}{3:<20}{4:<20}'.format(
            str(pfname), str(plname), str(cfname), str(clname), str(cnname)))


# This tells the user that they shouldn't be running this file like a program.
if __name__ == "__main__":
    assert False, f"print_tables.py is not a program, you should instead run DnDatabase_main.py."
