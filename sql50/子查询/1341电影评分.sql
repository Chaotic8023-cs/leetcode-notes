/*
按题意分别写两个任务的查询再union起来即可。
需要注意的是：
1. 要加括号：直接在UNION前后的SELECT语句中使用ORDER BY和LIMIT通常会导致语法错误，因为UNION操作是在排序和限制之前执行的。
UNION首先会合并两个查询的结果集，然后才会考虑对合并后的结果集进行排序或限制。
2. 测试用例中有人名和电影名一样的情况，所以要用union all防止去重。
*/
(
    SELECT
        u.name AS results
    FROM
        MovieRating mr LEFT JOIN Users u
        ON mr.user_id = u.user_id
    GROUP BY
        mr.user_id
    ORDER BY
        COUNT(*) DESC, u.name
    LIMIT 1
)
UNION ALL
(
    SELECT
        m.title AS results
    FROM
        MovieRating mr LEFT JOIN Movies m
        ON mr.movie_id = m.movie_id
    WHERE
        mr.created_at >= "2020-02-01" AND mr.created_at < "2020-03-01"
    GROUP BY
        mr.movie_id
    ORDER BY AVG(rating) DESC, m.title
    LIMIT 1
)
