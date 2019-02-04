SELECT Name FROM Candidate WHERE id = 
(SELECT V.CandidateId FROM Vote V
GROUP BY V.CandidateId
ORDER BY COUNT(*) DESC
LIMIT 1)
