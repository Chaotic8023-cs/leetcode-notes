/*
自己的解法：
主要是用DATE_FORMAT函数判断是否日期是2020年2月。
*/
SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    Orders o INNER JOIN Products p
    ON o.product_id = p.product_id
WHERE DATE_FORMAT(o.order_date, "%Y-%m") = '2020-02'
GROUP BY o.product_id
HAVING SUM(o.unit) >= 100