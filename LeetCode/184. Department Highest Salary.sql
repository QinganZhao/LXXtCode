# Write your MySQL query statement below
SELECT d.Name Department, e.name Employee, e.Salary
FROM Employee e
JOIN Department d ON e.DepartmentId = d.Id
WHERE (e.DepartmentId, e.Salary) IN (
    SELECT e.DepartmentId, MAX(e.Salary)
    FROM Employee e
    GROUP BY e.DepartmentId
)