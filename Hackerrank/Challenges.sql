SELECT h.hacker_id, h.name, COUNT(*) num
FROM Hackers h, Challenges c
WHERE h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING num = (SELECT COUNT(*) 
              FROM Challenges
              GROUP BY hacker_id
              ORDER BY COUNT(*) DESC
              LIMIT 1)
OR num IN (SELECT t.num
           FROM (SELECT COUNT(*) num
                 FROM Challenges
                 GROUP BY hacker_id) t
           GROUP BY t.num
           HAVING COUNT(t.num) = 1)
ORDER BY num DESC, h.hacker_id
