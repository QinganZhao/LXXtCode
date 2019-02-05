SELECT DISTINCT c1.seat_id FROM cinema c1, cinema c2
WHERE c1.free != 0
AND c2.free != 0
AND (c1.seat_id - 1 = c2.seat_id
OR c1.seat_id + 1 = c2.seat_id)
ORDER BY seat_id
