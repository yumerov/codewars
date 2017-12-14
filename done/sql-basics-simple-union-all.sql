-- https://www.codewars.com/kata/sql-basics-simple-union-all/train/sql

SELECT us.*, 'US' AS LOCATION FROM ussales AS us WHERE us.price >= 50
UNION ALL
SELECT eu.*, 'EU' AS LOCATION FROM eusales AS eu WHERE eu.price >= 50