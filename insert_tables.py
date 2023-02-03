import threading
import mysql.connector.cursor_cext
import mysql.connector.connection_cext

cursor = mysql.connector.cursor_cext.CMySQLCursor
database = mysql.connector.connection_cext.CMySQLConnection
database_str = ""

def initial_setup():
    """
    Tells the SQL server to not do specific checks, otherwise the server will return an error.

    Args:
        None
    """

    global cursor

    sql_scripts = []
    sql_scripts.append(
        "SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;")
    sql_scripts.append(
        "SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;")
    sql_scripts.append(
        "SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    sql_scripts.append(f"USE `{database_str}`")

    # Executes the SQL scripts
    for sql_script in sql_scripts:
        cursor.execute(sql_script)


def class_data():
    """
    Inserts class data into the class table

    Args:
        None    
    """
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

def player_data():
    """
    Inserts player data into the player table

    Args:
        None    
    """
    global cursor

    sql_script = """
    INSERT INTO
        player(player_fname, player_lname)
    VALUES
        ('Anne', 'Sue'),
        ('Donald', 'Hart'),
        ('Janet', 'Hool'),
        ('Keagan', 'Hart'),
        ('Mitch', 'Lincoln');   
    """

    cursor.execute(sql_script)

def creature_type_data():
    """
    Inserts creature type data into the creature_type table

    Args:
        None    
    """
    global cursor

    sql_script = """
    INSERT INTO
        creature_type(creature_type)
    VALUES
        ('Aberration'),
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

def ability_score_data():
    """
    Inserts ability score data into the ability_score table

    Args:
        None
    
    """
    global cursor

    sql_script = """
    INSERT INTO
        ability_score(str_score, dex_score, con_score, int_score, wis_score, chr_score)
    VALUES
        (24,14,16,12,16,15),
        (13,13,18,15,8,8),
        (12,20,16,12,18,14),
        (11,18,9,14,20,16),
        (13,12,15,18,16,12),
        (10,19,12,18,19,25),
        (10,15,14,14,12,15),
        (16,20,12,25,16,14),
        (10,25,18,12,18,10),
        (15,14,16,14,25,9),
        (13,14,12,3,12,7),
        (26,8,16,4,6,7),
        (12,15,14,10,10,12),
        (15,10,18,8,10,12),
        (8,20,27,18,17,20);
    """
    
    cursor.execute(sql_script)
    
def monster_data():
    """
    Inserts monster data into the monster table

    Args:
        None
    """
    global cursor
    
    sql_script = """
    INSERT INTO
        monster(monster_name, ability_score_id, monster_AC, monster_HP, monster_description)
    VALUES
        ('Jasper', 11, 18, 16, 'Theas Mastiff'),
        ('Undead Acid Carrier', 12, 15, 30, 'Acid Zombie, explodes'),
        ('Raider', 13, 16, 23, 'Former criminal turned violent raider'),
        ('Undead Zombie (Normal)', 14, 16, 35, 'Former Humanoid turned flesh-eating Zombie');    
    """
    
    cursor.execute(sql_script)

def monster_has_creature_type_data():
    global cursor
    
    sql_script = """
    INSERT INTO
        monster_has_creature_type(monster_id, creature_type_id)
    VALUES
        (1,7),
        (2,14),
        (3,10),
        (4,14);   
    """
    
    cursor.execute(sql_script)
    
def NPC_data():
    global cursor
    
    sql_script = """
    INSERT INTO
        NPC(creature_type_id, ability_score_id, character_fname, character_lname, character_nickname, total_level, AC, HP)
    VALUES
        (10, 6, NULL, 'Jenklin', 'Dr. Jenklin', 20, 17, 77),
        (6, 7, 'Eira', NULL, 'Ice Nympth', 16, 18, 95),
        (10, 8, NULL, 'Warhall', 'Marshall Warhall', 20, 18, 123),
        (4, 9, 'P1', '-3RC3', 'Pi', 20, 23, 183),
        (4, 10, 'Bip', 'Bop', 'BipBop', 6, 18, 8),
        (5, 15, 'Taranis', NULL, 'Ral, Caller of Storms', 20, 18, 292);
    """

    cursor.execute(sql_script)

def player_character_data():
    global cursor
    
    sql_script = """
    INSERT INTO
        player_character(player_id, creature_type_id, ability_score_id, character_fname, character_lname, character_nickname, total_level, AC, HP)
    VALUES
        (1, 10, 1, 'Acquillia', 'Simmons', 'Quill', 7, 17, 34),
        (2, 10, 2, 'Ricky', 'Bigfoot', NULL, 7, 15, 19),
        (3, 14, 3, 'Thea', 'Firestone', NULL, 7, 18, 61),
        (4, 10, 4, 'ROB', NULL, 'Chewie', 6, 19, 9),
        (5, 10, 5, 'Frank', NULL, 'Frank the Tank', 7, 17, 45);
    """
    
    cursor.execute(sql_script)
    
def player_character_has_class_data():
    global cursor
    
    sql_script = """
    INSERT INTO
        player_character_has_class(player_character_id, class_id)
    VALUES
        (1, 6),
        (1, 4),
        (2, 2),
        (3, 9),
        (3, 10),
        (4, 7),
        (5, 1),
        (5, 6);    
    """

    cursor.execute(sql_script)
    
def NPC_has_class():
    global cursor
    
    sql_script = """
    INSERT INTO
        NPC_has_class(NPC_id, class_id)
    VALUES
        (1, 12),
        (1, 10),
        (2, 11),
        (2, 13),
        (3, 10),
        (4, 7),
        (5, 4),
        (6, 11);
    """
    
    cursor.execute(sql_script)

def final_cleanup():
    global cursor
    
    sql_scripts = []
    sql_scripts.append("SET SQL_MODE=@OLD_SQL_MODE;")
    sql_scripts.append("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;")
    sql_scripts.append("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;")

    for sql_script in sql_scripts:
        cursor.execute(sql_script)

def table_insert(database_obj:mysql.connector.connection_cext.CMySQLConnection, cursor_obj:mysql.connector.cursor_cext.CMySQLCursor, database_name: str):
    global database
    global cursor
    global database_str 
    
    database_str = database_name
    database = database_obj
    cursor = cursor_obj
    
    print("Starting table insert")
    
    
    initial_setup()
    
    
    threads = []
    
    # Indepndent tables
    ability_thread = threading.Thread(ability_score_data())
    creature_thread = threading.Thread(creature_type_data())
    player_thread = threading.Thread(player_data())
    class_thread = threading.Thread(class_data())

    threads.append(ability_thread)
    threads.append(creature_thread)
    threads.append(player_thread)
    threads.append(class_thread)

    
    # Dependent (Layer 2) tables
    monster_thread = threading.Thread(monster_data())
    NPC_thread = threading.Thread(NPC_data())
    player_character_thread = threading.Thread(player_character_data())

    threads.append(monster_thread)
    threads.append(NPC_thread)
    threads.append(player_character_thread)


    # Dependent (Layer 3) tables
    monster_has_creature_type_thread = threading.Thread(monster_has_creature_type_data())
    player_character_has_class_thread = threading.Thread(player_character_has_class_data())
    NPC_has_class_thread = threading.Thread(NPC_has_class())
    
    threads.append(monster_has_creature_type_thread)
    threads.append(player_character_has_class_thread)
    threads.append(NPC_has_class_thread)
    
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
    final_cleanup()
    
    print("Finishing table insert")
    
if __name__ == "__main__":
    assert False, f"insert_tables.py is not a program, you should instead run DnDatabase_main.py."
