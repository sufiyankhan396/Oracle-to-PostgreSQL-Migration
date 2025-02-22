SPOOL employee_data.csv;
SET HEADING OFF
SET FEEDBACK OFF
SELECT emp_id || ',' || name || ',' || salary || ',' || TO_CHAR(hire_date, 'YYYY-MM-DD')
FROM employees;
SPOOL OFF;