SELECT CASE WHEN g.Grade >= 8 THEN s.Name ELSE NULL END, g.Grade, s.Marks
FROM Students s, Grades g
WHERE s.Marks <= g.Max_Mark AND s.Marks >= g.Min_Mark
ORDER BY g.Grade DESC, s.Name, s.Marks
