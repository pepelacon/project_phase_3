
from db.models import Base, Manager, Employee
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == '__main__':
    engine = create_engine('sqlite:///project.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    print('Welcome to my CLI!')
    
    def get_all(session):
        a= session.query(Employee).all()
        print(a)
        return a
    get_all(session)
    
    print('Thanks for using my CLI')
