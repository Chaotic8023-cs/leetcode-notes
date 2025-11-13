/*
本题核心是选出 <= 目标日期"2019-08-16"的最大的那一天。
解决方法是先用where过滤出来所有足目标日期之前的行，然后使用窗口函数 ROW_NUMBER 按日期倒排标记，
最后选出第一行，即"2019-08-16"前的最大的那天。
注意：MySQL的执行顺序是 from -> where -> group by -> having -> select -> order by，
所以是where先执行筛选出符合条件的日期，再用窗口函数标注行数！
最后，对于那些所有记录都是目标日期之后的，我们筛选出来使用默认的10元价格。
*/
SELECT
    product_id,
    new_price AS price
FROM (
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM
        Products
    WHERE
        change_date <= "2019-08-16"
) AS p
WHERE rn = 1
UNION  -- 所有记录都出现在目标日期之后的，单独筛选出来进行 UNION
SELECT
    product_id, 10 AS price
FROM
    Products
GROUP BY
    product_id
HAVING MIN(change_date) > "2019-08-16"

/*
筛选目标日期之后的还能使用 NOT IN:

SELECT
    product_id, 10 AS price
FROM
    Products
WHERE
    product_id NOT IN (
        SELECT product_id FROM Products WHERE change_date <= "2019-08-16"
    )
*/




