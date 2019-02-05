SELECT
(CASE WHEN A = B AND B = C THEN 'Equilateral'
 WHEN (A = B AND A + B > C) OR (B = C AND B + C > A) OR (A = C AND A + C > B) THEN 'Isosceles'
 WHEN A + B > C AND A + C > B AND B + C > A THEN 'Scalene'
 ELSE 'Not A Triangle' END) Types
FROM TRIANGLES
