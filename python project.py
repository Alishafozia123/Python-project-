import os

# File to store the tasks
TASK_FILE = 'tasks.txt'

# Function to load tasks from the file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]  # Strip newlines and extra spaces
    return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display tasks
def display_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour To-Do list is empty!")

# Function to add a new task
def add_task(tasks):
    task = input("\nEnter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added!")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] = tasks[task_num - 1] + " (Completed)"
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        
        try:
            choice = int(input("\nChoose an option (1-5): "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                mark_completed(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
