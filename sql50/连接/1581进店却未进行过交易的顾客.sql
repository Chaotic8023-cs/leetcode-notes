/*
自己的解法：
首先用 LEFT JOIN 得到 所有visits的数据，然后通过where transaction_id = null 进行过滤得到
所有没有交易的visits，最后用group by按customer_id分组并统计次数即可。
*/
SELECT
    v.customer_id,
    COUNT(*) as count_no_trans -- 经过where过滤后都是没有交易的visits，所以直接COUNT(*)
FROM
    Visits as v LEFT JOIN Transactions as t
    ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id