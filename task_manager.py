# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

def reg_user():
    '''Add a new user to the user.txt file'''
    valid_user = True
    # - Request input of a new username
    while valid_user:
        new_username = input("New Username: ")
        for i in username_password.keys():
            if i == new_username:
                print("Username has been taken. Please choose a new Username.")
                break
            else:
                valid_user = False
            

    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password
        
        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

    # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Then get the current date.
    curr_date = date.today()
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }

    task_list.append(new_task)
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))
    print("Task successfully added.")

def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''
    
    for num, t in enumerate(task_list, 1): #tried to incoporate enumerate to display numbers
        disp_str = f"{num} Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)
        #yes_or_no = input("completed task Y/N: ")

def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''

    dictionary = {}
    for num, t in enumerate(task_list, 1):
        if t['username'] == curr_user:
            disp_str = f"{num} Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            dictionary[num] = t
            print(disp_str)
    user_input = int(input("Please input a valid number or -1 to return: "))
    if input == -1:
        return
    user_selection = dictionary[user_input]
    edit_choice = input("""What would you like to do with this task?\n
    1) Mark as Complete
    2) Change the Due Date
    3) Change the Assigned User\n
    Please select 1, 2 or 3: """)
    if edit_choice == "1":
        user_selection["completed"] = True
        user_selection["due_date"]

    elif edit_choice == "2":
        user_selection["due_date"] = input("Please change the Due Date: ")
    
    elif edit_choice == "3":
        user_selection["username"] = input("Please type in the new user: ")

    print(dictionary)
    print(user_selection)

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)
for task in task_list:
    print(task['username'])

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()
            
    elif menu == 'vm':
        view_mine()
    
    elif menu == "gr":
        task_overview_string = ""
        completed_tasks = 0
        uncompleted_tasks = 0
        overdue_tasks = 0
        uncompleted_percentage = 0
        overdue_percentage = 0
        todays_date = datetime.now()
        task_list_lenght = len(task_list)
        task_overview_string += f"Total Tasks: {task_list_lenght}\n"
        for i in task_list:
    
            if i["completed"] == True:
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                if todays_date > i["due_date"]:
                    overdue_tasks += 1
                uncompleted_percentage = (uncompleted_tasks / task_list_lenght) * 100
                overdue_percentage = (overdue_tasks / task_list_lenght) * 100
        task_overview_string += f"Completed Tasks: {completed_tasks}\n"
        task_overview_string += f"Uncompleted Tasks: {uncompleted_tasks}\n"
        task_overview_string += f"Overdue Tasks: {overdue_tasks}\n"
        task_overview_string += f"Uncompleted Percentage: {uncompleted_percentage}\n"
        task_overview_string += f"Overdue Percentage: {overdue_percentage}\n"

        username_password_lenght = len(username_password)
        user_tasks_dict = {}
        user_tasks_perc_dict = {}
        user_tasks_perc_complete_dict = {}
        user_tasks_perc_uncomplete_dict = {}
        user_tasks_overdue_dict = {}
        user_tasks = 0
        user_tasks_complete = 0
        user_tasks_incomplete = 0
        user_tasks_overdue = 0 
        percentage_user_tasks_completed = 0
        percentage_user_tasks_uncompleted = 0
        percentage_user_tasks_overdue = 0
        user_overview_string = ""
        
        for x in username_password.keys():
            for y in task_list:
                if x == y["username"]:
                    user_tasks += 1
                    if y["completed"] == True:
                        user_tasks_complete += 1
                    else:
                        user_tasks_incomplete += 1
                        if todays_date > y["due_date"]:
                            user_tasks_overdue += 1
            user_tasks_dict[x] = user_tasks    
            percentage_user_tasks_total = (user_tasks / task_list_lenght) * 100
            user_tasks_perc_dict[x] = percentage_user_tasks_total
            percentage_user_tasks_completed = (user_tasks_complete / user_tasks) * 100
            user_tasks_perc_complete_dict[x] = percentage_user_tasks_completed
            percentage_user_tasks_uncompleted = (user_tasks_incomplete / user_tasks) * 100
            user_tasks_perc_uncomplete_dict[x] = percentage_user_tasks_uncompleted
            percentage_user_tasks_overdue = (user_tasks_overdue / user_tasks) * 100
            user_tasks_overdue_dict[x] = percentage_user_tasks_overdue

        user_overview_string += f"Total Users: {username_password_lenght}\n"
        user_overview_string += f"Total Tasks: {task_list_lenght}\n"
        for x in username_password.keys():
            user_overview_string += f"Total Statistics for {x}\n"
            user_overview_string += f"Total Tasks Assigned: {user_tasks_dict[x]}\n"
            user_overview_string += f"Percentage Tasks Assigned: {user_tasks_perc_dict[x]}\n"
            user_overview_string += f"Percentage Tasks Completed: {user_tasks_perc_complete_dict[x]}\n"
            user_overview_string += f"Percentage Tasks Incompleted: {user_tasks_perc_uncomplete_dict[x]}\n"
            user_overview_string += f"Percentage Overdue: {user_tasks_overdue_dict[x]}\n"
            

        with open("task_overview.txt", "w+") as task_overview:
            task_overview.write(task_overview_string)
        with open("user_overview.txt", "w+") as user_overview:
            user_overview.write(user_overview_string)
                
    elif menu == 'ds' and curr_user == 'admin': 
        '''If the user is an admin they can display statistics about number of users
            and tasks.'''
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
