-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the procedure
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN in_user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    
    -- Calculate the average score for the user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = in_user_id;
    
    -- Update the user's average_score
    UPDATE users
    SET average_score = avg_score
    WHERE id = in_user_id;
END //

DELIMITER ;
