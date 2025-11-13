/*
笨办法：
直接join三次，条件就是num相等且id递增
*/
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs l1
    INNER JOIN Logs l2 ON l1.num = l2.num AND l2.id = l1.id + 1
    INNER JOIN Logs l3 ON l2.num = l3.num AND l3.id = l2.id + 1

/*
笨办法的另一种写法
*/
SELECT
    DISTINCT num AS ConsecutiveNums FROM Logs 
WHERE
    (id+1, num) IN (SELECT * FROM Logs)
    AND (id+2, num) IN (SELECT * FROM Logs)

/*
使用窗口函数 LEAD 解决：
    LEAD(col, offset)用于在查询结果中访问下一行（后续行）的数据
我们使用窗口函数给表新增两列，分别是后一行和后两行的数，再用where筛选出num和后两行的num相等的即可！
*/
SELECT
    DISTINCT(num) as ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        LEAD(num, 1) OVER (ORDER BY ID) AS l1, -- 下一行
        LEAD(num, 2) OVER (ORDER BY ID) AS l2 -- 后续第2行
    FROM
        Logs
) AS l
WHERE num = l1 AND num = l2