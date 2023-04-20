from db.models import Base, Manager, Employee, Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettytable import PrettyTable


import click
import sys

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


###sign in
@click.command()
@click.option('--id', prompt='Enter your account ID', help='manager name')
def select_manager(id):
    user_manager = session.query(Manager).filter(Manager.id == id).first()
    print("********************************")
    click.echo(f"Hello {user_manager.name} ")
    print("********************************")

    manager_menu(id)

def manager_menu(id):
   
    print("Choose an option:")
    print("---------------------------")
    print("| 1 | See your projects?  |")
    print("| 2 | Add a new project?  |")
    print("| 3 | See your employees? |")
    print("| 4 | Add a new employee? |")
    print("| 5 | Delete an employee? |")
    print("| 6 | Delete a manager?   |")
    print("| 7 | Update a project?   |")
    print("---------------------------")
    
    choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7): ")

    if choice == '1' :
        show_all_manager_projects(session,id)
    elif  choice == '2':
        add_project(id)
    elif  choice == '3':
        show_all_manager_employees(session,id)
    elif  choice == '4':
        add_employee()
    elif  choice == '5':
        delete_employee()
    elif  choice == '6':
        delete_manager()
    elif  choice == '7':
        update_project()
    
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




############## ! ADD PROJECT ---------------


def add_project(manager_id):
    name = input("Enter New project name: ")
    description = input("Enter description: ")
    project = Project(name = name , description = description, manager_id = manager_id)
    session.add(project)
    session.commit()
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == manager_id).all()
    print("Your employee: ")
    [print(f'ID: {emp.id} | Employee name: {emp.name}') for emp in all_manager_employee]
    chosen_employee = int(input("Enter employee ID for project: "))
    employee_for_this_project =  session.query(Employee).filter(Employee.id == chosen_employee).first()
    employee_for_this_project.project_id = project.id
    employee_for_this_project.manager_id = manager_id
    session.add(employee_for_this_project)
    session.commit()
    click.echo(f"Created project: {name} , Description  {description} - {manager_id}!")
    manager_menu(manager_id)




############ edit / update #################

@click.command()
@click.option('--project_id', prompt='Enter project id of project to edit', help='project name')
@click.option('--manager_id', prompt = 'Enter your manager id', help = 'project description')
def update_project(manager_id, project_id):
    projects = session.query(Project).filter((Project.manager_id == manager_id ) | (Project.manager_id == None)).all()
    employees = session.query(Employee).filter(Employee.project_id == project_id ).all()
    if int(project_id) in [project.id for project in projects]:
        project = session.query(Project).filter( Project.id == project_id).first()
        choice = input('Do you want to change the project name: y/n?')
        if choice == 'y' :
            proj_input = input('Enter new project name: ')
            project.name= proj_input
            session.add(project)
            session.commit()
        else:
            pass
        
        choice = input('Do you want to change the project description: y/n?')
        if choice == 'y' :
            proj_input = input('Enter new project description: ')
            project.description= proj_input
            session.add(project)
            session.commit()
        else:
            pass
        
        choice = input('Do you want to change the project manager: y/n?')
        if choice == 'y' :
            proj_input = input('Enter new project manager ID: ')
            project.manager_id= proj_input
            for employee in employees:
                employee.manager_id = proj_input
                session.add(employee)
                session.commit()
            session.add(project)
            session.commit()
        else:
            pass
    else:
        print('not')


### queries ####
def show_all_managers(session):
    all_managers = session.query(Manager).all()
    man_id = [manager.id for manager in all_managers]
    man_name = [manager.name for manager in all_managers]
    table = PrettyTable()
    table.hrules = True 
    table.field_names = ["ID", "Name"]
    for i in range(0,len(all_managers)):
        table.add_row([man_id[i], man_name[i]])
    print(table)


def show_all_manager_projects(session,id):
    #### BUILD TABLE FORMATTING
    all_manager_project = session.query(Project).filter(Project.manager_id == id).all()

    proj_id = [project.id for project in all_manager_project]
    proj_name = [project.name for project in all_manager_project]
    proj_description = [project.description for project in all_manager_project]
    proj_manager_id = [project.manager_id for project in all_manager_project]

    table = PrettyTable()
    table.field_names = ["Project_ID", "Manager_ID",  "Name", "description" ]
    table.hrules = True
    for i in range(0,len(all_manager_project)):
        table.add_row([proj_id[i], proj_manager_id[i], proj_name[i], proj_description[i]])
    print(table)
    manager_menu(id)

def show_all_manager_employees(session, id):
    #### BUILD TABLE FORMATTING
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == id).all()
    emp_id = [employee.id for employee in all_manager_employee]
    man_id = [employee.manager_id for employee in all_manager_employee]
    pro_id = [employee.project_id for employee in all_manager_employee]
    name = [employee.name for employee in all_manager_employee]
    email = [employee.email for employee in all_manager_employee]
    phone_number = [employee.phone_number for employee in all_manager_employee]
    position = [employee.position for employee in all_manager_employee]
    
    if len(all_manager_employee) == 0:
        print("-----------------------")
        print("You dont have any power")
        print("-----------------------")
    else:
        table = PrettyTable()
        table.field_names = ["Employee_ID", "Manager_ID", "Project_ID", "Name", "EMAIL", "Phone Number", "Position" ]
        table.hrules = True
        for i in range(0,len(all_manager_employee)):
            table.add_row([emp_id[i], man_id[i], pro_id[i], name[i], email[i], phone_number[i], position[i]])
        print(table)
    
    manager_menu(id)



#### DELETE ###    
@click.command()
@click.option('--employee_id', prompt='Enter Employee ID', help='employee name')  
@click.option('--manager_id', prompt='Enter Manager ID', help='employee name')  
def delete_employee(employee_id, manager_id):
    employee = session.query(Employee).filter(Employee.id == employee_id).first()
    if employee.manager_id == int(manager_id):
        session.delete(employee)
        session.commit()
        manager_menu(manager_id)
    else:
        print('This employee does not belong to this manager.')
        
        
@click.command()
@click.option('--manager_id', prompt='Enter your manager ID', help='employee name')  
@click.option('--deleted_manager_id', prompt='Enter Manager ID of manager to delete', help='employee name')  
def delete_manager(manager_id,deleted_manager_id):
        manager = session.query(Manager).filter(Manager.id == deleted_manager_id).first()
        session.delete(manager)
        session.commit()
        if int(manager_id) == int(deleted_manager_id):
            print('Congratulations, you are FREEEEEEE!!!!!! Good luck with Antonio')
        else:
            manager_menu(manager_id)


