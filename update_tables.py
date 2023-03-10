# Allows the defining of datatypes for parameters
import mysql.connector.cursor_cext
import mysql.connector.connection_cext


def update_table_data(cursor_obj: mysql.connector.cursor_cext.CMySQLCursor, database_obj: mysql.connector.connection_cext.CMySQLConnection):
    global database
    global cursor
    global database_str
    global searching

    cursor = cursor_obj
    database = database_obj

    # Updates player table
    print("\nUpdating the player roster\n")

    sql_script = """
    UPDATE player
    SET player_fname = 'Mitchell'
    WHERE player_fname = 'Mitch'    
    """

    cursor.execute(sql_script)

    print(f"{cursor.rowcount} record(s) affected")

    # Updates player_chaacter table
    print("\nUpdating the player_character roster\n")

    sql_script2 = f"""
    UPDATE player_character
    SET character_lname = 'Robinson'
    WHERE character_fname = 'Frank'    
    """

    cursor.execute(sql_script2)

    print(f"{cursor.rowcount} record(s) affected")


# This tells the user that they shouldn't be running this file like a program.
if __name__ == "__main__":
    assert False, f"update_tables.py is not a program, you should instead run DnDatabase_main.py."
