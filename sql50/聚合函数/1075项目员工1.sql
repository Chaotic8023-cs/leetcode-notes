/*
自己的解法：
直接一个 inner join然后计算平均即可。
*/
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) as average_years
FROM
    Project as p INNER JOIN Employee as e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id
