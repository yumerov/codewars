-- https://www.codewars.com/kata/sql-basics-simple-exists/train/sql

SELECT *
FROM departments AS p
WHERE EXISTS (SELECT 1 FROM sales AS s WHERE s.department_id = p.id AND s.price >= 98)