/*

Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.



*/

SELECT tab.Triangle_Type
FROM(
SELECT A,B,C,
             CASE WHEN A+B > C AND A=B AND B=C AND A=C THEN "Equilateral"
              WHEN A+B > C AND A=B AND A <> C AND B <> C OR A=C AND A<>B AND B<>C THEN "Isosceles"
              WHEN A+B > C AND A <> B AND A<>C AND B<>C THEN "Scalene"
              WHEN A+B <= C THEN "Not A Triangle" END as Triangle_Type
FROM TRIANGLES)tab;
