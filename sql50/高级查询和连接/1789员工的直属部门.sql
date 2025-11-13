/*
自己的解法：
按employee_id分组，然后用一个case去分情况讨论
*/
SELECT
    employee_id,
    CASE
        WHEN COUNT(*) = 1 THEN MAX(department_id)  -- 只有一个部门时则这个部门就是直属部门（这里用MAX因为department_id不在聚合列中，所以得用一个聚合函数）
        ELSE SUM(IF(primary_flag = "Y", department_id, 0))  -- 有多个部门时取primary_flag为Y的那个部门，这里用一个SUM+IF来得到
    END
    AS department_id
FROM
    Employee
GROUP BY
    employee_id

/*
方法2：用Union合并只有一个部门的员工及明确拥有直属部门的员工
*/
SELECT employee_id, department_id
FROM employee
GROUP BY employee_id
HAVING COUNT(department_id) = 1 -- 只有一个部门的员工
UNION
SELECT employee_id, department_id
FROM employee
WHERE primary_flag = "Y"  -- 直接用where筛选出primary_flag为Y的员工即有明确直属部门的员工