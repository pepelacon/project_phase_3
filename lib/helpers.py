from db.models import Base, Manager, Employee, Project
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from prettytable import PrettyTable
import sys


engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


###sign in
def select_manager():
    while True:
        id = input("Enter your account ID: ").strip()
        user_manager = session.query(Manager).filter(Manager.id == id).first()
        print(user_manager)
        if  user_manager:
            break
        else:
            print("Invalid choice. Chose valid manager ID")
            continue
    print("-----------------------------")
    print(f"Hello {user_manager.name} ")
    print("-----------------------------")

    manager_menu(id)


def manager_menu(id):

    while True:

        print("        MAIN MENU         ")
        print("     Choose an option:    ")
        print("--------------------------")
        print("| 1 | See your projects  |")
        print("| 2 | Add a new project  |")
        print("| 3 | See your employees |")
        print("| 4 | Add a new employee |")
        print("| 5 | Delete an employee |")
        print("| 6 | Delete a manager   |")
        print("| 7 | Update a project   |")
        print("| 8 | Sign Out           |")
        print("--------------------------")
        
        choice = input("Enter your choice (1, 2, 3, 4, 5, 6, 7, 8): ")

        if choice == '1':
            show_all_manager_projects(session, id)
        elif choice == '2':
            add_project(id)
        elif choice == '3':
            show_all_manager_employees(session, id)
        elif choice == '4':
            add_employee(id)
        elif choice == '5':
            delete_employee(id)
        elif choice == '6':
            delete_manager(id)
        elif choice == '7':
            update_project(id)
        elif choice == '8':
            sign_out()
        else:
            print("------------------------------------")
            print("You need to chose one of the options")
            print("------------------------------------")

            continue

        break


def sign_out():
    from cli import start
    start()

def sign_in():
    show_all_managers()
    select_manager()

def sign_up():
    add_manager()
    
def exit_app():
    sys.exit(1)

### Create New ####

def add_manager():
    name= input('Enter New Manager name: ')
    email=input('Enter Email: ')
    manager = Manager(name = name , email = email)
    session.add(manager)
    session.commit()
    print(f"Hello {name} , {email} : your id is {manager.id}!")
    manager_menu(manager.id)
    

############## $ ADD EMPLOYEE --------------- 

def add_employee(manager_id):
    name = input("Enter New employee name: ")
    email = input("Enter employee Email: ")
    # email = input("Enter employee Email: ")
    phone_number = input("Enter employee Phone Number: ")
    position = input("Enter employee Position: ")

    ######## ADDD PRETYY TABLES ###########
    all_manager_project = session.query(Project).filter((Project.manager_id == manager_id ) | (Project.manager_id == None)).all()
    print("----------------------------------------------------------------")
    print("                                                                ")
    print("list of current projects to choose for your new employee:")
    table = PrettyTable()
    table.field_names = ["Project_ID", "Project_name",  "Project manager ID"]
    table.hrules = True
    for project in all_manager_project:
        table.add_row([project.id, project.name, project.manager_id])
    print(table)
    
    projects_id = [proj.id for proj in all_manager_project]
    if not len(projects_id):
        chosen_proj = None
    else:
        while True:
            try:
                chosen_proj = int(input("Enter project ID to assign employee: "))
            except ValueError:
                print("Invalid choice. Chose valid project ID")
                continue
            if chosen_proj in projects_id:
                    break
            else:
                print("Invalid choice. Chose valid project ID")
    employee = Employee(name = name , email = email, phone_number = phone_number, position=position, manager_id=manager_id, project_id=chosen_proj)
    session.add(employee)
    session.commit()
    print(f"Created new {employee}!")
    manager_menu(manager_id)


############## ! ADD PROJECT ---------------

def add_project(manager_id):
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == manager_id).all()
    employees_id = [emp.id for emp in all_manager_employee]
    if employees_id:
        name = input("Enter New project name: ")
        description = input("Enter description: ")
        project = Project(name = name , description = description, manager_id = manager_id)
        session.add(project)
        session.commit()
        print("Your employee: ")
        print("---------------------------------------------------------------------------")
        [print(f'ID: {emp.id} | Employee name: {emp.name}') for emp in all_manager_employee]
        print("---------------------------------------------------------------------------")
        
        while True:
            try:
                chosen_employee = int(input("Enter employee ID for project: "))
            except ValueError:
                print("Invalid choice. Chose valid employee ID")
                continue
            if chosen_employee in employees_id:
                    break
            else:
                print("Invalid choice. Chose valid employee ID")
                
        employee_for_this_project =  session.query(Employee).filter(Employee.id == chosen_employee).first()
        employee_for_this_project.project_id = project.id
        employee_for_this_project.manager_id = manager_id
        session.add(employee_for_this_project)
        session.commit()
        print(f"Your project was Created: {project} !")
    else:
        print('You have no employees to assign to a new project. Please hire an employee')
    manager_menu(manager_id)




