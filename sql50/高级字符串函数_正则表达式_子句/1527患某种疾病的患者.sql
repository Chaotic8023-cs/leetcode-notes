/*
使用LIKE匹配
*/
SELECT
    patient_id, patient_name, conditions
FROM
    Patients
WHERE
    conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%'  -- DIAB1要么在开头，要么在中间某个空格后

/*
使用正则表达式匹配
匹配以 DIAB1 开头的疾病代码，它要么出现在字符串开头，要么前面有一个空格。
(^| )DIAB1 的意思是：
    ^：字符串开头
    （空格）：单词分隔符
    |：或者
    DIAB1：我们要匹配的关键字
*/
SELECT
    patient_id, patient_name, conditions
FROM
    Patients
WHERE
    conditions REGEXP '(^| )DIAB1'

