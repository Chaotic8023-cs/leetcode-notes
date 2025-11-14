/*
使用DENSE_RANK排序即可满足第二高的不同工资这个条件。
需要注意的时候，不存在时要返回NULL，如果直接用SELECT DISTINCT salary就会返回空而不是NULL，所以需要单独用IF处理。
*/
SELECT
    IF(COUNT(*) != 0, MAX(salary), NULL) AS SecondHighestSalary -- 或着直接使用 MAX(salary)，MAX也会返回NULL！
FROM (
    SELECT
        *,
        DENSE_RANK() OVER(ORDER BY salary DESC) AS rk
    FROM
        Employee
) AS t
WHERE rk = 2