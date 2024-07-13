-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that 
-- computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables first
    DECLARE average_weighted_score FLOAT DEFAULT 0;
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE done INT DEFAULT FALSE;
    DECLARE userId INT;

    -- Then declare cursor
    DECLARE cur CURSOR FOR SELECT id FROM users;

    -- Declare continue handler after declaring cursors
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO userId;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate average_weighted_score logic here
        SELECT 
            SUM(p.weight), SUM(c.score * p.weight)
        INTO 
            total_weight, total_weighted_score
        FROM 
            corrections c
        JOIN 
            projects p ON c.project_id = p.id
        WHERE 
            c.user_id = userId;

        -- Calculate the average weighted score
        IF total_weight > 0 THEN
            SET average_weighted_score = total_weighted_score / total_weight;
        ELSE
            SET average_weighted_score = 0;
        END IF;
        -- Update the user's average_score
        UPDATE users
        SET average_score = average_weighted_score
        WHERE id = userId;

    END LOOP;

    CLOSE cur;
END //

DELIMITER ;
