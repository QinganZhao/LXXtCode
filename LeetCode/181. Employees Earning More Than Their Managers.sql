# Write your MySQL query statement below
SELECT emp.Name AS Employee FROM Employee AS emp
LEFT JOIN Employee ON emp.ManagerId = Employee.Id
WHERE emp.Salary > Employee.Salary

