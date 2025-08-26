import json
import os
from datetime import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Task status constants
PENDING = "pending"
DONE = "done"

def load_tasks():
    """Load tasks from the JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                tasks = json.load(file)
                # Ensure all tasks have the required fields
                for task in tasks:
                    if 'id' not in task:
                        task['id'] = len(tasks) + 1
                    if 'status' not in task:
                        task['status'] = PENDING
                    if 'created_at' not in task:
                        task['created_at'] = datetime.now().isoformat()
                return tasks
            except json.JSONDecodeError:
                return []
    else:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file"""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    """Add a new task"""
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty!")
        return tasks
    
    task_id = max([task['id'] for task in tasks], default=0) + 1
    new_task = {
        'id': task_id,
        'description': description,
        'status': PENDING,
        'created_at': datetime.now().isoformat()
    }
    tasks.append(new_task)
    print(f"Task added successfully (ID: {task_id})")
    return tasks

def list_tasks(tasks):
    """List all tasks"""
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- To-Do List ---")
    for task in tasks:
        status = "✓" if task['status'] == DONE else "○"
        print(f"{task['id']}. [{status}] {task['description']}")
    print("------------------")

def update_task(tasks):
    """Update an existing task description"""
    if not tasks:
        print("No tasks available to update.")
        return tasks
    
    try:
        task_id = int(input("Enter task ID to update: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return tasks
        
        new_description = input(f"Enter new description (current: '{task['description']}'): ").strip()
        if not new_description:
            print("Task description cannot be empty!")
            return tasks
        
        task['description'] = new_description
        print("Task updated successfully.")
        return tasks
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return tasks

def delete_task(tasks):
    """Delete a task"""
    if not tasks:
        print("No tasks available to delete.")
        return tasks
    
    try:
        task_id = int(input("Enter task ID to delete: "))
        task_index = next((i for i, t in enumerate(tasks) if t['id'] == task_id), None)
        if task_index is None:
            print(f"Task with ID {task_id} not found.")
            return tasks
        
        tasks.pop(task_index)
        print("Task deleted successfully.")
        return tasks
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return tasks

def mark_task_done(tasks):
    """Mark a task as done"""
    if not tasks:
        print("No tasks available to mark as done.")
        return tasks
    
    try:
        task_id = int(input("Enter task ID to mark as done: "))
        task = next((t for t in tasks if t['id'] == task_id), None)
        if not task:
            print(f"Task with ID {task_id} not found.")
            return tasks
        
        if task['status'] == DONE:
            print("Task is already marked as done.")
        else:
            task['status'] = DONE
            print("Task marked as done.")
        return tasks
    except ValueError:
        print("Invalid task ID. Please enter a number.")
        return tasks

def show_menu():
    """Display the menu options"""
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")
    print("-------------------------")

def main():
    """Main function to run the To-Do List Manager"""
    tasks = load_tasks()
    
    while True:
        show_menu()
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                tasks = add_task(tasks)
            elif choice == '2':
                list_tasks(tasks)
            elif choice == '3':
                tasks = update_task(tasks)
            elif choice == '4':
                tasks = delete_task(tasks)
            elif choice == '5':
                tasks = mark_task_done(tasks)
            elif choice == '6':
                save_tasks(tasks)
                print("Tasks saved. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
            
            # Save tasks after each operation
            save_tasks(tasks)
        except KeyboardInterrupt:
            save_tasks(tasks)
            print("\nTasks saved. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()