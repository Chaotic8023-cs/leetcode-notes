/*
自己的解法：
LEFT JOIN后用一个if来统计confirmed的个数，COUNT(*)来统计所有的请求数。

注意：
也可以不用 IF，用 SUM(c.action = "confirmed")，因为布尔表达式会被自动转为值。
但是，left join后某些action会是NULL，这样SUM(NULL)最终也会变为NULL，而不是0，
所以我们要套一个 IFNULL 函数，来确保NULL时输出0：
    IFNULL(SUM(c.action = "confirmed"), 0)
*/
SELECT
    s.user_id,
    ROUND(SUM(IF(c.action = "confirmed", 1, 0)) / COUNT(*), 2) AS confirmation_rate
FROM
    Signups as s LEFT JOIN Confirmations as c
    ON s.user_id = c.user_id
GROUP BY s.user_id