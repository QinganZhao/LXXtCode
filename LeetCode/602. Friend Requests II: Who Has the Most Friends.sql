SELECT a.id id, 
COUNT(*) num
FROM 
((SELECT accepter_id id FROM request_accepted)
 UNION ALL
 (SELECT requester_id FROM request_accepted)) AS a
GROUP BY id
ORDER BY num DESC
LIMIT 1
