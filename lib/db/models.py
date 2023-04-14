from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///project.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Manager(Base):

    __tablename__ = 'managers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    employee = relationship("Employee", backref="employees")

    def __repr__(self):
        return f"Manager {self.id}: " \
            + f"Manager name {self.name}, " \
            + f"Email {self.email}"
    


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())
    position = Column(String())
    manager_id = Column(Integer(), ForeignKey('managers.id'))

    def __repr__(self):
        return f"Employee_Id {self.id}: " \
            + f"Employee name {self.name}, " \
            + f"Email {self.email}, " \
            + f"Phone Number {self.phone_number}, " \
            + f"Position {self.position}, " \
            + f"Manager {self.manager_id}" 


# class Project(Base):
#     __tablename__ = 'projects'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     description = Column(String())
#     manager_id = Column(Integer(), ForeignKey('managers.id'))
#     employee_id = Column(Integer(), ForeignKey('employees.id'))

#     def __repr__(self):
#         return f"Project_Id {self.id}: " \
#             + f"Project name {self.name}, " \
#             + f"Description name {self.description}, " \
#             + f"Manager Name {self.manager_id}, " \
#             + f"Employee Name {self.employee_id}"




# lib/sqlalchemy_sandbox.py


# from datetime import datetime

# from sqlalchemy import (create_engine, desc,
#     Index, Column, DateTime, Integer, String)
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

# class Student(Base):
#     __tablename__ = 'students'

#     Index('index_name', 'name')

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())
#     email = Column(String(55))
#     grade = Column(Integer())
#     birthday = Column(DateTime())
#     enrolled_date = Column(DateTime(), default=datetime.now())

#     def __repr__(self):
#         return f"Student {self.id}: " \
#             + f"{self.name}, " \
#             + f"Grade {self.grade}"

# if __name__ == '__main__':

#     engine = create_engine('sqlite:///:memory:')
#     Base.metadata.create_all(engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     albert_einstein = Student(
#         student_name="Albert Einstein",
#         student_email="albert.einstein@zurich.edu",
#         student_grade=6,
#         student_birthday=datetime(
#             year=1879,
#             month=3,
#             day=14
#         ),
#     )

#     alan_turing = Student(
#         student_name="Alan Turing",
#         student_email="alan.turing@sherborne.edu",
#         student_grade=11,
#         student_birthday=datetime(
#             year=1912,
#             month=6,
#             day=23
#         ),
#     )

#     session.bulk_save_objects([albert_einstein, alan_turing])
#     session.commit()