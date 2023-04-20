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
    employees = relationship("Employee", back_populates = "manager")

    def __repr__(self):
        return f"Manager_ID: {self.id}, " \
            + f"Manager_name: {self.name}, " \
            + f"Email: {self.email}."


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone_number = Column(Integer())
    position = Column(String())
    manager_id = Column(Integer(), ForeignKey('managers.id'))
    project_id = Column(Integer(), ForeignKey('projects.id'))
    project = relationship("Project", back_populates = "employees")
    manager = relationship("Manager", back_populates = "employees")

    def __repr__(self):
        return f"Employee_ID: {self.id}, " \
            + f"Name: {self.name}, " \
            + f"Email: {self.email}, " \
            + f"Phone_Number: {self.phone_number}, " \
            + f"Position: {self.position}, "\
            + f"Manager_ID: {self.manager_id}, "\
            + f"Project_ID: {self.project_id}. "\
            


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    description = Column(String())
    manager_id = Column(Integer(), ForeignKey('managers.id'))
    manager = relationship("Manager", back_populates = "projects")
    employees = relationship("Employee", back_populates = "project")

    def __repr__(self):
        return f"Project_ID: {self.id}, " \
            + f"Project_Name: {self.name}, " \
            + f"Project_Description: {self.description}, " \
            + f"Manager_ID: {self.manager_id}." \
    
Base.metadata.create_all(engine)




