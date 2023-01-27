import mysql.connector.cursor

def monster(MYCURSOR:mysql.connector.cursor, DATABASE:str):
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{DATABASE}`.`monster` (
        `monster_id` INT NOT NULL AUTO_INCREMENT,
        `monster_name` VARCHAR(30) NOT NULL,
        `monster_AC` TINYINT NOT NULL,
        `monster_HP` SMALLINT NOT NULL,
        `monster_description` VARCHAR(8000) NULL,
        PRIMARY KEY (`monster_id`),
        UNIQUE INDEX `monster_id_UNIQUE` (`monster_id` ASC) VISIBLE)
    ENGINE = InnoDB
    """
    MYCURSOR.execute(sql_script)

def creature_type(MYCURSOR:mysql.connector.cursor, DATABASE:str):
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{DATABASE}`.`creature_type` (
        `creature_type_id` INT NOT NULL AUTO_INCREMENT,
        `creature_type` VARCHAR(11) NULL,
        PRIMARY KEY (`creature_type_id`),
        UNIQUE INDEX `creature_type_id_UNIQUE` (`creature_type_id` ASC) VISIBLE,
        UNIQUE INDEX `creature_type_UNIQUE` (`creature_type` ASC) VISIBLE)
    ENGINE = InnoDB   
    """
    MYCURSOR.execute(sql_script)
    
def monster_has_creature_type(MYCURSOR:mysql.connector.cursor, DATABASE:str):
    sql_script = f"""
    CREATE TABLE IF NOT EXISTS `{DATABASE}`.`monster_has_creature_type` (
        `monster_id` INT NOT NULL,
        `creature_type_id` INT NOT NULL,
        PRIMARY KEY (`monster_id`, `creature_type_id`),
        INDEX `fk_monster_has_creature_type_creature_type1_idx` (`creature_type_id` ASC) VISIBLE,
        INDEX `fk_monster_has_creature_type_monster_idx` (`monster_id` ASC) VISIBLE,
        CONSTRAINT `fk_monster_has_creature_type_monster`
            FOREIGN KEY (`monster_id`)
            REFERENCES `DnD_DB`.`monster` (`monster_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
        CONSTRAINT `fk_monster_has_creature_type_creature_type1`
            FOREIGN KEY (`creature_type_id`)
            REFERENCES `DnD_DB`.`creature_type` (`creature_type_id`)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION)
    ENGINE = InnoDB
    """
    MYCURSOR.execute(sql_script)
    




def main(MYCURSOR:mysql.connector.cursor, DATABASE:str):
    
    monster(MYCURSOR, DATABASE)
    creature_type(MYCURSOR, DATABASE)
    monster_has_creature_type(MYCURSOR, DATABASE)
    
    