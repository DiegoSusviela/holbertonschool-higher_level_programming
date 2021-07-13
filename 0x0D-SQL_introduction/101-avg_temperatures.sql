-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
