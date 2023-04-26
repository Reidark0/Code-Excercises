--Generate the following two result sets:

--1 - Query an alphabetically ordered list of all names in OCCUPATIONS, 
--immediately followed by the first letter of each profession as a 
--parenthetical (i.e.: enclosed in parentheses). 
--For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
--2 - Query the number of ocurrences of each occupation in OCCUPATIONS. 
--Sort the occurrences in ascending order, and output them in the following format:

--There are a total of [occupation_count] [occupation]s.

--where [occupation_count] is the number of occurrences of an 
--occupation in OCCUPATIONS and [occupation] is the lowercase 
--occupation name. If more than one Occupation 
--has the same [occupation_count], 
--they should be ordered alphabetically.


-- Primeira tentativa
SELECT CONCAT(name, CONCAT ('(',LEFT(occupation, 1),')'))
FROM occupations
ORDER BY name;
SELECT CONCAT('There are a total of ', COUNT(occupation), ' doctors.')
from occupations
WHERE occupation = 'Doctor';
SELECT CONCAT('There are a total of ', COUNT(occupation), ' singers.')
from occupations
WHERE occupation = 'Singer';
SELECT CONCAT('There are a total of ', COUNT(occupation), ' actors.')
from occupations
WHERE occupation = 'Actor';
SELECT CONCAT('There are a total of ', COUNT(occupation), ' professors.')
from occupations
WHERE occupation = 'Professor'

-- Segunda Tentativa
SELECT CONCAT(name, CONCAT ('(',LEFT(occupation, 1),')'))
FROM occupations
ORDER BY name;
SELECT CONCAT('There are a total of ', COUNT(occupation), ' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(occupation) ASC, occupation ASC;