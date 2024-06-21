/*
Enter your query here.
*/
SELECT 
CASE
    WHEN NOT ((A+B>C) AND (B+C>A) AND (A+C>B)) THEN 'Not A Triangle'
    WHEN ((A=B AND A!=C) OR (B=C AND A!=C) OR (C=A AND B!=C)) THEN 'Isosceles'
    WHEN (A=B AND B=C) THEN 'Equilateral'
    ELSE 'Scalene'
END
FROM TRIANGLES
