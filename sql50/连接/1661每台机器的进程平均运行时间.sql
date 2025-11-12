/*
自己的解法：
使用 SELF JOIN，将每个 (machine_id, process_id) 对应的end和start合并到一行，得到如下的结果：

    0	0	start	0.712	0	0	end	1.52
    0	1	start	3.14	0	1	end	4.12
    1	0	start	0.55	1	0	end	1.55
    1	1	start	0.43	1	1	end	1.42
    2	0	start	4.1	2	0	end	4.512
    2	1	start	2.5	2	1	end	5

然后再按 machine_id 合并并计算 end-start的平均值即可。
*/
SELECT
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM
    Activity AS a1 INNER JOIN Activity AS a2
    ON
        a1.machine_id = a2.machine_id
        AND a1.process_id = a2.process_id
        AND a1.activity_type = "start"
        AND a2.activity_type = 'end'
GROUP BY a1.machine_id



/*
不需要join的写法：
按 machine_id 分组，然后用一个if来求和，end乘上1，start乘上-1，最后除以 process_id的个数，即等效于求平均运行时间。
*/
SELECT
    machine_id,
    ROUND(SUM(IF(activity_type = "end", 1, -1) * timestamp) / COUNT(DISTINCT process_id), 3) AS processing_time
FROM
    Activity
GROUP BY
    machine_id