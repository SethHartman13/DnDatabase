import threading
import mysql.connector.cursor_cext

cursor = mysql.connector.cursor_cext.CMySQLCursor
database = ""


def insert_class_data():
    global database
    global cursor

    sql_script = """
    INSERT INTO
        class(class_name)
    VALUES
        ('Artificer'),
        ('Barbarian'),
        ('Bard'),
        ('Cleric'),
        ('Druid'),
        ('Fighter'),
        ('Monk'),
        ('Paladin'),
        ('Ranger'),
        ('Rogue'),
        ('Sorcerer'),
        ('Warlock'),
        ('Wizard');
    """

    cursor.execute(sql_script)

def insert_player_data():
    global database
    global cursor





















def table_insert(database_name:str, cursor_obj:mysql.connector.cursor_cext.CMySQLCursor):
    global database
    global cursor

    database = database_name
    cursor = cursor_obj