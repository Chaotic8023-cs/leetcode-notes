/*
自己的解法：
主要考察 **关联子查询** 的应用
*/
SELECT
    ROUND(SUM(i1.tiv_2016), 2) AS tiv_2016
FROM
    Insurance i1
WHERE EXISTS (  -- 第一个条件：他在 2015 年的投保额 (tiv_2015) 至少跟一个其他投保人在 2015 年的投保额相同。
    SELECT 1
    FROM Insurance i2
    WHERE i1.pid != i2.pid AND i1.tiv_2015 = i2.tiv_2015
)
AND NOT EXISTS (  -- 他所在的城市必须与其他投保人都不同（也就是说 (lat, lon) 不能跟其他任何一个投保人完全相同）。
    SELECT 1
    FROM Insurance i3
    WHERE i1.pid != i3.pid AND (i1.lat, i1.lon) = (i3.lat, i3.lon)
)