# Write your MySQL query statement below
SELECT d.Name Department, e.Name Employee, e.Salary
FROM Employee e 
JOIN Department d ON e.DepartmentId = d.Id
WHERE (
    SELECT COUNT(DISTINCT e1.Salary) FROM Employee e1
    WHERE e1.Salary > e.Salary
    AND e1.DepartmentId = e.DepartmentId
) < 3
ORDER BY Department, Salary DESC
