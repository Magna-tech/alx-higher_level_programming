-- Average temperatures per city
SELECT city, AVG(value) AS temp
FROM temperatures
GROUP BY city
ORDER BY temp DESC;
