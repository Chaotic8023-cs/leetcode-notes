/*
自己的解法：
为了找到一个员工的所有下属，用 e1.id = e2.managerId 作为条件的 SELF INNER JOIN 能得到 领导-下属 的表，
然后通过领导id合并（e1.id，注意名字可能重复，但主键id不会），最后用having去掉小于5个下属的领导即可。
*/
SELECT
    e1.name
FROM
    Employee AS e1 INNER JOIN Employee AS e2
    ON e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(e1.id) >= 5