from Task1 import Employees, Base, Session, engine, Department, Jobs, Locations
import sqlalchemy


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    for first_name, last_name in session.query(Employees.first_name, Employees.last_name):  #1
        print(first_name, last_name)

    for department_id in session.query(Employees.department_id).distinct():            #2
        print(department_id)

    for everything in session.query(Employees).all():             #3
        print(everything)

    for first_name, last_name, salary, percent_of_salary12 in session.query(Employees.first_name, Employees.last_name, Employees.salary, Employees.salary*0.12):  #4
        print(first_name, last_name, salary, percent_of_salary12)

    print(session.query(Employees.first_name, Employees.last_name, Employees.salary).order_by(Employees.salary).first())  #5
    print(session.query(Employees.first_name, Employees.last_name, Employees.salary).order_by(Employees.salary.desc()).first())     #6
    for month_salary in session.query(Employees.salary/12).all():         #7
        print(month_salary)

    for department_name in session.query(Department.department_name).all():  #8
        print(department_name)

    for job_title, employee_first_name, employee_last_name, difference_between_max_and_current_salary, in session.query(Jobs.job_title, Employees.first_name, Employees.last_name, Jobs.max_salary-Employees.salary).filter(Jobs.job_id == Employees.job_id).all():    #9
        print(job_title,employee_first_name,employee_last_name,difference_between_max_and_current_salary)

    for employee_first_name, employee_last_name, employee_salary in session.query(Employees.first_name, Employees.last_name, Employees.salary).filter(Employees.department_id== Department.department_id).filter(Department.location_id == Locations.location_id).filter(Locations.city == "London").all():         #10
        print(employee_first_name, employee_last_name, employee_salary)
