from models import (Base, Manager, Employee, Project)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
import random
from faker import Faker
faker = Faker()

package_dir = '/'.join(os.path.abspath(os.path.dirname(__file__)).split('/')[0:-1])
db_dir = os.path.join(package_dir, 'project.db')
SQLITE_URL = ''.join(['sqlite:///', db_dir])


if __name__ == '__main__':
    engine = create_engine(SQLITE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()


############ * MANAGER * #############

    session.query(Manager).delete()
    for i in range(10):
        manager = Manager(
            name = faker.name(),
            email = faker.email()
        )

        print(manager)
        session.add(manager)



############ * EMPLOYEE * #############


    position = ["Jr. Dev", "Sr. Dev", "UX Specialist"]

    session.query(Employee).delete()
    for i in range(10):
        employee = Employee(
            name = faker.name(),
            email = faker.email(),
            phone_number = random.randint(1000000000, 9999999999),
            position = random.choice(position),
            manager_id = random.randint(1, 10),
            project_id = random.randint(1, 10)
        )

        print(employee)
        session.add(employee)

    
############ * PROJECTS * #############

    projects = ["Samsung", "Project_2", "Project_3", "Project_4", "Project_5", "Project_6"]
    
    session.query(Project).delete()
    for i in range(10):
        project = Project(
            name = random.choice(projects),
            description = faker.sentence(nb_words=10, variable_nb_words=False),
            manager_id = random.randint(1, 10),
        )

        print(project)
        session.add(project)



    session.commit()
