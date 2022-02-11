--  lists all the cities of California that can be found in the database
SELECT id, name FROM cities WHERE state_id = (
SELECT id from states WHERE name = 'California') ORDER BY ASC;
