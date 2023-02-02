-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DnD_DB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema DnD_DB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DnD_DB` DEFAULT CHARACTER SET utf8 ;
USE `DnD_DB` ;

-- -----------------------------------------------------
-- Table `DnD_DB`.`ability_score`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`ability_score` (
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


-- -----------------------------------------------------
-- Table `DnD_DB`.`monster`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`monster` (
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
    REFERENCES `DnD_DB`.`ability_score` (`ability_score_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`creature_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`creature_type` (
  `creature_type_id` INT NOT NULL AUTO_INCREMENT,
  `creature_type` VARCHAR(11) NULL,
  PRIMARY KEY (`creature_type_id`),
  UNIQUE INDEX `creature_type_id_UNIQUE` (`creature_type_id` ASC) VISIBLE,
  UNIQUE INDEX `creature_type_UNIQUE` (`creature_type` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`monster_has_creature_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`monster_has_creature_type` (
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
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`player` (
  `player_id` INT NOT NULL AUTO_INCREMENT,
  `player_fname` VARCHAR(45) NOT NULL,
  `player_lname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`player_id`),
  UNIQUE INDEX `player_id_UNIQUE` (`player_id` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`player_character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`player_character` (
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
    REFERENCES `DnD_DB`.`player` (`player_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_character_creature_type1`
    FOREIGN KEY (`creature_type_id`)
    REFERENCES `DnD_DB`.`creature_type` (`creature_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_character_ability_score1`
    FOREIGN KEY (`ability_score_id`)
    REFERENCES `DnD_DB`.`ability_score` (`ability_score_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`class` (
  `class_id` INT NOT NULL AUTO_INCREMENT,
  `class_name` VARCHAR(9) NULL,
  PRIMARY KEY (`class_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`player_character_has_class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`player_character_has_class` (
  `player_character_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  PRIMARY KEY (`player_character_id`, `class_id`),
  INDEX `fk_player_character_has_class_class1_idx` (`class_id` ASC) VISIBLE,
  INDEX `fk_player_character_has_class_player_character1_idx` (`player_character_id` ASC) VISIBLE,
  CONSTRAINT `fk_player_character_has_class_player_character1`
    FOREIGN KEY (`player_character_id`)
    REFERENCES `DnD_DB`.`player_character` (`player_character_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_player_character_has_class_class1`
    FOREIGN KEY (`class_id`)
    REFERENCES `DnD_DB`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`NPC`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`NPC` (
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
    REFERENCES `DnD_DB`.`creature_type` (`creature_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_NPC_ability_score1`
    FOREIGN KEY (`ability_score_id`)
    REFERENCES `DnD_DB`.`ability_score` (`ability_score_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DnD_DB`.`NPC_has_class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DnD_DB`.`NPC_has_class` (
  `NPC_id` INT NOT NULL,
  `class_id` INT NOT NULL,
  PRIMARY KEY (`NPC_id`, `class_id`),
  INDEX `fk_NPC_has_class_class1_idx` (`class_id` ASC) VISIBLE,
  INDEX `fk_NPC_has_class_NPC1_idx` (`NPC_id` ASC) VISIBLE,
  CONSTRAINT `fk_NPC_has_class_NPC1`
    FOREIGN KEY (`NPC_id`)
    REFERENCES `DnD_DB`.`NPC` (`NPC_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_NPC_has_class_class1`
    FOREIGN KEY (`class_id`)
    REFERENCES `DnD_DB`.`class` (`class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
