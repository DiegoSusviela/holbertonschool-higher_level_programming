-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;
