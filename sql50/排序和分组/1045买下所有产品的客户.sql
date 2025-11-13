/*
自己的解法：
首先用子查询得到每个用户购买的产品数量，然后用where筛选出购买个数等于产品总数的用户即可。
*/
SELECT
    customer_id
FROM (
    SELECT
        customer_id,
        COUNT(DISTINCT product_key) as cnt
    FROM
        Customer
    GROUP BY
        customer_id
) AS c
WHERE c.cnt = (SELECT COUNT(*) FROM Product)

/*
简化版：子查询获得每个用户购买的产品个数直接放到having中就行
*/
SELECT
    customer_id
FROM
    Customer
GROUP BY
    customer_id
HAVING
    COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)