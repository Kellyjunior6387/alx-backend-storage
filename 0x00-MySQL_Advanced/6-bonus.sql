-- script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER //

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(256), bonus_score INT)
BEGIN
    DECLARE project_id INT;
    SET project_id = (SELECT id FROM projects WHERE name = project_name);
    IF project_id IS NULL THEN
        INSERT INTO projects(name) VALUES(project_name);
        SET  project_id = LAST_INSERT_ID();
    END IF;
    INSERT INTO corrections(user_id, project_id, score) VALUES (user_id, project_id, bonus_score);
END//

DELIMITER ;
