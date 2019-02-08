SELECT SUM(ci.POPULATION)
FROM CITY ci, COUNTRY co
WHERE ci.CountryCode = co.code AND co.CONTINENT = 'Asia'
