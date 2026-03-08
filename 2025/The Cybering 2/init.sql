-- This ensures all subsequent commands are run against your new database
USE db;

-- Now create your tables and insert your data
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) NOT NULL PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    flag VARCHAR(255)
);
INSERT INTO users (username, password, flag) VALUES ("admin", "@Humpback34Walru5", "Intake{Th3re5ASQL2Th3Cyber1n9??}");