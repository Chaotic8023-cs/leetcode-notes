/*
自己的解法：
先一个join把product名字加到sales中，然后按product_id分组，having来保证所有销售记录的日期都在范围内。
*/
SELECT
    p.product_id, p.product_name
FROM
    Sales AS s INNER JOIN Product AS p
    ON s.product_id = p.product_id
GROUP BY
    p.product_id
HAVING
    MIN(s.sale_date) >= "2019-01-01" AND MAX(s.sale_date) <= "2019-03-31"  -- 注意，是所有销售记录都要在范围内！