from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import relationship, backref, declarative_base
from sqlalchemy.orm import sessionmaker

import os

package_dir = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[0:-1])
db_dir = os.path.join(package_dir, 'project.db')
SQLITE_URL = ''.join(['sqlite:///', db_dir])

Base = declarative_base()
engine = create_engine(SQLITE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Manager(Base):
    __tablename__ = 'managers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    projects = relationship("Project", back_populates = "manager")

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
    projects = relationship("Project", back_populates = "employee")

    def __repr__(self):
        return f"Employee_Id {self.id}: " \
            + f"Employee name {self.name}, " \
            + f"Email {self.email}, " \
            + f"Phone Number {self.phone_number}, " \
            + f"Position {self.position}"


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    manager_id = Column(Integer(), ForeignKey('managers.id'))
    employee_id = Column(Integer(), ForeignKey('employees.id'))
    manager = relationship("Manager", back_populates="projects")
    employee = relationship("Employee", back_populates="projects")

    def __repr__(self):
        return f"Project_Id {self.id}: " \
            + f"Project name {self.name}, " \
            + f"Description name {self.description}, " \
            + f"Manager Name {self.manager_id}, " \
            + f"Employee Name {self.employee_id}"
    
Base.metadata.create_all(engine)




