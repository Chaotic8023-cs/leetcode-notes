/*
窗口函数的应用：
1. 首先利用窗口函数创建一个新列 first_order_date，找出每个客户的首单日期
2. 然后利用CASE（或IF）直接计算所有客户首单为即时订单的个数，除以总客户数即可。
*/
SELECT
    ROUND(SUM(
        CASE
            WHEN d.order_date = d.first_order_date AND d.order_date = d.customer_pref_delivery_date THEN 1
            ELSE 0
        END
    ) / COUNT(DISTINCT d.customer_id) * 100, 2) AS immediate_percentage
FROM (
    SELECT
        customer_id,
        order_date,
        customer_pref_delivery_date,
        MIN(order_date) OVER (PARTITION BY customer_id) AS first_order_date
    FROM Delivery
) AS d