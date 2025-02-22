COPY employees(emp_id, name, salary, hire_date)
FROM '/path/to/employee_data.csv'
DELIMITER ','
CSV HEADER;