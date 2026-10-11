"""
==========================================================
 SIMPLE TO-DO LIST (Command Line)
 First Year Python Project - Easy Version
==========================================================

WHAT THIS DOES:
    Lets the user add tasks, view tasks, mark them as done,
    and delete them. Tasks are stored in a simple LIST while
    the program is running.

CONCEPTS USED (easy to explain in viva):
    1. Lists           -> to store all tasks
    2. Loops (while)   -> to keep showing the menu
    3. Conditionals    -> if/elif to choose what to do
    4. Functions       -> to keep code organized
==========================================================
"""

tasks = []   # This list will hold all our tasks


def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")
    else:
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")


def mark_done():
    view_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number to mark done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1] = tasks[num - 1] + " (Done)"
            print("Task marked as done!")
        else:
            print("Invalid number.")


def delete_task():
    view_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("Invalid number.")


# Main loop - keeps running until user chooses to exit
while True:
    show_menu()
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
