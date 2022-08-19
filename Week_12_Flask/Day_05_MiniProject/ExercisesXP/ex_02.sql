SELECT * FROM customer;
SELECT first_name, last_name FROM customer AS full_name;
SELECT DISTINCT create_date FROM customer;
SELECT * FROM customer ORDER BY first_name DESC;
SELECT film_id, title, description, release_year, rental_rate FROM film;
SELECT address, phone FROM address WHERE district = 'Texas';
SELECT * FROM film where film_id = 15 or film_id = 50;
SELECT film_id, title, description, rental_rate FROM film WHERE title ILIKE '%Freddy Storm%';
SELECT film_id, title, description, rental_rate FROM film WHERE title ILIKE 'Mi%';
SELECT title, rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
SELECT title, rental_rate FROM film ORDER BY rental_rate ASC OFFSET 10 LIMIT 10;
SELECT amount, payment_date FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id ORDER BY customer.customer_id ASC;
SELECT * FROM film LEFT JOIN inventory ON film.film_id = inventory.film_id WHERE inventory.film_id IS NULL;
SELECT DISTINCT city.city, country.country FROM city LEFT JOIN country ON city.country_id = country.country_id ORDER BY country.country ASC;
SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
    FROM customer INNER JOIN payment
    ON payment.customer_id = customer.customer_id
    WHERE payment.staff_id = 1
    ORDER BY payment.staff_id ASC;