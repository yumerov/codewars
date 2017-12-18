SELECT p.id AS `id`, p.name AS `name`, p.isbn AS `isbn`, p.price AS `price`, c.id AS `company_id`, c.name AS `company_name`
FROM products AS p
INNER JOIN companies AS c
    ON p.company_id = c.id