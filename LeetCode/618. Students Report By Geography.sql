SELECT America, Asia, Europe
FROM 
(SELECT @AM:=0, @AS:=0, @EU:=0) AS id,
(SELECT @AS:=@AS+1 AS_id, name Asia
 FROM student
 WHERE continent = 'Asia'
 ORDER BY Asia) AS Asia
RIGHT JOIN
(SELECT @AM:=@AM+1 AM_id, name America
 FROM student
 WHERE continent = 'America'
 ORDER BY America) AS America
ON AM_id = AS_id
LEFT JOIN
(SELECT @EU:=@EU+1 EU_id, name Europe
 FROM student
 WHERE continent = 'Europe'
 ORDER BY Europe) AS Europe
ON AM_id = EU_id
