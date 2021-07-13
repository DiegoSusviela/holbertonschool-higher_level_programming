-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
