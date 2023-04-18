
from db.models import Base, Manager, Employee
from helpers import sign_up,add_employee,delete_employee,add_project,sign_in
import sys

if __name__ == '__main__':
    
    def start() :
        print('Welcome to the project manager tool!')
        
        options = {
            '1': sign_in,
            '2': sign_up
        }  
        print("Choose an option:")
        print("1. Manager Sign in")
        print("2. Manager Sign up")
        
        choice = input("Enter your choice (1, 2): ")

        if choice in options:
            options[choice]()
        else:
            print("Invalid choice.")
            sys.exit(1)
        
    start()