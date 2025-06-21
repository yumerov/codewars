-- https://www.codewars.com/kata/sql-basics-simple-join-and-rank

SELECT p.*, count(s.sale) AS sale_count, sum(s.price) AS sale_rank
FROM people AS p, sales AS s
WHERE p.id = s.people_id
GROUP BY p.id
ORDER BY sum(s.price)