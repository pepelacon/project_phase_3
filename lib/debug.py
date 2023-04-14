from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Manager, Employee

if __name__ == '__main__':
    import ipdb;
    engine = create_engine('sqlite:///project.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    employee = session.query(Employee).all()
    print(employee)
    ipdb.set_trace()
    # employees = session.query(Manager).filter_by(manager_id=manager.id)

    # manager.employees
