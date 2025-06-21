-- https://www.codewars.com/kata/sql-basics-top-10-customers-by-total-payments-amount

SELECT customer.customer_id, customer.email, COUNT(payment.payment_id) AS payments_count, SUM(payment.amount)::float8 AS total_amount
FROM customer, payment
WHERE customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY SUM(payment.amount) DESC
LIMIT 10