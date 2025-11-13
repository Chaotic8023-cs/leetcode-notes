/*
用子查询先找出出现一次的数字，然后取其中的max即可。
*/
SELECT
    MAX(num) as num
FROM (
    SELECT
        num
    FROM
        MyNumbers
    GROUP BY
        num
    HAVING COUNT(*) = 1
) AS n  -- FROM后面的子查询必须要加alias！

/*
子查询也可以用 WHERE IN代替！
*/
SELECT
    MAX(num) AS num
FROM
    MyNumbers
WHERE num IN ( -- 
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)

