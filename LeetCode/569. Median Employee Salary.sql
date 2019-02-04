SELECT E1.id, E1.Company, E1.Salary
FROM Employee E1, Employee E2
WHERE E1.Company = E2.Company
GROUP BY E1.Company, E1.Salary
HAVING SUM(CASE WHEN E1.Salary = E2.salary THEN 1 ELSE 0 END) >= ABS(SUM(SIGN(E1.Salary - E2.Salary)))
ORDER BY Company
