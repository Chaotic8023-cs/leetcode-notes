/*
使用窗口函数SUM得到累加的体重，然后where筛选出 <=1000的，最后通过按turn倒排+limit取出turn最大的那个
*/
SELECT
    person_name
FROM (
    SELECT
        *,
        SUM(weight) OVER (ORDER BY turn) AS acc_weight
    FROM
        Queue
) AS q1
WHERE
    acc_weight <= 1000
ORDER BY turn DESC
LIMIT 1


/*
倒排+LIMIT取出turn最大的可以替换为使用RANK窗口函数：
*/
WITH
    q1 AS ( -- q1负责获取累加体重
        SELECT
            *,
            SUM(weight) OVER (ORDER BY turn) as acc_weight
        FROM
            Queue
    ),
    q2 AS ( -- q2负责筛选出累加体重 <= 1000的，并加入rank，然后按turn倒排
        SELECT
            *,
            RANK() OVER(ORDER BY turn DESC) as rnk
        FROM q1
        WHERE acc_weight <= 1000
    )

SELECT
    person_name
FROM q2
WHERE rnk = 1 -- 最后选出最大的那个turn（rank=1）的即可