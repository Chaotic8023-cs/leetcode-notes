/*
和1174题一样，用窗口函数即可解决：
先利用窗口函数找到每个玩家第一次登陆的日期，然后用一个case找出第二天登录的个数，除以玩家个数即可。
*/
SELECT
    ROUND(SUM(
        CASE
            WHEN DATEDIFF(a.event_date, a.first_date) = 1 AND games_played > 0 THEN 1
            ELSE 0
        END
    ) / COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT
        player_id,
        device_id,
        event_date,
        games_played,
        MIN(event_date) OVER (PARTITION BY player_id) AS first_date
    FROM Activity
) AS a