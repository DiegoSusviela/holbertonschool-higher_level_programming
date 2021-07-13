-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_shows DESC;
