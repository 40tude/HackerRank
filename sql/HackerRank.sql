/*
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
JOIN another_table
ON mytable.column = another_table.column
WHERE constraint_expression
GROUP BY column
HAVING constraint_expression
ORDER BY column ASC/DESC
LIMIT count OFFSET COUNT;
 */
-- Voir aussi les exos sur aussi : https://sqlbolt.com/
-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT
  (COUNT(CITY) - COUNT(DISTINCT CITY))
FROM
  STATION;

-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
SELECT
  CITY
FROM
  STATION
WHERE
  (LOWER(CITY) LIKE "a%")
  OR (LOWER(CITY) LIKE "e%")
  OR (LOWER(CITY) LIKE "i%")
  OR (LOWER(CITY) LIKE "o%")
  OR (LOWER(CITY) LIKE "u%");

SELECT
  CITY
FROM
  STATION
WHERE
  (CITY LIKE "a%")
  OR (CITY LIKE "e%")
  OR (CITY LIKE "i%")
  OR (CITY LIKE "o%")
  OR (CITY LIKE "u%");

/******************************************************************************
17 10 2023
 ******************************************************************************/
-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (CITY LIKE "%a")
  OR (CITY LIKE "%e")
  OR (CITY LIKE "%i")
  OR (CITY LIKE "%o")
  OR (CITY LIKE "%u");

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. 
-- Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (
    (CITY LIKE "%a")
    OR (CITY LIKE "%e")
    OR (CITY LIKE "%i")
    OR (CITY LIKE "%o")
    OR (CITY LIKE "%u")
  )
  AND (
    (CITY LIKE "a%")
    OR (CITY LIKE "e%")
    OR (CITY LIKE "i%")
    OR (CITY LIKE "o%")
    OR (CITY LIKE "u%")
  );

-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (CITY NOT LIKE "a%")
  AND (CITY NOT LIKE "e%")
  AND (CITY NOT LIKE "i%")
  AND (CITY NOT LIKE "o%")
  AND (CITY NOT LIKE "u%");

-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (CITY NOT LIKE "%a")
  AND (CITY NOT LIKE "%e")
  AND (CITY NOT LIKE "%i")
  AND (CITY NOT LIKE "%o")
  AND (CITY NOT LIKE "%u");

-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (
    (
      (CITY NOT LIKE "%a")
      AND (CITY NOT LIKE "%e")
      AND (CITY NOT LIKE "%i")
      AND (CITY NOT LIKE "%o")
      AND (CITY NOT LIKE "%u")
    )
    OR (
      (CITY NOT LIKE "a%")
      AND (CITY NOT LIKE "e%")
      AND (CITY NOT LIKE "i%")
      AND (CITY NOT LIKE "o%")
      AND (CITY NOT LIKE "u%")
    )
  );

-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT
  CITY
FROM
  STATION
WHERE
  (
    (
      (CITY NOT LIKE "%a")
      AND (CITY NOT LIKE "%e")
      AND (CITY NOT LIKE "%i")
      AND (CITY NOT LIKE "%o")
      AND (CITY NOT LIKE "%u")
    )
    AND (
      (CITY NOT LIKE "a%")
      AND (CITY NOT LIKE "e%")
      AND (CITY NOT LIKE "i%")
      AND (CITY NOT LIKE "o%")
      AND (CITY NOT LIKE "u%")
    )
  );

-- Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
SELECT
  name
FROM
  Employee
ORDER BY
  name ASC;

-- Write a query that prints a list of employee names (i.e.: the name attribute) 
-- for employees in Employee having a salary greater than 2000 per month 
-- who have been employees for less than 10 months. 
-- Sort your result by ascending employee_id.
SELECT
  name
FROM
  Employee
WHERE
  (
    (salary > 2000)
    AND (months < 10)
  )
ORDER BY
  employee_id ASC;

-- Query the Name of any student in STUDENTS 
-- who scored higher than 75 Marks. 
-- Order your output by the last three characters of each name. 
-- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
-- secondary sort them by ascending ID.
SELECT
  Name
FROM
  Students
WHERE
  (Marks > 75)
ORDER BY
  SUBSTR (Name, -3, 3) ASC, -- Should work with MySQL and SQLite. MySQL accepts SUBSTR(Name, -3) 
  Id ASC;

-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
-- Query the two cities in STATION with 
-- the shortest and longest CITY names, 
-- as well as their respective lengths (i.e.: number of characters in the name). 
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
-- Fonctionne dans SQLite sur le premier exemple mais pas dans MySQL !!!
CREATE TABLE
  STATION (CITY text);

INSERT INTO
  STATION (CITY)
VALUES
  ('WXY'),
  ('ABC'),
  ('DEF'),
  ('PQRS');

SELECT
  *
FROM
  STATION;

