from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Base, Manager, Employee

if __name__ == '__main__':
    import ipdb;
    engine = create_engine('sqlite:////Users/daniel/Development/code/phase-3/project/project_phase_3/lib/db/project.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()


    employee = session.query(Employee)
    
    ipdb.set_trace()
   

 
