SELECT ROUND((SQRT(POW((p1.x - p2.x), 2) + POW((p1.y - p2.y), 2))), 2) 
AS shortest
FROM point_2d p1, point_2d p2
WHERE (p1.x, p1.y) != (p2.x, p2.y)
ORDER BY shortest
LIMIT 1