SELECT
  CITY,
  MIN(LENGTH (CITY))
FROM
  (
    SELECT
      *
    FROM
      STATION
    ORDER BY
      CITY ASC
  );

SELECT
  CITY,
  MAX(LENGTH (CITY))
FROM
  (
    SELECT
      *
    FROM
      STATION
    ORDER BY
      CITY ASC
  );

-- Fonctionne avec MySQL
-- Penser à LIMIT 1
SELECT
  CITY,
  MIN(LENGTH (CITY))
FROM
  STATION
GROUP BY
  CITY
ORDER BY
  MIN(LENGTH (CITY)) ASC,
  CITY ASC
LIMIT
  1;

SELECT
  CITY,
  MAX(LENGTH (CITY))
FROM
  STATION
GROUP BY
  CITY
ORDER BY
  MAX(LENGTH (CITY)) DESC,
  CITY ASC
LIMIT
  1;

/******************************************************************************
18 10 2023
 ******************************************************************************/
-- Query a count of the number of cities in CITY having a Population larger than 100000
SELECT
  COUNT(NAME) AS Nombre
FROM
  CITY
WHERE
  POPULATION > 100000
  -- Query the total population of all cities in CITY where District is California.
SELECT
  SUM(POPULATION)
FROM
  CITY
WHERE
  DISTRICT = "California"
  -- Query the average population of all cities in CITY where District is California.
SELECT
  AVG(POPULATION)
FROM
  CITY
WHERE
  DISTRICT = "California"
  -- Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
SELECT
  SUM(POPULATION)
FROM
  CITY
WHERE
  COUNTRYCODE = "JPN"
  -- Query the difference between the maximum and minimum populations in CITY.
SELECT
  MAX(POPULATION) - MIN(POPULATION)
FROM
  CITY
  -- Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT
  CAST(AVG(POPULATION) AS SIGNED)
FROM
  CITY;

-- MySQL
SELECT
  CAST(AVG(POPULATION) AS INT)
FROM
  CITY;

-- SQLite
-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2375. 
-- Truncate your answer to 4 decimal places.
SELECT
  ROUND(SUM(LAT_N), 4)
FROM
  STATION
WHERE
  LAT_N > 38.7880
  AND LAT_N < 137.2345;

-- Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. 
-- Truncate your answer to  decimal places.
SELECT
  ROUND(MAX(LAT_N), 4)
FROM
  STATION
WHERE
  LAT_N < 137.2345;

-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 3877.80 . Round your answer to  decimal places.
SELECT
  ROUND(MIN(LAT_N), 4)
FROM
  STATION
WHERE
  LAT_N > 38.7880;

/******************************************************************************
19 10 2023
 ******************************************************************************/
-- Somme des population des villes d'asie
SELECT
  SUM(CITY.POPULATION)
FROM
  CITY
  JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE
  COUNTRY.CONTINENT = "Asia";

-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
SELECT
  CITY.NAME
FROM
  CITY
  JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE
  COUNTRY.CONTINENT = "Africa";

-- Given the CITY and COUNTRY tables, 
-- query the names of all the continents (COUNTRY.Continent) 
-- and their respective average city populations (CITY.Population) rounded down to the nearest integer.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
-- Floor. MySQL. Return the largest integer value that is less than or equal to the argument
SELECT
  COUNTRY.CONTINENT,
  FLOOR(AVG(CITY.POPULATION))
FROM
  CITY
  JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY
  COUNTRY.CONTINENT;

/******************************************************************************
20 10 2023
 ******************************************************************************/
-- Query the following two values from the STATION table:
-- The sum of all values in LAT_N rounded to a scale of  decimal places.
-- The sum of all values in LONG_W rounded to a scale of  decimal places.
SELECT
  ROUND(SUM(LAT_N), 2),
  ROUND(SUM(LONG_W), 2)
FROM
  STATION;

-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345
-- Round your answer to  decimal places.
SELECT
  ROUND(LONG_W, 4)
FROM
  STATION
WHERE
  LAT_N < 137.2345
ORDER BY
  LAT_N DESC
LIMIT
  1;

-- Query the Western Longitude (LONG_W)
-- where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. 
-- Round your answer to  decimal places.
SELECT
  ROUND(LONG_W, 4)
FROM
  STATION
WHERE
  LAT_N > 38.7780
ORDER BY
  LAT_N ASC
LIMIT
  1;

-- We define an employee's total earnings to be their monthly salary*months worked
-- and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. 
-- Write a query to find the maximum total earnings for all employees 
-- as well as the total number of employees who have maximum total earnings. 
-- Then print these values as 2 space-separated integers.
SELECT
  (months * salary) AS earnings,
  COUNT(*)
FROM
  Employee
GROUP BY
  earnings
ORDER BY
  earning DESC
