.open hr.db
SELECT first_name, last_name FROM employees;
SELECT DISTINCT department_id FROM employees;
SELECT * FROM employees ORDER BY first_name DESC;
SELECT first_name, last_name, salary, salary*0.12 FROM employees;
SELECT first_name, last_name, min(salary) FROM employees;
SELECT first_name, last_name, max(salary) FROM employees;
SELECT round(salary/12, 2) FROM employees;