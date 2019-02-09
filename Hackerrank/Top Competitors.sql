SELECT h.hacker_id, h.name
FROM Hackers h, Difficulty d, Challenges c, Submissions s
WHERE h.hacker_id = s.hacker_id AND s.challenge_id = c.challenge_id
AND d.difficulty_level = c.difficulty_level AND s.score = d.score
GROUP BY h.hacker_id, h.name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC, h.hacker_id
