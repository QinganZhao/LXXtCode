SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code),         
       COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), 
       COUNT(DISTINCT e.employee_code)
FROM Company c, Lead_manager l, Senior_manager s, Manager m, Employee e
WHERE c.company_code = l.company_code
AND l.company_code = s.company_code
AND s.company_code = m.company_code
AND m.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY c.company_code
