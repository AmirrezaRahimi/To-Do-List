"""
Created on Tue Mar  7 09:21:33 2023

@author: Amirreza Rahimi
"""

#ToDo List
## add , remove , edit , search , display , reset , exit
def add():
    """add a new task to the todo list"""
    task = input('your task: ')
    if task not in tasks:
        tasks.append(task)
        is_done.append(False)
    else:
        print(f'{task} is exist!')

def display():
    for i in range(len(tasks)):
        print(f'{i+1}: {tasks[i]} ----> {is_done[i]}')

def remove():
    try:
        i = int(input("index of task to remove: "))
        if i <= len(tasks) and i >= 1:
            i -= 1
            tasks.pop(i)
            is_done.pop(i)
            print('Your task has been successfully deleted')
        else:
            print('index out of range!')
            remove()
    except Exception as error:
        print(error)
        remove()

def edit():
    try:
        i = int(input("index of task to edit: "))
        if i <= len(tasks) and i >= 1:
            i -= 1
            new_task = input('new task: ')
            tasks[i] = new_task
            print('Your task has been successfully edited')
        else:
            print('index out of range!')
            edit()
    except Exception as error:
        print(error)
        edit()

def search():
    task = input('task to search: ').lower()
    for i in range(len(tasks)):
        if task in tasks[i]:
            print(f'{tasks[i]} ----> {is_done[i]}')

def done(done_list):
    for i in done_list:
        try:
            is_done[i-1] = True
        except Exception as error:
            print(error)

tasks = []
is_done = []
while True:
    command = input("""Todo-List@Select an option\
    (add-remove-edit-search-done-display-reset-exit):$ """).lower()
    if command == 'add':
        add()
    elif command == 'remove':
        display()
        remove()
    elif command == 'edit':
        display()
        edit()
    elif command == 'search':
        search()
    elif command == 'done':
        tasks_done = input('tasks: ')
        done_list = list(map(int, tasks_done.split()))
        done(done_list)
    elif command == 'display':
        display()
    elif command == 'reset':
        pass
    elif command == 'exit':
        exit()
    elif command == '':
        pass
    else:
        print(f'{command} : not found!')
