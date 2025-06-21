-- https://www.codewars.com/kata/sql-bug-fixing-fix-the-join/train/sql

SELECT
  j.job_title,
  round(SUM(j.salary)::numeric / COUNT(p), 2)::float8 as average_salary,
  COUNT(p.id) as total_people,
  round(SUM(j.salary)::numeric, 2)::float8 as total_salary
  FROM people AS p
    JOIN job AS j ON (p.id = j.people_id)
  GROUP BY j.job_title
  ORDER BY average_salary desc