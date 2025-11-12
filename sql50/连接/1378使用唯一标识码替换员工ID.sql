/*
观察输出发现，需要所有名字，所以使用 LEFT JOIN 即可。
*/
SELECT
    t2.unique_id,
    t1.name
FROM
    Employees as t1 LEFT JOIN EmployeeUNI as t2 ON t1.id = t2.id