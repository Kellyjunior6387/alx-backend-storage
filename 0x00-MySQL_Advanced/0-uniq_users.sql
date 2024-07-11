-- Create a table users with the following requirements:
-- The field id must be an autoincrement.
-- The field email must be unique.
-- The table must contain a field name.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
