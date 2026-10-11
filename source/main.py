import json
import os

# Initialize the file path
file_path = "../task.json"


def load_data():
    with open(file_path, 'r', encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def initialize_user():
    if os.path.isfile(file_path):
        data = load_data()
        print(f"Welcome back, {data.get('name', 'User')}!\n")
    else:
        print("Hey there new user, what is your name?")
        name = input("Name: ").strip() or "User"
        initial_data = {
            "name": name,
            "tasks": [],
            "done": []
        }
        save_data(initial_data)
        print(f"\nHi {name}!\nThis is a TODO list where you can manage and complete your tasks.\n")


def show_menu():
    print("--- List of commands ---")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. List of pending tasks")
    print("4. Mark a task complete")
    print("5. View completed task")
    print("9. Exit the program")
    print("0. Reset data\n")


def addTask(task: str):
    if not task.strip():
        print("Task cannot be empty.\n")
        return
    data = load_data()
    data["tasks"].append(task.strip())
    save_data(data)
    print("Task was added.\n")


def list_tasks(completed):
    data = load_data()
    key = "done" if completed else "tasks"
    title = "Completed tasks" if completed else "Pending Tasks"
    items = data.get(key, [])

    if not items:
        print(f"No {title.lower()} found.\n")
        return False

    print(f"\n--- {title} ---")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print()
    return True


def remove_task():
    pass


def mark_task():
    pass


def reset_task():
    pass


if __name__ == "__main__":
    initialize_user()

    # CLI
    function_to_choose = -1
    while function_to_choose != 9:
        show_menu()
        function_to_choose = int(input("Choose a command: "))
        if function_to_choose == 1:
            new_task = input("Enter a task: ")
            addTask(new_task)
        elif function_to_choose == 2:
            remove_task()
        elif function_to_choose == 3:
            list_tasks(False)
        elif function_to_choose == 4:
            mark_task()
        elif function_to_choose == 5:
            list_tasks(True)
        elif function_to_choose == 9:
            print("Goodbye! See you later.")
        elif function_to_choose == 0:
            reset_task()
        else:
            print("Wrong input. Please Try again\n")
