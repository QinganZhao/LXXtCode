SELECT salary * months AS earnings, COUNT(*)
FROM Employee
WHERE salary * months = (SELECT MAX(salary * months) FROM Employee)
GROUP BY earnings
