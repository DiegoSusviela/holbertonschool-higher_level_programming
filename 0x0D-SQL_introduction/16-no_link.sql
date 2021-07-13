-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
