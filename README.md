# Phase 3 CLI Project  - Daniel, Diana, Mandy

## How to run:

- in the terminal run: pipenv install
- in the terminal run: pipenv shell
- in the terminal run: python lib/db/seed.py
- in the terminal run: python lib/cli.py

## Description
- This is a project management tool for managers

## Functionality

- Landing page:

  - sign in: existing managers log in using their manager ID
  - sign up: new managers can sign up (name and email) and receive their manager ID
  - exit application

- Main manager menu - can do the following: 
  - See your projects
  - Add a new project: manager can create a new project and assign one of their employees to that project. The project is assigned this manager as project manager
  - See your employees: manager can see all their employees
  - Add a new employee: a manager can create a new employee (name, email, phone, position) and assign one of their projects to that employee. The employee is assigned this manager as project manager
  - Delete an employee: manager can delete their employee. Cannot delete an employee not assigned to them
  - Delete a manager: manager can delete a manager: a. if delete self, manager is logged out, 2. if delete other manager, return to main manager menu
  - Update a project: manager can update their project or a project not assigned to any manager
      - can edit project name, project description, assign manager
  - Sign Out: return to landing page


 