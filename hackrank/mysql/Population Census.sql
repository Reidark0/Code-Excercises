--Given the CITY and COUNTRY tables, query the sum of the populations 
--of all cities where the CONTINENT is 'Asia'.


SELECT SUM(city.population)
FROM CITY 
WHERE population IN (
    SELECT city.population
    FROM city
    JOIN country ON country.code = city.countrycode
    WHERE country.continent = 'asia')