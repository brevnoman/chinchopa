.open hr.db
--department
--departments
SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees, department WHERE employees.department_id=department.department_id;

SELECT employees.first_name, employees.last_name, department.department_name, locations.city, locations.state_province
FROM employees, department, locations WHERE employees.department_id=department.department_id AND department.location_id=locations.location_id;

SELECT employees.first_name, employees.last_name, employees.department_id, department.department_name
FROM employees, department WHERE employees.department_id=department.department_id and (employees.department_id=40 or employees.department_id=80);

SELECT department_name FROM department;

SELECT e.first_name, e.last_name, m.first_name, m.last_name FROM employees e, employees m WHERE e.manager_id=m.employee_id;

SELECT j.job_title, e.first_name, e.last_name, j.max_salary-e.salary from employees e, jobs j where e.job_id=j.job_id;

SELECT j.job_title, avg(e.salary) FROM jobs j, employees e where j.job_id=e.job_id group by j.job_title;

SELECT e.first_name, e.last_name, e.salary FROM employees e, department d, locations l where e.department_id=d.department_id and d.location_id=l.location_id and l.city="London";

SELECT d.department_name, count(e.first_name) from department d, employees e where d.department_id=e.department_id group by d.department_name;
