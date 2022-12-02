-- group scores by the number of times its repeated
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY 1 ORDER BY number DESC;
