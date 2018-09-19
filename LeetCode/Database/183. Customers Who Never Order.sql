# Write your MySQL query statement below
SELECT Name Customers FROM Customers c
WHERE c.Id NOT IN (SELECT CustomerId FROM Orders)