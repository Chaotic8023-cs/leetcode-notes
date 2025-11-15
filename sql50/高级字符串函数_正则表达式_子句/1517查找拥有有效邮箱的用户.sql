/*
使用正则表达式。
由于需要区分大小写，使用REGEXP_LIKE函数。
*/
SELECT
    user_id, name, mail
FROM
    Users
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$', 'c')  -- 'c'指case sensitive