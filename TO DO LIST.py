#Hello all I am Tharun Kumar Reddy Chitiki 
# Iam writing this code to make a to do list as a part of my internship task in CODE SOFT
# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to remove a task by its index
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Invalid task index.")

# Main program loop
while True:
    print("\nTodo List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter a task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter the index of the task to remove: "))
        remove_task(index)
    elif choice == "4":
        print("See you soon :) ")
        break
    else:
        print("Invalid choice. Please select a valid option.")
