SELECT E1.Id, E1.Month,
IFNULL(E1.Salary, 0) + IFNULL(E2.Salary, 0) + IFNULL(E3.Salary, 0) Salary
FROM 
(SELECT MAX(Month) MS, Id FROM Employee GROUP BY Id HAVING COUNT(*) > 1) AS m
LEFT JOIN Employee E1 ON E1.id = m.id AND m.MS != E1.Month
LEFT JOIN Employee E2 ON E2.id = E1.id AND E2.Month = E1.Month - 1
LEFT JOIN Employee E3 ON E3.id = E1.id AND E3.Month = E1.Month - 2
ORDER BY Id, Month DESC
