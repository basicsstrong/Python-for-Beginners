# Import necessary libraries
import os

# Function to load tasks from the file
def load_tasks():
    """
    Loads the tasks from 'tasks.txt' file. 
    If the file does not exist, returns an empty list.
    """
    try:
        # Open the tasks file in read mode
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            # Clean up newlines and extra spaces
            tasks = [task.strip() for task in tasks]  
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        tasks = []  
    return tasks

# Function to save tasks back to the file
def save_tasks(tasks):
    """
    Saves the list of tasks to 'tasks.txt' file.
    Each task is written to a new line.
    """
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

# Function to add a new task
def add_task(tasks):
    """
    Prompts the user to enter a new task and adds it to the list of tasks.
    Then saves the updated list to the file.
    """
    task = input("Enter a new task: ")
    tasks.append(task)  # Add the task to the list
    print(f"Task '{task}' added!")
    save_tasks(tasks)

# Function to view all tasks
def view_tasks(tasks):
    """
    Displays all the tasks in the list. 
    If no tasks are present, it notifies the user.
    """
    if not tasks:
        print("No tasks available!")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to mark a task as complete
def mark_task_complete(tasks):
    """
    Prompts the user to select a task by its number and marks it as complete. 
    The task will be updated with a '(Completed)' tag.
    """
    view_tasks(tasks)  # Show the tasks first
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        task = tasks[task_number - 1]
        tasks[task_number - 1] = task + " (Completed)"
        print(f"Task '{task}' marked as complete!")
        save_tasks(tasks)
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

# Function to delete a task
def delete_task(tasks):
    """
    Prompts the user to select a task by its number and deletes it from the list.
    """
    view_tasks(tasks)  # Show all tasks first
    try:
        task_number = int(input("Enter the task number to delete: "))
        task = tasks.pop(task_number - 1)  # Remove the task
        print(f"Task '{task}' deleted!")
        save_tasks(tasks)
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

# Main function to run the To-Do List application
def main():
    """
    Main loop for the To-Do List application.
    It allows the user to interact with the list of tasks.
    """
    tasks = load_tasks()  # Load tasks when the app starts
    
    whi
