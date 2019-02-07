SET @did:=0, @pid:=0, @sid:=0, @aid:=0;
SELECT MIN(doctor), MIN(professor), MIN(singer), MIN(actor)
FROM (SELECT (CASE WHEN Occupation = 'Doctor' THEN @did:=@did+1
                   WHEN Occupation = 'Professor' THEN @pid:=@pid+1
                   WHEN Occupation = 'Singer' THEN @sid:=@sid+1
                   WHEN Occupation = 'Actor' THEN @aid:=@aid+1 END) id,
             (CASE WHEN Occupation = 'Doctor' THEN name END) doctor,
             (CASE WHEN Occupation = 'Professor' THEN name END) professor,
             (CASE WHEN Occupation = 'Singer' THEN name END) singer,
             (CASE WHEN Occupation = 'Actor' THEN name END) actor
      FROM OCCUPATIONS
      ORDER BY name) occ
GROUP BY id
