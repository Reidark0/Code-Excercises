--A median is defined as a number separating the higher half of a data set from the lower half. 
--Query the median of the Northern Latitudes (LAT_N) from STATION and 
--round your answer to 4 decimal places.

'COUNT(*)
FROM station'

SELECT FORMAT(MAX(lat_n),4)
FROM (
    SELECT lat_n
    FROM station
    ORDER BY lat_n ASC
    LIMIT 250) a
