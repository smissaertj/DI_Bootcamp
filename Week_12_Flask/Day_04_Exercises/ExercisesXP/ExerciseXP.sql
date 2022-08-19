-- Database: public

DROP DATABASE IF EXISTS public;

	
CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(50) NOT NULL,
	item_price INTEGER NOT NULL);
	
CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL)

INSERT INTO items (item_name, item_price) VALUES ('Small Desk', 100);
INSERT INTO items (item_name, item_price) VALUES ('Large Desk', 300);
INSERT INTO items (item_name, item_price) VALUES ('Fan', 80);

	
	
INSERT INTO customers (first_name, last_name) VALUES ('Greg', 'Jones');
INSERT INTO customers (first_name, last_name) VALUES ('Sandra', 'Jones');
INSERT INTO customers (first_name, last_name) VALUES ('Scott', 'Scott');
INSERT INTO customers (first_name, last_name) VALUES ('Trevor', 'Green');
INSERT INTO customers (first_name, last_name) VALUES ('Melanie', 'Johnson');

SELECT * FROM items;
SELECT * FROM items WHERE item_price > 80;
SELECT * FROM items WHERE item_price <= 300;

SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE last_name != 'Scott';