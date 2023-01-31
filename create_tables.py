from time import sleep
import threading
import mysql.connector.cursor_cext

cursor = mysql.connector.cursor_cext.CMySQLCursor
database = ""

def initial_setup(threads: list):
    """
    Tells the SQL server to not do specific checks, otherwise the server will return an error.

    Args:
        threads (list): list of threads
    """

    global database
    global cursor

    sql_scripts = []
    sql_scripts.append(
        "SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;")
    sql_scripts.append(
        "SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;")
    sql_scripts.append(
        "SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';")
    sql_scripts.append(f"USE `{database}`")

    # Executes the SQL scripts
    for sql_script in sql_scripts:
        cursor.execute(sql_script)

    # Starts the threads
    for thread in threads:
        thread.start()


def ability_score(ability_score_event: threading.Event):
    """
    Creates the ability_score table by querying the server.

    Args:
        ability_score_event (threading.Event): Event that prevents the creation of tables dependant upon the ability_score table.
    """

    global database
    global cursor
    
    sql_script = f'''
    CREATE TABLE IF NOT EXISTS `{database}`.`ability_score` (
        `ability_score_id` INT NOT NULL AUTO_INCREMENT,
        `str_score` TINYINT NOT NULL,
        `dex_score` TINYINT NOT NULL,
        `con_score` TINYINT NOT NULL,
        `int_score` TINYINT NOT NULL,
        `wis_score` TINYINT NOT NULL,
        `chr_score` TINYINT NOT NULL,
        PRIMARY KEY (`ability_score_id`),
        UNIQUE INDEX `ability_scores_id_UNIQUE` (`ability_score_id` ASC) VISIBLE)
    ENGINE = InnoDB;
    '''

    cursor.execute(sql_script)
    ability_score_event.set()


def monster(monster_event: threading.Event, ability_score_event: threading.Event):
    """
    Creates the monster table by querying the server
    Args:
        monster_event (threading.Event): Event that prevents the creation of tables dependant upon the ability_score table.
        ability_score_event (threading.Event): _description_
    """
    
    global database
    global cursor
    
    sql_script = f'''
    CREATE TABLE IF NOT EXISTS `{database}`.`monster` (
        `monster_id` INT NOT NULL AUTO_INCREMENT,
        `monster_name` VARCHAR(30) NOT NULL,
        `ability_score_id` INT NOT NULL,
        `monster_AC` TINYINT NOT NULL,
        `monster_HP` SMALLINT NOT NULL,
        `monster_description` VARCHAR(8000) NULL,
        PRIMARY KEY (`monster_id`),
        UNIQUE INDEX `monster_id_UNIQUE` (`monster_id` ASC) VISIBLE,
        INDEX `fk_monster_ability_score1_idx` (`ability_score_id` ASC) VISIBLE,
        CONSTRAINT `fk_monster_ability_score1`
            FOREIGN KEY (`ability_score_id`)
            REFERENCES `{database}`.`ability_score` (`ability_score_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB;    
    '''

    ability_score_event.wait()
    cursor.execute(sql_script)
    monster_event.set()


