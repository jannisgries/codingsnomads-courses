'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''
##############################################################
# TO-DOS before running script
##############################################################
# Create VENV and install inquirer

##############################################################
# Script Initialization
##############################################################
import inquirer
import requests
from pprint import pprint

chosen_task = ""
active_user = None
user_api_url = 'http://demo.codingnomads.co:8080/tasks_api/users'
tasks_api_url = 'http://demo.codingnomads.co:8080/tasks_api/tasks'
horizontal_line = "__________________________________________"

##############################################################
# Function Definitions
##############################################################

def ask_user_options() -> str:
    """Ask user, which action he would like to take


    Returns:
        str: Chosen option
    """
    questions = [
        inquirer.List(
            "size",
            message="What would you like to do?",
            choices=["1) Create a new account (POST)",
                     "2) View all your tasks (GET)",
                     "3) View your completed tasks (GET)",
                     "4) View only your incomplete tasks (GET)",
                     "5) Create a new task (POST)",
                     "6) Update an existing task (PATCH/PUT)",
                     "7) Delete a task (DELETE)",
                     "QUIT"],
        ),
    ]
    chosen_task = inquirer.prompt(questions)['size']
    print(f"\n{horizontal_line}\n")
    return chosen_task

def get_user(user_email: str = "") -> dict:
    """Get and return user data either from local storage or api

    Args:
        user_email (str, optional): user email. Defaults to "".

    Returns:
        dict: User db entry as dict
    """
    # Initialize variables
    user = None
    quit_login = False
    answer = ""
    # Check if user is already "logged in" and return local stored user data
    if active_user != None:
        user = active_user
    # Get user data from api
    else:
        while user == None and quit_login == False:
            # Get User Email
            if user_email == "" or answer == "Try again":
                user_email = input("Please type in the E-Mail, you have registered with: ")
            params = {
                'email': user_email
            }
            # Get User Data from API
            response = requests.get(user_api_url, params=params)
            if response.status_code == 200:
                user = response.json()['data'][0]
            # Error handling
            else: 
                print("Sorry, but something went wrong.")
                questions = [
                    inquirer.List(
                        "quit",
                        message="What would you like to do?",
                        choices=["Try again",
                                "Go back to Main Menu"],
                    ),
                ]
                answer = inquirer.prompt(questions)['quit']
                if answer == "Go back to Main Menu":
                    quit_login = True
    return user

def print_tasks(params: dict):
    """Print all the tasks, the user has asked for

    Args:
        params (dict): Parameters for API call, namely userId and potentially filter: completed / incompleted
    """
    # Check if user provided filter element > Delete from params and store in local variable 
    # Background: Just want to call the api once, therefore need all tasks > Filter locally, not by api
    if 'complete' in params:
        task_complete = params['complete']
        del params['complete']
    # Check if local storage contains user tasks, if not call api
    if 'tasks' not in active_user or active_user['tasks'] == [{}]:
        response = requests.get(tasks_api_url, params=params)
        # add the returned tasks to the local storage variable of the user
        if response.status_code == 200:
            data = response.json()['data']
            active_user['tasks'] = data
        # Error handling
        else: 
            print("\nSorry, something went wrong - Please try again.")
            print(f"\n{horizontal_line}\n")
    print("")
    no_task = True
    # Print the tasks from local user variable
    for task in active_user['tasks']:
        # Filter, to only print out the required tasks
        if 'task_complete' in locals():
            if task['completed'] == (task_complete == 'complete'):
                no_task = False
                print(f"- {task['name']}\n  {task['description']}")
        else:
            print(f"- {task['name']}\n  {task['description']}")
            no_task = False
    # Fallback-Message, if user hasnt got any tasks
    if no_task == True:
        print(f"You havent saved any tasks of this category.")
    print(f"{horizontal_line}")

