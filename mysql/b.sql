CREATE USER 'auser'@'%' IDENTIFIED BY 'pw';

GRANT ALL PRIVILEGES ON adb.* TO 'auser'@'%'
WITH GRANT OPTION;

-- Set password and grant at once
-- Not work?
-- GRANT ALL PRIVILEGES ON adb.* TO 'auser'@'%' IDENTIFIED BY 'pw';
