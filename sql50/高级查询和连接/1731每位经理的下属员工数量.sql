/*
自己的解法：
1. 用with创建个临时表Managers，包含所有manager的id和名字
2. 用manager和employee表在 e.reports_to = m.employee_id 上inner join，这样就只保留了需要reports to的员工，并给他们配上对应manager的信息，
最后按manager id分组并计算下属个数和平均年龄即可。
*/
WITH Managers AS (
    SELECT
        m.employee_id,
        e.name
    FROM
        Employees AS e INNER JOIN
        (SELECT DISTINCT reports_to AS employee_id FROM Employees) AS m -- 筛选出所有manager的id
        ON e.employee_id = m.employee_id
)
SELECT
    m.employee_id,
    m.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e.age), 0) AS average_age
FROM
    Employees AS e INNER JOIN Managers AS m
    ON e.reports_to = m.employee_id
GROUP BY
    m.employee_id, m.name
ORDER BY m.employee_id

/*
简化版：其实不用先单独创建一个Manager的表，直接一个self inner join就可以：
e1作为下属表，e2作为领导表，直接一join即可
*/
SELECT
    e2.employee_id,
    e2.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e1.age), 0) AS average_age -- 下属的平均年龄
FROM
    Employees e1 INNER JOIN Employees e2  -- e1：下属，e2：领导
    ON e1.reports_to = e2.employee_id
GROUP BY
    e2.employee_id  -- 按领导分组（e1.reports_to也可以）
ORDER BY
    e2.employee_id
