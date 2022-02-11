-- lists all cities
SELECT cities.id, cities.name, states.name FROM cities WHERE cities.state_id
= id ORDER BY cities.id ASC;
