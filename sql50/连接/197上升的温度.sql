/*
自己的解法：
使用self join，条件为日期大1以及温度更高。
*/
SELECT
    w1.id -- 注意，这里必须是w1，不能是w2，因为条件中以w1为基准的！
FROM
    Weather as w1 INNER JOIN Weather as w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1 AND w1.Temperature > w2.Temperature
