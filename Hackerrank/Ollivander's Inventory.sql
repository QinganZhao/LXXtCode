SELECT w.id, t.* FROM
(SELECT p.age, MIN(w.coins_needed) coin, w.power 
FROM Wands w, Wands_Property p
WHERE w.code = p.code
AND p.is_evil = 0
GROUP BY p.age, w.power) t
JOIN Wands w ON w.coins_needed = t.coin AND w.power = t.power
JOIN Wands_Property p ON w.code = p.code AND p.age = t.age
ORDER BY w.power DESC, p.age DESC
