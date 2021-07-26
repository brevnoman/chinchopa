from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, Text, Float
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine('sqlite:///hr.db', echo=True)
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)


class Employees(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(25))
    email = Column(String(25))
    phone_number = Column(String(25))
    hire_date = Column(Date)
    job_id = Column(String(10))
    salary = Column(Numeric)
    commission_pct = Column(Integer)
    manager_id = Column(Integer)
    department_id = Column(Integer)

    def __repr__(self):
        return f"ID: {self.employee_id}, First name: {self.first_name}, Last name: {self.last_name}, Email: {self.email}, " \
               f"Phone Number: {self.phone_number}, Hire Date: {self.hire_date}, Job_id: {self.job_id}, Salary: {self.salary}," \
               f"Commission PCT: {self.commission_pct}, Manager ID: {self.manager_id}, Department ID: {self.department_id}"


class Jobs(Base):
    __tablename__ = 'jobs'
    job_id = Column(String(10), primary_key=True)
    job_title = Column(String(25))
    min_salary = Column(Numeric(precision=2, scale=2))
    max_salary = Column(Numeric(precision=2, scale=2))
    # employees = relationship("Employees", back_populates='job')


class CompanyView(Base):
    __tablename__ = 'COMPANY_VIEW'
    job_id = Column(String(10), primary_key=True)
    min_sal = Column()



class EmployeeIncome(Base):
    __tablename__ = "EMPLOYEE_INCOME"
    empid = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(Integer)


class Esercici01(Base):
    __tablename__ = "ESERCICIO1"
    c = Column(Text, primary_key=True)
    d = Column(Text)


class Emor(Base):
    __tablename__ = "Emor"
    id = Column(Integer, primary_key=True)
    name = Column(Text)


class MinSalary(Base):
    __tablename__ = "MIN_SALARY"
    job_id = Column(Text, primary_key=True)
    min_salary = Column(String)


class Student(Base):
    __tablename__ = "STUDENT"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    age = Column(Integer)
    address = Column(String)
    fees = Column(Float)


class Countries(Base):
    __tablename__ = "countries"
    country_id = Column(String(2), primary_key=True)
    country_name = Column(String(40))
    region_id = Column(Integer)


class Department(Base):
    __tablename__ = "department"
    department_id = Column(Text, primary_key=True)
    department_name = Column(Text)
    manager_id = Column(Text)
    location_id = Column(Text)


class Departments(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String)
    manager_id = Column(Integer)
    location_id = Column(Integer)


class Details(Base):
    __tablename__ = "details"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    turn = Column(Integer)


class EmployeeData(Base):
    __tablename__ = "employee_data"
    employee_name = Column(Text)
    item = Column(Text)
    rate = Column(Float)
    quantity = Column(Integer)
    date = Column(Text)
    id = Column(Integer, primary_key=True)


class JobHistory(Base):
    __tablename__ = "job_history"
    employye_id = Column(Integer)
    start_date = Column(Date)
    end_date = Column(Date)
    job_id = Column(String(10), primary_key=True)
    department_id = Column(Integer)


class Locations(Base):
    __tablename__ = "locations"
    location_id = Column(Integer, primary_key=True)
    street_address = Column(String(25))
    postal_code = Column(String(12))
    city = Column(String(30))
    state_province = Column(String(12))
    country_id = Column(String(2))


class Orders(Base):
    __tablename__ = "orders"
    odr_no = Column(Integer, primary_key=True)
    item_id = Column(Integer)
    item_name = Column(Text(20))
    ord_qty = Column(Integer)
    cost =Column(Integer)


class ProdBackup(Base):
    __tablename__ = "prod_backup"
    prod_id = Column(Integer, primary_key=True)
    prod_name = Column(Text(20))
    prod_rate = Column(Integer)
    prod_qc = Column(Text(10))


class ProdMast(Base):
    __tablename__ = "prod_mast"
    prod_id = Column(Integer, primary_key=True)
    prod_name = Column(Text(20))
    prod_rate = Column(Integer)
    prod_qc = Column(Text(20))


class R(Base):
    __tablename__ = "r"
    a = Column(Integer, primary_key=True)
    b = Column(Integer)


class Regions(Base):
    __tablename__ = "regions"
    region_id = Column(Integer, primary_key=True)
    region_name = Column(String(25))


class S(Base):
    __tablename__ = "s"
    a = Column(Integer, primary_key=True)
    d = Column(Integer)
    e = Column(Integer)


class Tags(Base):
    __tablename__ = "tags"
    title = Column(Text, primary_key=True)
    description = Column(Text)
    created = Column(Text)


class Tb1(Base):
    __tablename__ = "tb1"
    c1 = Column(Integer, primary_key=True)
    c2 = Column(String(5))
    c3 = Column(Float)


class Users(Base):
    __tablename__ = "users"
    name = Column(String(128))
    email = Column(String(128), primary_key=True)


class ViewMinSal(Base):
    __tablename__ = "view_min_sal"
    job_id = Column(String(10), primary_key=True)
    min_sal = Column()

