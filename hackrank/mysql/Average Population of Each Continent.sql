--Given the CITY and COUNTRY tables, query the names of all 
--the continents (COUNTRY.Continent) and their respective average 
--city populations (CITY.Population) rounded down to the nearest integer.


SELECT country.continent, city.population
FROM country
LEFT JOIN city ON country.code = city.countrycode
ORDER BY continent

SELECT SUM(city.population)
FROM CITY 
WHERE population IN (
    SELECT city.population
    FROM city
    JOIN country ON country.code = city.countrycode)