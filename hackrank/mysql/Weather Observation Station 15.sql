--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) 
--in STATION that is less than 137.2345 Round your answer to 4 decimal places.


SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n IN (
    SELECT MAX(lat_n)
    FROM station
    WHERE lat_n < 137.2345)