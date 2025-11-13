/*
直接分别统计三个工资等级然后把三个表union一下即可。
*/
SELECT
    "Low Salary" AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION
SELECT
    "Average Salary" AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000
UNION
SELECT
    "High Salary" AS category,
    COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000