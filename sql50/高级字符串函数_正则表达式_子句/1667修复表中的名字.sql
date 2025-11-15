/*
用到的函数：
- CONCAT 用来拼接字符串
- LEFT 从左边截取字符
- RIGHT 从右边截取字符
- UPPER 变为大写
- LOWER 变为小写
- LENGTH 获取字符串长度
*/
SELECT
    user_id,
    CONCAT(UPPER(left(name, 1)), LOWER(right(name, LENGTH(name) - 1))) AS name
FROM Users
ORDER BY user_id