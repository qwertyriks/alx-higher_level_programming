-- This script creates the user user_0d_2 and
-- the database hbtn_0d_2.

-- user_0d_2 should only have SELECT privilege
-- in the database hbtn_0d_2

-- user_0d_2's password should be set to user_0d_2_pwd.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED By 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
