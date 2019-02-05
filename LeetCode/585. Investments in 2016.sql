SELECT ROUND(SUM(TIV_2016), 2) TIV_2016 FROM insurance i
WHERE i.TIV_2015 IN (SELECT TIV_2015 FROM insurance 
                     GROUP BY TIV_2015
                     HAVING COUNT(*) > 1)
AND i.PID IN (SELECT PID FROM insurance
              GROUP BY LAT, LON 
              HAVING COUNT(*) = 1)
