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

    sql_script = """
    INSERT INTO
        player(player_fname, player_lname)
    VALUES
        ('Kimberly', 'Hartman'),
        ('Dawson', 'Fenn'),
        ('Kasden', 'Fenn'),
        ('Logan', 'Peterson'),
        ('Niagra', 'Lister');   
    """

    cursor.execute(sql_script)
    

def insert_creature_type_data():
    global database
    global cursor

    sql_script = """
    INSERT INTO
        creature_type(creature_type)
    VALUES
        ('Sberration'),
        ('Beast'),
        ('Celestial'),
        ('Construct'),
        ('Dragon'),
        ('Elemental'),
        ('Fey'),
        ('Fiend'),
        ('Giant'),
        ('Humanoid'),
        ('Monstrosity'),
        ('Ooze'),
        ('Plant'),
        ('Undead');    
    """

    cursor.execute(sql_script)

def insert_ability_score_data():
    global database
    global cursor

    sql_script = f"""
    INSERT INTO
        ability_score(str_score, dex_score, con_score, int_score, wis_score, chr_score)
    
    
    
    
    
    """




def table_insert(database_name:str, cursor_obj:mysql.connector.cursor_cext.CMySQLCursor):
    global database
    global cursor

    database = database_name
    cursor = cursor_obj