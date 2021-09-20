# Python -Technical Question

- [Question 1](#question-1)
- [Question 2](#question-2)

## Question 1
 
First create the table useing the below SQL.

Then find the sales who made the most sales amount for the year 2020, the result should include two columns sales_id, total_amount
 

```
CREATE TABLE sales (
  id INT,
  amount INT,
  sales_id VARCHAR(30),
  sales_date DATE
);
INSERT INTO sales VALUES (1, 150, 'Andy', '2020-01-01');
INSERT INTO sales VALUES (2, 210, 'John', '2020-01-02');
INSERT INTO sales VALUES (3, 140, 'Mike', '2020-01-03');
INSERT INTO sales VALUES (4, 70, 'Andy', '2020-01-04');
INSERT INTO sales VALUES (5, 10, 'John', '2020-01-05');
INSERT INTO sales VALUES (6, 150, 'Andy', '2021-01-01');
INSERT INTO sales VALUES (7, 100, 'Tom', '2020-01-03');
```

## Question 2

First create the table useing the below SQL.

Please use PostgresSQL v10.0
We have a table with duplicated rows, for example, there are two records with id 1, and we need to only pick one of them.
 The rule is, the latest row (based on the load_datetime) is the valid record.
 Please write SELECT query to do the de-dup, and return valid unique rows only
 

```
CREATE TABLE customer_sales (
  id INT,
  amount INT,
  customer_id VARCHAR(30),
  load_datetime TIMESTAMP
);
INSERT INTO customer_sales VALUES (1, 200, 'Mike', '2020-01-01 01:00:00');
INSERT INTO customer_sales VALUES (2, 299, 'John', '2020-01-02 01:00:00');
INSERT INTO customer_sales VALUES (1, 201, 'Mike', '2020-01-01 01:13:00');
INSERT INTO customer_sales VALUES (3, 70, 'Andy', '2020-01-01 01:13:00');
```
