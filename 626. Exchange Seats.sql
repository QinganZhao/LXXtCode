SELECT 
(CASE WHEN MOD(id, 2) = 1 AND id != count_id THEN id + 1
WHEN MOD(id, 2) = 1 AND id = count_id THEN id 
ELSE id - 1 END) id, student
FROM seat, 
(SELECT COUNT(*) count_id FROM seat) counted_id
ORDER BY id
