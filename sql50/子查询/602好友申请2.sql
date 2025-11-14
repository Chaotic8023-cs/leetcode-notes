/*
好友数其实就是发了多少个请求+接受了多少个请求，所以直接将所有requester_id和accepter_id两列合并起来（不去重），
再分组统计即可！
*/
SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) AS t
GROUP BY
    id
ORDER BY 
    COUNT(*) DESC
LIMIT 1

/*
自己的解法（史）：
先创建
    1. 发请求的人的好友cnt
    2. 接受请求的人的好友cnt
然后用UNION实现FULL JOIN，将接受请求的和发送请求的计数合起来：
    | rid  | cnt_r | aid  | cnt_a |
    | ---- | ----- | ---- | ----- |
    | 1    | 2     | null | null  |
    | 2    | 1     | 2    | 1     |
    | 3    | 1     | 3    | 2     |
    | null | null  | 4    | 1     |
我们会发现有的人只发出过请求（id=1），有的人只接受过请求（id=4），所以最后select的时候需要用IF判断，挑出rid和aid不为NULL的作为ID，
两个cnt之和作为好友数。
*/
WITH
    Request AS (
        SELECT
            requester_id as rid,
            COUNT(*) as cnt_r
        FROM
            RequestAccepted
        GROUP BY
            requester_id
    ),
    Accept AS (
        SELECT
            accepter_id as aid,
            COUNT(*) as cnt_a
        FROM
            RequestAccepted
        GROUP BY accepter_id
    )
SELECT
    IF(rid IS NOT NULL, rid, aid) AS id,
    IF(cnt_r IS NOT NULL, cnt_r, 0) + IF(cnt_a IS NOT NULL, cnt_a, 0) AS num
FROM (
    SELECT * FROM Request r LEFT JOIN Accept a ON r.rid = a.aid
    UNION
    SELECT * FROM Request r RIGHT JOIN Accept a ON r.rid = a.aid
) AS ra
ORDER BY
    num DESC
LIMIT 1