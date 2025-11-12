/*
自己的解法：
由于所有的product_id都要计算均价，所以先用Prices表 left join UnitsSold，条件包括交易的时间在售价时间范围内，
这样就得到了所有交易时的售价。然后，按product_id合并，用总售价除以给个数得到平均售价。注意某些时间段可能没有卖出，
所以left join后会会是NULL，需要用IFNULL处理！
*/
SELECT
    p.product_id,
    ROUND(
        IFNULL(SUM(p.price * u.units) / SUM(u.units), 0), -- 有些没卖掉所以会是NULL，需要用IFNULL处理
        2) AS average_price
FROM
    Prices as p LEFT JOIN UnitsSold as u
    ON p.product_id = u.product_id AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY p.product_id