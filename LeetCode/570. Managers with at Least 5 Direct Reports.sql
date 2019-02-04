SELECT E1.Name 
FROM Employee E1, Employee E2
WHERE E1.Id = E2.ManagerId
GROUP BY E1.Name 
HAVING COUNT(*) >= 5
