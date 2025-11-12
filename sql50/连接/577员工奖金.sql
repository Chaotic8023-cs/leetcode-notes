/*
自己的解法：
观察输出可以看出NULL也要，所以用LEFT JOIN + where过滤即可。
*/
SELECT
    e.name,
    b.bonus
FROM
    Employee AS e LEFT JOIN Bonus AS b
    ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL