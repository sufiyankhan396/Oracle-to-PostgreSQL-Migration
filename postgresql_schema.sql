CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    hire_date DATE
);