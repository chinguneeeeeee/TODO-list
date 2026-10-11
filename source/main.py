import json
import os

# Initialize the variables
file = "../task.json"
file_exist = True

# Check whether the file exists or not
if not os.path.isfile(file):
    file_exist = False

# Check if it is a new user or not
if file_exist:
    with open(file, "r") as f:
        data = json.load(f)
    print("Welcome back ", data["name"], "!", sep="")
    print()
else:
    print("Hey there new user, what is your name?")
    name = input("Name: ")
    x = {
        "name": name,
        "tasks": [

        ],
        "done": [

        ],
    }
    with open(file, "w", encoding="utf-8") as f:
        json.dump(x, f)
    print("Hi ", name, "!\n"
                       "This is a TODO list that you can add/update tasks and mark your tasks!", sep="")
    print()


def list_of_task():
    print("List of commands")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. List of tasks")
    print("4. Mark a task complete")
    print("9. Exit the program")
    print("0. Reset data\n")


def newTask(tsk: str):
    with open(file, "r") as f:
        value = json.load(f)
    value["tasks"].append(tsk)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(value, f)


def listOfTasks():
    with open(file, "r") as f:
        val = json.load(f)

    count = 1

    if not val["tasks"]:
        print("The tasks are empty\n")
    else:
        for i in val["tasks"]:
            print(count, ". ", i, sep="")
        print()

if __name__ == "__main__":
    # CLI
    function_to_choose = -1
    while function_to_choose != 9:
        list_of_task()
        function_to_choose = int(input("Choose a command: "))
        if function_to_choose == 1:
            task = input("Enter a task: ")
            newTask(task)
        elif function_to_choose == 2:
            pass
        elif function_to_choose == 3:
            listOfTasks()
        elif function_to_choose == 9:
            pass
        elif function_to_choose == 0:
            pass
        else:
            print("Wrong input. Please Try again\n")
