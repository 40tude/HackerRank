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

-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
select  (count(CITY)- count(distinct CITY)) from STATION; 

-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
select CITY from STATION where (LOWER(CITY) like "a%") OR (LOWER(CITY) like "e%") OR (LOWER(CITY) like "i%") or (LOWER(CITY) like "o%") or (LOWER(CITY) like "u%");
select CITY from STATION where (CITY like "a%") OR (CITY like "e%") OR (CITY like "i%") or (CITY like "o%") or (CITY like "u%");




-- 17 10
-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
select DISTINCT CITY from STATION where (CITY like "%a") OR (CITY like "%e") OR (CITY like "%i") OR (CITY like "%o") OR (CITY like "%u");

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. 
-- Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE ((CITY like "%a") OR (CITY like "%e") OR (CITY like "%i") OR (CITY like "%o") OR (CITY like "%u"))
AND ((CITY like "a%") OR (CITY like "e%") OR (CITY like "i%") OR (CITY like "o%") OR (CITY like "u%"));

-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (CITY NOT LIKE "a%") AND (CITY NOT LIKE "e%") AND (CITY NOT LIKE "i%") AND (CITY NOT LIKE "o%") AND (CITY NOT LIKE "u%");

-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (CITY NOT LIKE "%a") AND (CITY NOT LIKE "%e") AND (CITY NOT LIKE "%i") AND (CITY NOT LIKE "%o") AND (CITY NOT LIKE "%u");

-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (
  ((CITY NOT LIKE "%a") AND (CITY NOT LIKE "%e") AND (CITY NOT LIKE "%i") AND (CITY NOT LIKE "%o") AND (CITY NOT LIKE "%u"))
  OR
  ((CITY NOT LIKE "a%") AND (CITY NOT LIKE "e%") AND (CITY NOT LIKE "i%") AND (CITY NOT LIKE "o%") AND (CITY NOT LIKE "u%"))
);

-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (
  ((CITY NOT LIKE "%a") AND (CITY NOT LIKE "%e") AND (CITY NOT LIKE "%i") AND (CITY NOT LIKE "%o") AND (CITY NOT LIKE "%u"))
  AND
  ((CITY NOT LIKE "a%") AND (CITY NOT LIKE "e%") AND (CITY NOT LIKE "i%") AND (CITY NOT LIKE "o%") AND (CITY NOT LIKE "u%"))
);


-- Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in alphabetical order.
SELECT name
FROM Employee
    ORDER BY name ASC
;

-- Write a query that prints a list of employee names (i.e.: the name attribute) 
-- for employees in Employee having a salary greater than 2000 per month 
-- who have been employees for less than 10 months. 
-- Sort your result by ascending employee_id.
SELECT name
FROM Employee
  WHERE ((salary>2000) AND (months<10))
  ORDER BY employee_id ASC
;


-- Query the Name of any student in STUDENTS 
-- who scored higher than 75 Marks. 
-- Order your output by the last three characters of each name. 
-- If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), 
-- secondary sort them by ascending ID.
SELECT Name 
FROM Students
WHERE (Marks>75)
ORDER BY 
  SUBSTR(Name, -3, 3) ASC, -- Should work with MySQL and SQLite. MySQL accepts SUBSTR(Name, -3) 
  Id ASC
;  


-- MARCHE PAS !!!!!!!!!!!!!!!
-- https://www.hackerrank.com/challenges/weather-observation-station-5/problem?isFullScreen=true
-- Query the two cities in STATION with 
-- the shortest and longest CITY names, 
-- as well as their respective lengths (i.e.: number of characters in the name). 
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
SELECT MAX(LENGTH(CITY)), LENGTH(CITY)
FROM Stations
WHERE (LENGTH(CITY)= OR (LENGTH(CITY)=MIN(LENGTH(CITY))
ORDER by CITY ASC
;


