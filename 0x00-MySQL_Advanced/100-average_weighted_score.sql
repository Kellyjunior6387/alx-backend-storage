-- script that creates a stored procedure ComputeAverageWeightedScoreForUser that 
-- computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight FLOAT DEFAULT 0;
    DECLARE total_weighted_score FLOAT DEFAULT 0;
    DECLARE average_score FLOAT DEFAULT 0;

    SELECT
        SUM(p.weight), SUM(c.score * p.weight)
    INTO
        total_weight, total_weighted_score
    FROM
        corrections c
    JOIN 
        projects p ON p.id = c.project_id
    WHERE
        c.user_id = user_id;
    
    SET average_score = total_weighted_score / total_weight;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END//

DELIMITER ;
