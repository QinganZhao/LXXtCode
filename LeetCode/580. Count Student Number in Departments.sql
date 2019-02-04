SELECT d.dept_name, COUNT(student_id) student_number
FROM student s
RIGHT JOIN department d ON s.dept_id = d.dept_id
GROUP BY d.dept_id
ORDER BY student_number DESC, dept_name
