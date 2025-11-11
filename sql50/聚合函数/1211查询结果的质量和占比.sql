-- MYSQL中真值为1，假值为0，故可用AVG计算 poor_query_percentage
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(100 * AVG(rating < 3), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;