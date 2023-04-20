
from db.models import Base, Manager, Employee
from helpers import sign_up,add_employee,delete_employee,add_project,sign_in
import sys
import pyfiglet

def start() :
    print('Welcome to the project manager tool!')
    text = "WTFAlchemy"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
    options = {
        '1': sign_in,
        '2': sign_up
    }  
    print("Choose an option:")
    print("----------------------")
    print("| 1. Manager Sign IN |")
    print("----------------------")
    print("| 2. Manager Sign UP |")
    print("----------------------")
    
    
    while True:
        choice = input("Enter your choice (1, 2): ")
        if choice in options:
            break
        else:
            print("-------------------------------------------")
            print("Sorry,you need to chose one of the options.")
            print("-------------------------------------------")
            continue
    options[choice]()

start()
  