/*
CHAR_LENGTH() 或 LENGTH() 函数来计算列中字符串的字符数。这两个函数的区别在于处理非 ASCII 字符时的行为：
    - CHAR_LENGTH() 返回字符串的字符数
    - LENGTH() 返回字符串的字节数。
对于 ASCII 字符，这两个函数的结果是相同的。
*/

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;