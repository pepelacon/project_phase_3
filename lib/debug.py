from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Manager, Employee

if __name__ == '__main__':
    import ipdb;
    engine = create_engine('sqlite:///project.db')
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    employee = session.query(Employee)
    
    ipdb.set_trace()

