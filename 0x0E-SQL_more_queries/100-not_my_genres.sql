-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
USE hbtn_0d_tvshows;

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_shows.title = 'Dexter'
)
GROUP BY tv_genres.name
ORDER BY tv_genres.name ASC;