def creature_type(creature_type_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`creature_type` (
        `creature_type_id` INT NOT NULL AUTO_INCREMENT,
        `creature_type` VARCHAR(11) NULL,
        PRIMARY KEY (`creature_type_id`),
        UNIQUE INDEX `creature_type_id_UNIQUE` (`creature_type_id` ASC) VISIBLE,
        UNIQUE INDEX `creature_type_UNIQUE` (`creature_type` ASC) VISIBLE)
    ENGINE = InnoDB   
    """

    cursor.execute(sql_script)
    creature_type_event.set()


def monster_has_creature_type(monster_event: threading.Event, creature_type_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`monster_has_creature_type` (
        `monster_id` INT NOT NULL,
        `creature_type_id` INT NOT NULL,
        PRIMARY KEY (`monster_id`, `creature_type_id`),
        INDEX `fk_monster_has_creature_type_creature_type1_idx` (`creature_type_id` ASC) VISIBLE,
        INDEX `fk_monster_has_creature_type_monster_idx` (`monster_id` ASC) VISIBLE,
        CONSTRAINT `fk_monster_has_creature_type_monster`
            FOREIGN KEY (`monster_id`)
            REFERENCES `{database}`.`monster` (`monster_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_monster_has_creature_type_creature_type1`
            FOREIGN KEY (`creature_type_id`)
            REFERENCES `{database}`.`creature_type` (`creature_type_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB
    """

    monster_event.wait()
    creature_type_event.wait()
    cursor.execute(sql_script)


def player(player_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`player` (
        `player_id` INT NOT NULL AUTO_INCREMENT,
        `player_fname` VARCHAR(45) NOT NULL,
        `player_lname` VARCHAR(45) NOT NULL,
        PRIMARY KEY (`player_id`),
        UNIQUE INDEX `player_id_UNIQUE` (`player_id` ASC) VISIBLE)
    ENGINE = InnoDB;
    """

    cursor.execute(sql_script)
    player_event.set()


def player_character(player_character_event: threading.Event, player_event: threading.Event, ability_score_event: threading.Event, creature_type_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`player_character` (
        `player_character_id` INT NOT NULL AUTO_INCREMENT,
        `player_id` INT NOT NULL,
        `creature_type_id` INT NOT NULL,
        `ability_score_id` INT NOT NULL,
        `character_fname` VARCHAR(45) NULL,
        `character_lname` VARCHAR(45) NULL,
        `character_nickname` VARCHAR(45) NULL,
        `total_level` TINYINT NOT NULL,
        `AC` TINYINT NOT NULL DEFAULT 10,
        `HP` TINYINT NOT NULL,
        PRIMARY KEY (`player_character_id`),
        INDEX `fk_player_character_player1_idx` (`player_id` ASC) VISIBLE,
        INDEX `fk_player_character_creature_type1_idx` (`creature_type_id` ASC) VISIBLE,
        INDEX `fk_player_character_ability_score1_idx` (`ability_score_id` ASC) VISIBLE,
        UNIQUE INDEX `ability_score_id_UNIQUE` (`ability_score_id` ASC) VISIBLE,
        UNIQUE INDEX `player_id_UNIQUE` (`player_id` ASC) VISIBLE,
        CONSTRAINT `fk_player_character_player1`
            FOREIGN KEY (`player_id`)
            REFERENCES `{database}`.`player` (`player_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_player_character_creature_type1`
            FOREIGN KEY (`creature_type_id`)
            REFERENCES `{database}`.`creature_type` (`creature_type_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_player_character_ability_score1`
            FOREIGN KEY (`ability_score_id`)
            REFERENCES `{database}`.`ability_score` (`ability_score_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    """

    player_event.wait()
    ability_score_event.wait()
    creature_type_event.wait()

    cursor.execute(sql_script)

    player_character_event.set()


def char_class(class_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`class` (
        `class_id` INT NOT NULL AUTO_INCREMENT,
        `class_name` VARCHAR(9) NULL,
        PRIMARY KEY (`class_id`))
    ENGINE = InnoDB;
    """

    cursor.execute(sql_script)
    class_event.set()


def player_character_has_class(player_character_event: threading.Event, class_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`player_character_has_class` (
        `player_character_id` INT NOT NULL,
        `class_id` INT NOT NULL,
        PRIMARY KEY (`player_character_id`, `class_id`),
        INDEX `fk_player_character_has_class_class1_idx` (`class_id` ASC) VISIBLE,
        INDEX `fk_player_character_has_class_player_character1_idx` (`player_character_id` ASC) VISIBLE,
        CONSTRAINT `fk_player_character_has_class_player_character1`
            FOREIGN KEY (`player_character_id`)
            REFERENCES `{database}`.`player_character` (`player_character_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_player_character_has_class_class1`
            FOREIGN KEY (`class_id`)
            REFERENCES `{database}`.`class` (`class_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    """

    player_character_event.wait()
    class_event.wait()

    cursor.execute(sql_script)


def NPC(NPC_event: threading.Event, ability_score_event: threading.Event, creature_type_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`NPC` (
        `NPC_id` INT NOT NULL AUTO_INCREMENT,
        `creature_type_id` INT NOT NULL,
        `ability_score_id` INT NOT NULL,
        `character_fname` VARCHAR(45) NULL,
        `character_lname` VARCHAR(45) NULL,
        `character_nickname` VARCHAR(45) NULL,
        `total_level` TINYINT NOT NULL,
        `AC` TINYINT NOT NULL DEFAULT 10,
        `HP` TINYINT NOT NULL,
        PRIMARY KEY (`NPC_id`),
        INDEX `fk_player_character_creature_type1_idx` (`creature_type_id` ASC) VISIBLE,
        INDEX `fk_NPC_ability_score1_idx` (`ability_score_id` ASC) VISIBLE,
        CONSTRAINT `fk_player_character_creature_type10`
            FOREIGN KEY (`creature_type_id`)
            REFERENCES `{database}`.`creature_type` (`creature_type_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_NPC_ability_score1`
            FOREIGN KEY (`ability_score_id`)
            REFERENCES `{database}`.`ability_score` (`ability_score_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
        ENGINE = InnoDB;
    """

    ability_score_event.wait()
    creature_type_event.wait()

    cursor.execute(sql_script)

    NPC_event.set


def NPC_has_class(NPC_event: threading.Event, class_event: threading.Event):
    global database
    global cursor
    
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{database}`.`NPC_has_class` (
        `NPC_id` INT NOT NULL,
        `class_id` INT NOT NULL,
        PRIMARY KEY (`NPC_id`, `class_id`),
        INDEX `fk_NPC_has_class_class1_idx` (`class_id` ASC) VISIBLE,
        INDEX `fk_NPC_has_class_NPC1_idx` (`NPC_id` ASC) VISIBLE,
        CONSTRAINT `fk_NPC_has_class_NPC1`
            FOREIGN KEY (`NPC_id`)
            REFERENCES `{database}`.`NPC` (`NPC_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_NPC_has_class_class1`
            FOREIGN KEY (`class_id`)
            REFERENCES `{database}`.`class` (`class_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB;
    """

    NPC_event.wait()
    class_event.wait()

    cursor.execute(sql_script)


def final_cleanup(threads: list):
    global database
    global cursor
    
    sql_scripts = []
    sql_scripts.append("SET SQL_MODE=@OLD_SQL_MODE;")
    sql_scripts.append("SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;")
    sql_scripts.append("SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;")

    for thread in threads:
        thread.join()

    for sql_script in sql_scripts:
        cursor.execute(sql_script)


def table_creation(database_name:str, cursor_obj:mysql.connector.cursor_cext.CMySQLCursor):
    global database
    global cursor
    
    database = database_name
    cursor = cursor_obj

    # Independent thread events
    ability_score_event = threading.Event()
    player_event = threading.Event()
    creature_type_event = threading.Event()
    class_event = threading.Event()

    # Dependent thread events
    monster_event = threading.Event()
    NPC_event = threading.Event()
    player_character_event = threading.Event()

    # Thread holder
    threads = []

    # Independent threads
    threads.append(ability_score(ability_score_event))
    threads.append(creature_type(creature_type_event))
    threads.append(player(player_event))
    threads.append(char_class(class_event))

    # Dependent (Layer 2) threads
    threads.append(monster(monster_event, ability_score_event))
    threads.append(NPC(NPC_event, ability_score_event, creature_type_event))
    threads.append(player_character(player_character_event,
                   player_event, ability_score_event, creature_type_event))

    # Dependent (Layer 3) threads
    threads.append(monster_has_creature_type(
        monster_event, creature_type_event))
    threads.append(player_character_has_class(
        player_character_event, class_event))
    threads.append(NPC_has_class(NPC_event, class_event))

    initial_setup(threads)

    final_cleanup(threads)
