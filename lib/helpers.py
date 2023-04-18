from db.models import Base, Manager, Employee, Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
import sys

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


###sign in
@click.command()
@click.option('--id', prompt='Enter  Manager id', help='manager name')
def select_manager(id):
    user_manager = session.query(Manager).filter(Manager.id == id).first()
    click.echo(f"Hello {user_manager.name} ")
    manager_menu(id)

def manager_menu(id):
    options = {
            '1': show_all_manager_projects,
            '2': add_project,
            '3': show_all_manager_employees,
            '4': add_employee
        }
    print("Choose an option:")
    print("1. do you want to see your projects?")
    print("2. do you want to add a new project?")
    print("3. do you want to see your employees?")
    print("4. do you want to add a new employee?")
    choice = input("Enter your choice (1, 2,3): ")

    if choice == '1' :
        options[choice](session,id)
    elif  choice == '2':
        add_project()
    elif  choice == '3':
        options[choice](session,id)
    elif  choice == '4':
        add_employee()
    else:
        print("Invalid choice.")
        sys.exit(1)

def sign_in():
    show_all_managers(session)
    select_manager()

def sign_up():
    add_manager()

### Create New ####
@click.command()
@click.option('--name', prompt='Enter New Manager name', help='manager name')
@click.option('--email', prompt = 'Enter Email', help = 'manager email')
def add_manager(name, email):
    """Simple program that greets NAME for a total of COUNT times."""
    manager = Manager(name = name , email = email)
    session.add(manager)
    session.commit()
    click.echo(f"Hello {name} : your id is  {manager.id}!")
    manager_menu(manager.id)
    
    
@click.command()
@click.option('--name', prompt='Enter New Employee name', help='employee name')
@click.option('--email', prompt = 'Enter Email', help = 'employee email')
@click.option('--phone_number', prompt = 'Enter phone_number', help = 'employee phone_number')
@click.option('--position', prompt = 'Enter position', help = 'employee position')
@click.option('--manager_id', prompt = 'Enter manager_id', help = 'employee manager_id')
@click.option('--project_id', prompt = 'Enter project_id', help = 'employee project_id')
def add_employee(name, email,phone_number,position,manager_id,project_id):
    """Simple program that greets NAME for a total of COUNT times."""
    employee = Employee(name = name , email = email, phone_number = phone_number, position=position,manager_id=manager_id,project_id=project_id)
    session.add(employee)
    session.commit()
    click.echo(f"Hello {name} -  {email}!")


@click.command()
@click.option('--name', prompt='Enter New project name', help='project name')
@click.option('--description', prompt = 'Enter description', help = 'project description')
@click.option('--manager_id', prompt = 'Enter manager_id', help = 'project manager_id')
def add_project(name, description,manager_id):
    """Simple program that greets NAME for a total of COUNT times."""
    project = Project(name = name , description = description, manager_id=manager_id)
    session.add(project)
    session.commit()
    click.echo(f"Created project: {name} , Description  {description} - {manager_id}!")
    manager_menu(manager_id)

#### edit / update ###



### queries ####
def show_all_managers(session):
    #### BUILD TABLE FORMATTING
    all_managers = session.query(Manager).all()
    print(all_managers)


def show_all_manager_projects(session,id):
    #### BUILD TABLE FORMATTING
    all_manager_project = session.query(Project).filter(Project.manager_id == id).all()
    print(all_manager_project)

def show_all_manager_employees(session,id):
    #### BUILD TABLE FORMATTING
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == id).all()
    print(all_manager_employee)



#### DELETE ###    
@click.command()
@click.option('--id', prompt='Enter New Employee id', help='employee name')  
def delete_employee(id):
    query = session.query(Employee).filter(Employee.id == id)
    query.delete()
    session.commit()


