from faker import Faker
from models import (Base, Manager, Employee)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

faker = Faker()


if __name__ == '__main__':
    engine = create_engine('sqlite:///project.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Manager).delete()
    for i in range(10):
        manager = Manager(
            name = faker.name(),
            email = faker.email()
        )

        print(manager)
        session.add(manager)
        session.commit()

    position = ["Jr. Dev", "Sr. Dev", "UX Specialist"]

    session.query(Employee).delete()
    for i in range(10):
        employee = Employee(
            name = faker.name(),
            email = faker.email(),
            phone_number = random.randint(1000000000, 9999999999),
            position = random.choice(position)
        )

        print(employee)
        session.add(employee)
        session.commit()

        
    session.query(Employee).delete()
    for i in range(10):
        employee = Employee(
            name = faker.name(),
            email = faker.email(),
            phone_number = random.randint(1000000000, 9999999999),
            position = random.choice(position)
        )

        print(employee)
        session.add(employee)
        session.commit()
    

