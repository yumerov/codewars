-- https://www.codewars.com/kata/even-or-odd/train/sql

SELECT
    (CASE WHEN number % 2 THEN "Odd"
        ELSE "Even" END) AS is_even
FROM numbers
