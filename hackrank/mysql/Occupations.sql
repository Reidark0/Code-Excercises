--Pivot the Occupation column in OCCUPATIONS so that each Name is sorted 
--alphabetically and displayed underneath its corresponding Occupation. 
--The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

--Note: Print NULL when there are no more names corresponding to an occupation.

"SET @d=0, @a=0, @p=0, @s=0;
SELECT MIN(Doctor),MIN(Professor),MIN(SINGER),MIN(Actor)
FROM
(SELECT IF(OCCUPATION='Actor',NAME,NULL) AS Actor,
        IF(OCCUPATION='Doctor',NAME,NULL) AS Doctor,
        IF(OCCUPATION='Professor',NAME,NULL) AS Professor,
        IF(OCCUPATION='Singer',NAME,NULL) AS SINGER,
 CASE OCCUPATION
    WHEN 'Actor' THEN @a:=@a+1
    WHEN 'Doctor' THEN @d:=@d+1
    WHEN 'Professor' THEN @p:=@p+1
    WHEN 'Singer' THEN @s:=@s+1
 END
AS idn FROM OCCUPATIONS ORDER BY NAME )
AS temp GROUP BY temp.idn;"

