/*
按user_id分组然后按user_id排序即可
*/
SELECT
    user_id,
    COUNT(*) AS followers_count
FROM
    Followers
GROUP BY
    user_id
ORDER BY
    user_id