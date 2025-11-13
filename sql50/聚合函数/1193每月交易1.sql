/*
自己的解法：
主要是解决如何按月分组：先使用 DATE_FORMAT 函数将日期转为 年-月 的形式，然后以这个形式 group by。
*/
SELECT
    DATE_FORMAT(trans_date, '%Y-%m') AS month, -- 转化为 年-月 格式，以便后面按月进行分组
    country,
    count(*) AS trans_count,
    SUM(state = "approved") AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = "approved", amount, 0)) AS approved_total_amount
FROM
    Transactions
GROUP BY month, country