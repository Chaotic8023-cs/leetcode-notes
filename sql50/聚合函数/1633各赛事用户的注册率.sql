-- 不需要join，用一个子查询从Users表得到用户总数作为分母即可！
SELECT
    contest_id,
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;