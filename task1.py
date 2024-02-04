#task 1
import os
import json
from datetime import datetime
#store the list data
TODO_FILE = "todo_list.json"
# Function to load list
def load_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    else:
        return []
# Function to save list
def save_todo_list(todo_list):
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=2)
# Function to display list
def display_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the To-Do list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task['title']} - {task['due_date']}")
# Function to add a new task to list
def add_task(todo_list):
    title = input("Enter task title: ")
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {"title": title, "due_date": str(due_date), "completed": False}
    todo_list.append(task)
    print("Task added successfully.")
# Function to mark a task as completed
def complete_task(todo_list):
    display_todo_list(todo_list)
    task_idx = int(input("Enter the task number to mark as completed: ")) - 1

    if 0 <= task_idx < len(todo_list):
        todo_list[task_idx]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")
# Function to remove completed tasks from the list
def remove_completed_tasks(todo_list):
    todo_list = [task for task in todo_list if not task["completed"]]
    print("Completed tasks removed.")
# Main function
def main():
    
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Application")
        print("1. Display To-Do List")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Remove Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            complete_task(todo_list)
        elif choice == "4":
            remove_completed_tasks(todo_list)
        elif choice == "5":
            
            save_todo_list(todo_list)
            print("To-Do list saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()