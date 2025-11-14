/*
使用窗口函数SUM 配合RANGE INTERVAL 6 DAY PRECEDING（窗口函数中的frame clause）统计每个日期+前6天内的累计销售额，
最后用DATEDIFF筛选出后面的那些天（从第一个第7天开始）。
注意，用distinct是因为示例中2019-01-10是重复的，所以窗口函数会给出两个一样的这天的结果，需去重
*/
SELECT
    visited_on,
    amount,
    ROUND(amount / 7, 2) AS average_amount
FROM (
    SELECT DISTINCT
        visited_on,
        SUM(amount) OVER (ORDER BY visited_on RANGE INTERVAL 6 DAY PRECEDING) AS amount
    FROM
        Customer
) AS c
WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6