/*
使用 DENSE_RANK 排名即可满足题意（不同工资的前3）：当出现两个并列第1时，第三个人的名从2开始。（RANK会从3开始）
*/
SELECT
    department_name AS Department,
    employee_name AS Employee,
    salary AS Salary
FROM (
    SELECT
        d.name AS department_name,  -- 注意：当子查询中有两个列名一样时，需要起一个alias方便外层调用
        e.name AS employee_name,
        e.salary,
        DENSE_RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rk  -- 按department分组
    FROM
        Employee e INNER JOIN Department d
        ON e.departmentId = d.id
) AS t
WHERE rk <= 3