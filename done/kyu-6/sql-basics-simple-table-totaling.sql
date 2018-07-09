--https://www.codewars.com/kata/sql-basics-simple-table-totaling/train/sql

select
  row_number() OVER(order by sum(points) desc) as rank,
  (case when (clan = '') is not false then '[no clan specified]' else clan end) as clan,
  sum(points) as total_points,
  count(1) as total_people
from people
group by clan
order by total_points desc