/*
其实换id最方便，而不是换学生。
学生顺序保持不变，我们发现原来第一个学生（奇数id 1）变为了第二位，即奇数+1，同理偶数-1。
特殊情况是最后一位如果为奇数则不变，通过case处理即可。
*/
SELECT
    CASE
        WHEN id % 2 = 0 THEN id - 1  -- 偶数-1
        WHEN id = (SELECT COUNT(*) FROM Seat) THEN id  -- 最后一个如果为奇数则不变
        ELSE id + 1  -- 奇数+1
    END AS id,
    student
FROM Seat
ORDER BY id

/*
聪明办法：
观察结果可以发现，只需要所有偶数同学向前移动一位，即可满足条件。这里使用RANK窗口函数，
让所有偶数同学id-2，即可实现移动一位的排序！
*/
SELECT
    RANK() OVER (ORDER BY IF(id % 2 = 0, id - 2, id)) AS id,
    student
FROM Seat
ORDER BY id
