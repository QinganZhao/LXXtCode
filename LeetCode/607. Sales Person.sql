SELECT name
FROM salesperson
WHERE name NOT IN
(SELECT s.name
 FROM salesperson s, company c, orders o
 WHERE o.com_id = c.com_id AND o.sales_id = s.sales_id
 AND c.name = 'RED')
