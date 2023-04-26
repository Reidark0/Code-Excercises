--Samantha was tasked with calculating the average monthly salaries for all employees in the 
--EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing 
--the calculation. She wants your help finding the difference between her miscalculation 
--(using salaries with any zeros removed), and the actual average salary.


SELECT ROUND(AVG(salary)) - ROUND(AVG(REPLACE(salary, 0, '')))
FROM employees