############ edit / update #################

def update_project(manager_id):
    projects = session.query(Project).filter((Project.manager_id == manager_id ) | (Project.manager_id == None)).all()
    
    all_manager_project = session.query(Project).filter((Project.manager_id == manager_id ) | (Project.manager_id == None)).all()

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
    
    project_id = input('Enter project id of project to edit: ')
    employees = session.query(Employee).filter(Employee.project_id == project_id ).all()
    if int(project_id) in [project.id for project in projects]:
        project = session.query(Project).filter( Project.id == project_id).first()
        choice = input('Do you want to change the project name: y/n?: ')
        options= ['y','n']  
        while choice not in options:
            choice = input('invalid input - enter y/n: ')
        if choice == 'y' :
            proj_input = input('Enter new project name: ')
            project.name= proj_input
            session.add(project)
            session.commit()
            # break
        else:
            pass
        
        choice = input('Do you want to change the project description: y/n?: ')
        while choice not in options:
            choice = input('invalid input - enter y/n: ')
        if choice == 'y' :
            proj_input = input('Enter new project description: ')
            project.description= proj_input
            session.add(project)
            session.commit()
        else:
            pass
        
        choice = input('Do you want to change the project manager: y/n?: ')
        while choice not in options:
            choice = input('invalid input - enter y/n: ')
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
        print('Stay in your lane. You do not have power to change this project.')
    manager_menu(manager_id)


### queries ####
def show_all_managers():
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
    table = PrettyTable()
    table.field_names = ["Project_ID", "Manager_ID",  "Name", "description" ]
    table.hrules = True
    for project in all_manager_project:
        table.add_row([project.id, project.manager_id, project.name, project.description])
    print(table)
    manager_menu(id)


def show_all_manager_employees(session, id):
    #### BUILD TABLE FORMATTING
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == id).all()

    if len(all_manager_employee) == 0:
        print("-----------------------")
        print("You dont have any power")
        print("-----------------------")
    else:
        table = PrettyTable()
        table.field_names = ["Employee_ID", "Manager_ID", "Project_ID", "Name", "EMAIL", "Phone Number", "Position" ]
        table.hrules = True
        for employee in all_manager_employee:
            table.add_row([employee.id, employee.manager_id, employee.project_id, employee.name, employee.email, employee.phone_number, employee.position])
        print(table)
    
    manager_menu(id)



#### DELETE ###    
def delete_employee( manager_id):
    all_manager_employee = session.query(Employee).filter(Employee.manager_id == manager_id).all()
    print("Your employees: ")
    print("---------------------------------------------------------------------------")
    [print(f'ID: {emp.id} | Employee name: {emp.name}') for emp in all_manager_employee]
    print("---------------------------------------------------------------------------")
    employee_id = [emp.id for emp in all_manager_employee]
    if all_manager_employee:
        while True:
            try:
                chosen_employee = int(input("Enter employee ID: "))
            except ValueError:
                print("Invalid choice. Chose valid employee ID")
                continue
            if chosen_employee in employee_id:
                    break
            else:
                print("This is not your employee. Choose from the table above.")
                
    else:
        print("You dont have employees, hire them before fire")
        print("---------------------------------------------------------------------------")
        manager_menu(manager_id)
    employee = session.query(Employee).filter(Employee.id == chosen_employee).first()
    
    session.delete(employee)
    session.commit()
    print(f'Deleted employee: {employee} ')
    manager_menu(manager_id)



def delete_manager(id):
    print('List of current managers:')
    show_all_managers()
    managers_id = [man.id for man in session.query(Manager).all()]
    while True:
        try:
            chosen_manager = int(input("Enter manager ID: "))
        except ValueError:
            print("Invalid choice. Chose valid manager ID")
            continue
        if chosen_manager in managers_id:
            break
        else:
            print("Invalid choice. Chose valid manager ID")
    
    manager = session.query(Manager).filter(Manager.id == chosen_manager).first()
    session.delete(manager)
    session.commit()
    print(f'Deleted manager: {manager} ')
    
    if int(id) == chosen_manager:
        print('Congratulations, you are FREEEEEEE!!!!!! Good luck with Antonio')
        sign_out()
    else:
        manager_menu(id)


