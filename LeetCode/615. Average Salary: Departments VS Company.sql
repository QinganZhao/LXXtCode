SELECT DATE_FORMAT(s.pay_date, '%Y-%m') AS pay_month, e.department_id,
(CASE WHEN ROUND(AVG(s.amount), 2) > ROUND(a.avg_mon, 2) THEN 'higher'
 WHEN ROUND(AVG(s.amount), 2) < ROUND(a.avg_mon, 2) THEN 'lower'
 ELSE 'same' END) comparison
FROM salary s, employee e,
(SELECT AVG(amount) avg_mon, DATE_FORMAT(pay_date, '%Y-%m') mon
 FROM salary
 GROUP BY DATE_FORMAT(pay_date, '%Y-%m'))
AS a
WHERE s.employee_id = e.employee_id 
AND DATE_FORMAT(s.pay_date, '%Y-%m') = a.mon
GROUP BY DATE_FORMAT(s.pay_date, '%Y-%m'), e.department_id
