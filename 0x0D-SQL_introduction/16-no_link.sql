-- list all records except rows with no names
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
