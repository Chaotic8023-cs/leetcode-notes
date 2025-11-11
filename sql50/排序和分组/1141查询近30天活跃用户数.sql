/*
DATEDIFF(date1, date2) 返回两个日期之间相差的天数（date1 - date2）
在 MySQL 中，结果是一个整数，表示 date1 比 date2 晚了多少天。
    - 如果 date1 晚于 date2，结果为正数；
    - 如果 date1 早于 date2，结果为负数；
    - 如果两个日期相同，结果为 0。
*/

SELECT
    activity_date as day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE datediff('2019-07-27', activity_date) >= 0 and datediff('2019-07-27', activity_date) < 30  -- 前30天，包括 2019-07-27
GROUP BY activity_date;

/*
这里也可以将where换成group by后面的having（sql中执行顺序为 WHERE -> GROUP BY -> HAVING，这里由于是过滤日期，所以可以用WHERE先过滤，或分组后用HAVING过滤）
Having datediff('2019-07-27', activity_date) >= 0 and datediff('2019-07-27', activity_date) < 30;

也可以把datediff换成：
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
缺点是需要手动计算前30天的具体日期
*/

