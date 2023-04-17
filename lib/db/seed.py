from faker import Faker
from models import (Base, Manager)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

faker = Faker()


# if __name__ == '__main__':
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
