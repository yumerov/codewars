-- https://www.codewars.com/kata/sql-bug-fixing-fix-the-query-totaling/train/sql

SELECT
  cast(s.transaction_date as date) as day,
  d.name as department,
  COUNT(s.id) as sale_count
  FROM department AS d
    JOIN sale AS s on d.id = s.department_id
  group by day, d.name
  order by day