def add_tasks(request_type: str, user_data:dict, task_id: int = 0):
    """Manipulate the stored data through api calls

    Args:
        request_type (str): type of api call
        user_data (dict): data which should be provided in body of api call
        task_id (int, optional): if task should be updated, id of task. Defaults to 0.
    
    Returns:
        dict: New Tasks, which was added / manipulated

    """
    if request_type == "post":
        response = requests.post(tasks_api_url, json=user_data)
        return response.json()['data']
    elif request_type == "put":
        taskid_added_task_api_url = tasks_api_url + f"/{task_id}"
        response = requests.put(taskid_added_task_api_url, json=user_data)
        return response.json()['data']
    if response.status_code == 201 or response.status_code == 200:
        print("Your task has been successfully (re)written.")
    else: 
        print("\nSorry, something went wrong - Please try again.")
        print(f"\n{horizontal_line}\n")

def choose_task(params: dict, task_action:str) -> int:
    """Get tasks from local variable or api and prompt user to choose one, then return this task

    Args:
        params (dict): Parameters for potential api call
        task_action (str): Action, which should be done with the task (eg. delte)

    Returns:
        int: id of the task
    """
    # Get user tasks
    # this could be abstracted into a get_tasks() method, which is also used in the print_tasks(method)
    if 'tasks' not in active_user or active_user['tasks'] == [{}]:
        response = requests.get(tasks_api_url, params=params)
        if response.status_code == 200:
            data = response.json()['data']
            if data == []:
                print(f"There are currently no tasks to {task_action}")
                chosen_task = None
            else: 
                active_user['tasks'] = data
        else: 
            print("\nSorry, something went wrong - Please try again.")
            print(f"\n{horizontal_line}\n")

    if 'tasks' in active_user:
        # convert the list of dicts into one dict, which has name of task as value and id as key
        # the other way around m
        tasks_as_dict = {el['id']: f"{el['name']} ({el['id']})" for el in active_user['tasks']}
        choices = [value for value in tasks_as_dict.values()]
        choices.append("Quit")
        questions = [
            inquirer.List(
                "task",
                message=f"Which task would you like to {task_action}?",
                choices=choices,
            ),
        ]
        answer = inquirer.prompt(questions)['task']
        if answer != "Quit":
            chosen_task = 0
            for el in active_user['tasks']:
                if answer == f"{el['name']} ({el['id']})":
                    chosen_task = el['id']
            return chosen_task
        else:
            return None

def get_task_index_by_id(id: int) -> int:
    """Get and return the index of the task, which is stored in a list of other tasks

    Args:
        id (int): id of the task (unique)

    Returns:
        int: index of the task in the local stored list of user tasks.
    """
    if 'tasks' in active_user:
        index = 0
        for el in active_user['tasks']:
            if el['id'] == id:
                task_index = index
            index+= 1
        return task_index
    else:
       return None

def wait_for_user():
    """Force User to press Enter in order to continue
    """
    while True:
        user_input = input("\nPress Enter to choose next option: ")
        if user_input == "":
            break
        else: 
            print("Please press enter only.")
    print(f"\n{horizontal_line}\n")

