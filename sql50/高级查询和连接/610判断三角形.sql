/*
主要考察三角形的构成条件（两短边长度之和需大于最长边）
设 x <= y <= z，则只需要判断 x + y > z 的结果即可
两边同时加上 z，得到 x + y + z > 2 * z，即 sum(x, y, z) > 2 * max(x, y, z)
用这个式子判断就不需要考虑 x, y, z 的大小关系了
*/
SELECT
    x, y, z,
    IF(x + y + z > 2 * GREATEST(x, y, z), 'Yes', 'No') AS Triangle  -- 注意不能用聚合函数，加法直接加，取max用GREATEST标量函数
FROM
    Triangle