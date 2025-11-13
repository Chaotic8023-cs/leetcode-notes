/*
一个Having进行过滤即可。
*/
SELECT
    class
FROM
    Courses
GROUP BY
    class
HAVING
    COUNT(*) >= 5