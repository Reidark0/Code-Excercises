-- Given the CITY and COUNTRY tables, query the names 
-- of all cities where the CONTINENT is 'Africa'.


SELECT name
FROM city
WHERE city.countrycode IN (
    SELECT city.countrycode
    FROM city
    JOIN country ON city.countrycode = country.code
    WHERE country.continent = 'AFRICA')