-- Write query to get number of graded assignments for each student:
-- count_grade_A_assignments_by_teacher_with_max_grading.sql
SELECT teacher_id, COUNT(*) AS grade_A_count
FROM assignments
WHERE grade = 'A'
GROUP BY teacher_id
ORDER BY grade_A_count DESC
LIMIT 1;

-- number_of_graded_assignments_for_each_student.sql
SELECT student_id, COUNT(*) AS graded_assignments_count
FROM assignments
WHERE state = 'GRADED'
GROUP BY student_id;
