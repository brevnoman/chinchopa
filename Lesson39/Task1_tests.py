from sqlalchemy.exc import IntegrityError

from Task1 import *
from datetime import date
import unittest
session = Session()
hire_date = date(2007, 12, 17)

class Tests(unittest.TestCase):

    def test_adding_new_employee(self):
        jora = Employees(employee_id=1337,
                          first_name='Jora',
                          last_name='Mamkin',
                          email='JoRiK@gmail.com',
                          phone_number='+380951488228',
                          hire_date=hire_date,
                          job_id="IT_PROG",
                          salary=40,
                          commission_pct=0,
                          manager_id=100,
                          department_id=90)
        try:
            session.add(jora)
            session.commit()
        except IntegrityError:
            session.rollback()
        self.assertEqual(str(session.query(Employees).filter(Employees.last_name=="Mamkin").one()), "ID: 1337, First name: Jora, Last name: Mamkin, Email: JoRiK@gmail.com, Phone Number: +380951488228, Hire Date: 2007-12-17, Job_id: IT_PROG, Salary: 40.0000000000,Commission PCT: 0, Manager ID: 100, Department ID: 90")
        print(type(session.query(Employees).filter(Employees.last_name=="Mamkin").one()))