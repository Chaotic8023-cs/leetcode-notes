/*
自己的解法：
观察输出，每个学生都要有所有的subject，所以先用Students表和Subjects表进行cross join得到笛卡尔积，
然后再left join Examinations表，最后统计subject_name即可（NULL会自动统计为0，满足题目条件）
*/
SELECT
    stu.student_id, stu.student_name, sub.subject_name, COUNT(exam.subject_name) AS attended_exams
FROM
    Students as stu CROSS JOIN Subjects as sub
    LEFT JOIN Examinations AS exam ON stu.student_id = exam.student_id AND sub.subject_name = exam.subject_name
GROUP BY stu.student_id, stu.student_name, sub.subject_name
ORDER BY stu.student_id, sub.subject_name