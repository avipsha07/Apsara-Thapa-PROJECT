import json
import os

TASKS_FILE = "tasks.json"

# Class: Task
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"title": self.title, "completed": self.completed}



# Function: load_tasks
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        data = json.load(file)
        return [Task(**task) for task in data]



# Function: save_tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump([t.to_dict() for t in tasks], file, indent=4)



# Function: display_menu
def display_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")



# MAIN FUNCTION (Required)
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            tasks.append(Task(title))
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                status = "✔" if task.completed else "✘"
                print(f"{i+1}. {task.title} [{status}]")

        elif choice == "3":
            index = int(input("Enter task number to complete: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index].completed = True
                save_tasks(tasks)
                print("Task completed!")
            else:
                print("Invalid task number.")

        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
                print("Task deleted!")
            else:
                print("Invalid task number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option! Try again.")


# Run the program
if __name__ == "__main__":
    main()
