SELECT *
FROM cinema
WHERE NOT description = "boring"
    AND id % 2 = 1 -- 或者用mod函数：mod(id, 2) = 1
ORDER BY rating DESC;