LIMIT
  1;

-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, 
-- but did not realize her keyboard's  key was broken until after completing the calculation. 
-- She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), 
-- and the actual average salary.
-- Write a query calculating the amount of error (i.e.: actual - miscalculated average monthly salaries), 
-- and round it up to the next integer.
SELECT
  CEIL((AVG(salary)) - (AVG(REPLACE (salary, '0', '')))) AS avg_salary
FROM
  employees;

-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
-- Output one of the following statements for each record in the table:
-- Equilateral: It's a triangle with  sides of equal length.
-- Isosceles: It's a triangle with  sides of equal length.
-- Scalene: It's a triangle with  sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle. Cannot form a triangle because the combined value of sides A and B is not larger than that of side .
-- Not sure it works with SQLite
SELECT
  CASE
    WHEN (A + B) <= C THEN "Not A Triangle"
    WHEN A = B
    AND A = C THEN "Equilateral"
    WHEN A = B
    OR A = C
    OR B = C THEN "Isosceles"
    WHEN A <> B
    AND B <> C THEN "Scalene"
  END
FROM
  TRIANGLES;

/******************************************************************************
21 10 2023
 ******************************************************************************/
-- Consider P1(a,b) and P2(c,d) to be two points on a 2D plane.
-- a happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
-- b happens to equal the minimum value in Western Longitude (LONG_W in STATION).
-- c happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
-- d happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points P1 and P2 and round it to a scale of  decimal places.
-- Manhattan Distance = |xb-xa| + |yb-ya|
SELECT
  ROUND(
    ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W)),
    4
  )
FROM
  STATION;

-- Consider P1(a, c) and P2(b,d) to be two points on a 2D plane 
-- where (a,b) are the respective minimum and maximum values of Northern Latitude (LAT_N) 
-- and (c,d) are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.
-- Query the Euclidean Distance between points P1 and P2 
-- and format your answer to display  decimal digits. 
-- Euclidean Distance = sqrt((x2-x1)² + (y2-y1)²)
-- a minimum LAT_N
-- b maximum LAT_N
-- c minimum LONG_W 
-- d maximum LONG_W
SELECT
  ROUND(
    SQRT(
      (MIN(LAT_N) - MAX(LAT_N)) * (MIN(LAT_N) - MAX(LAT_N)) + (MAX(LONG_W) - MIN(LONG_W)) * (MAX(LONG_W) - MIN(LONG_W))
    ),
    4
  )
FROM
  STATION;



/******************************************************************************
24 10 2023
 ******************************************************************************/


-- Generate the following two result sets:
-- Query an alphabetically ordered list of all names in OCCUPATIONS, 
-- immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). 
-- For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- Query the number of ocurrences of each occupation in OCCUPATIONS. 
-- Sort the occurrences in ascending order, and output them in the following format:
-- There are a total of [occupation_count] [occupation]s.
SELECT
  concat (Name, "(", LEFT (Occupation, 1), ")")
FROM
  occupations
ORDER BY
  name;

SELECT
  concat (
    "There are a total of ",
    COUNT(Occupation),
    " ",
    LOWER(Occupation),
    "s."
  )
FROM
  occupations
GROUP BY
  Occupation
ORDER BY
  COUNT(Occupation);

-- https://www.hackerrank.com/challenges/the-report/problem
-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. 
-- Ketty doesn't want the NAMES of those students who received a grade lower than 8. 
-- The report must be in descending order by grade 
-- i.e. higher grades are entered first. 
-- If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. 
-- Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. 
-- If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
SELECT
  CASE
    WHEN Grades.grade < 8 THEN NULL
    WHEN Grades.grade >= 8 THEN Students.name
  END,
  Grades.grade,
  Students.marks
FROM
  Students
  INNER JOIN Grades ON Students.marks BETWEEN Grades.min_mark AND Grades.max_mark
ORDER BY
  Grades.grade DESC,
  Students.name ASC,
  Students.Marks ASC;


/******************************************************************************
25 10 2023
******************************************************************************/

-- https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true
-- Les 2 fonctionnent
SELECT N,
  CASE
    WHEN P is NULL THEN "Root"                                     
    WHEN (SELECT COUNT(*) FROM BST WHERE Zoubida.N=P)>0 THEN "Inner"        
    ELSE "Leaf"       
  END 
FROM BST as Zoubida
ORDER BY N;

-- SELECT N,
--   CASE
--     WHEN P is NULL THEN "Root"                                     
--     WHEN Zoubida.N in (select P from BST) THEN "Inner"        
--     ELSE "Leaf"       
--   END 
-- FROM BST as Zoubida
-- ORDER BY N;


-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true
-- print hacker_id and name of hackers 
-- who achieved full scores for more than one challenge. 
-- Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
-- If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.