##############################################################
# Interact with API
##############################################################
while chosen_task != "QUIT":
    ##############################################################
    # Ask User for Task, which he would like to do
    chosen_task = ask_user_options()

    ##############################################################
    # Create New Account
    if chosen_task == "1) Create a new account (POST)":
        user_email = input("Please type in your email: ")
        user_fname = input("What is your first name? ")
        user_lname = input("What is your last name? ")
        user_data = {
            "email": user_email,
            "first_name": user_fname,
            "last_name": user_lname
        }
        response = requests.post(user_api_url, json=user_data)
        if response.status_code == 201:
            print("\nPerfect, your user account has been created.")
            # Set local variables
            user_email = response.json()['data']['email']
            active_user = get_user(user_email)
        else:
            print("Sorry, something went wrong. Please try again.")
    ##############################################################
    # View all tasks of user
    elif chosen_task == "2) View all your tasks (GET)":
        active_user = get_user()
        user_id = active_user['id']
        params = {
            'userId' : user_id
        }
        print("")
        print_tasks(params=params)

    ##############################################################
    # View all completed tasks of user
    elif chosen_task == "3) View your completed tasks (GET)":
        active_user = get_user()
        user_id = active_user['id']
        params = {
            'userId' : user_id,
            'complete': 'complete'
        }
        print("")
        print_tasks(params=params)

    ##############################################################
    # View all incompleted tasks of user
    elif chosen_task == "4) View only your incomplete tasks (GET)":
        active_user = get_user()
        user_id = active_user['id']
        params = {
            'userId' : user_id,
            'complete': 'incomplete'
        }
        print("")
        print_tasks(params=params)

    ##############################################################
    # Create new task
    elif chosen_task == "5) Create a new task (POST)":
        active_user = get_user()
        user_id = active_user['id']
        task_name = input("What is the name of the task? ")
        task_description = input(f"How would you describe the task '{task_name}': ")
        data = {
                "userId": user_id,
                "name": task_name,
                "description": task_description,
                "completed": False
                }
        print("")
        task = add_tasks(request_type="post", user_data=data)
        # Add the added task to the local variable of the user
        active_user['tasks'].append(task)
        
    ##############################################################
    # Update an existing task
    elif chosen_task == "6) Update an existing task (PATCH/PUT)":
        active_user = get_user()
        user_id = active_user['id']
        params = {
            'userId' : user_id
        }
        chosen_task = 0
        while chosen_task != None:
            chosen_task_id = choose_task(params=params,task_action="update")
            if chosen_task_id == None:
                break
            local_task_index = get_task_index_by_id(id=chosen_task_id)
            quit_update = False
            while quit_update == False:
                task = active_user['tasks'][local_task_index]
                questions = [
                    inquirer.List(
                        "task",
                        message="Which information would you like to change ?",
                        choices=[
                            f"Name: {task['name']}", 
                            f"Description: {task['description']}",
                            f"Completed: {task['completed']}",
                            "Done with changing"
                        ]
                    ),
                ]
                answer = inquirer.prompt(questions)['task']
                if answer == "Done with changing":
                    quit_update = True
                    break
                new_value = input("Please type in the new value: ")
                if answer == f"Name: {task['name']}":
                   task['name'] = new_value
                elif answer == f"Description: {task['description']}":
                   task['description'] = new_value
                elif answer == f"Completed: {task['completed']}":
                   task['completed'] = new_value in ['True', 'true']
            
            # Update local user data
            active_user['tasks'][local_task_index] = task

            # Update Value on API
            data = {
                "userId": task['userId'],
                "name": task['name'],
                "description": task['description'],
                "completed": task['completed']
            }
            add_tasks(request_type="put", user_data=data, task_id=chosen_task_id)
    ##############################################################
    # Delete Task
    elif chosen_task == "7) Delete a task (DELETE)":
        active_user = get_user()
        user_id = active_user['id']
        params = {
            'userId' : user_id
        }
        chosen_task = 0
        while chosen_task != None:
            chosen_task_id = choose_task(params=params,task_action="delete")
            if chosen_task_id == None:
                break
            local_task_index = get_task_index_by_id(id=chosen_task_id)
            task = active_user['tasks'][local_task_index]
            confirm = input(f"Are you sure to delete the task: {task['name']} ?\nType in 'yes' to confirm: ")
            if confirm.lower() == "yes":
                # Delete task w/ api
                taskid_added_task_api_url = tasks_api_url + f"/{chosen_task_id}"
                response = requests.delete(taskid_added_task_api_url)
                if response.status_code == 200:
                    # Delete task from local user variable
                    active_user['tasks'].pop(local_task_index)
                    print("\nThe task was sucessfully deleted!\n")
                else: 
                    print("Something went wrong, please try again.")
    if chosen_task != "QUIT":
        wait_for_user()