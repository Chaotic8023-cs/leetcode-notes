/*
主要考察 GROUP_CONCAT 函数：
    GROUP_CONCAT() 是用来把同一组中的多行字符串合并成一行的函数。

注：在聚合函数内部（例如本题的GROUP_CONCAT），可以使用 DISTINCT、ORDER BY、SEPARATOR 等关键字来控制函数行为
*/
SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date