
from db.models import Base, Manager, Employee
from helpers import add_manager,add_employee,delete_employee,add_project,sign_in
import sys

# if __name__ == '__main__':
    # add_employee()

    # add_manager()
    
    
    # print('Thanks for using my CLI')


def start() :
    print('Welcome to the project manager tool!')
    
    options = {
        '1': sign_in
    }  
    print("Choose an option:")
    print("1. Sign in")
    
    # # options = {
    #     '1': add_manager,
    #     '2': add_employee,
    #     '3': delete_employee,
    #     '4': add_project
    # }

    # # prompt the user for their choice
    # print("Choose an option:")
    # print("1. Add Manager")
    # print("2. Add Employee")
    # print("3. del Employee")
    # print("4. add project ")

    choice = input("Enter your choice (1, 2,3): ")

    # invoke the corresponding function based on the user's choice
    if choice in options:
        options[choice]()
    else:
        print("Invalid choice.")
        sys.exit(1)
    
start()