/*
筛选出符合条件的email然后删除。
*/
DELETE FROM Person
WHERE email IN ( -- 重复的email
    SELECT email FROM (
        SELECT email
        FROM Person
        GROUP BY email
        HAVING COUNT(*) > 1
    ) AS t1
) 
AND id NOT IN (  -- id不是重复email中最小的那个
    SELECT id FROM (
        SELECT MIN(id) AS id
        FROM Person
        GROUP BY email
        HAVING COUNT(*) > 1
    ) AS t2
)

/*
也可以先使用窗口函数给email分组排名，然后删除rank不为1的即可。
*/
WITH t AS (
    SELECT
        id, email,
        RANK() OVER (PARTITION BY email ORDER BY id) AS rnk
    FROM Person
)
DELETE FROM Person
WHERE id IN (
    SELECT id FROM t WHERE rnk != 1
)