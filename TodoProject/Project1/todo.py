# =====================================
#       TO-DO TASK MANAGEMENT SYSTEM
#          Developed by Zahid
# =====================================

import json
from datetime import datetime


FILE = "tasks.json"


# Load existing tasks
def load_tasks():
    try:
        with open(FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


# Save tasks
def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


def show_menu():

    print("\n" + "=" * 50)
    print("       TO-DO TASK MANAGEMENT SYSTEM")
    print("              Developed by Zahid")
    print("=" * 50)

    print("""
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Search Task
6. Exit
""")

    print("=" * 50)



def add_task():

    title = input("Enter task name: ").strip()


    if title == "":
        print("Task cannot be empty!")
        return


    # duplicate check
    for task in tasks:

        if task["title"].lower() == title.lower():

            print("Task already exists!")
            return


    new_task = {

        "id": len(tasks)+1,

        "title": title,

        "status": "Pending",

        "date": datetime.now().strftime("%Y-%m-%d %H:%M")

    }


    tasks.append(new_task)

    save_tasks()


    print("\nTask Added Successfully!")




def view_tasks():


    print("\n========== YOUR TASKS ==========")


    if not tasks:

        print("No tasks available.")
        return


    for task in tasks:

        print(
f"""
ID: {task['id']}
Task: {task['title']}
Status: {task['status']}
Created: {task['date']}
-------------------------
"""
        )





def complete_task():

    view_tasks()


    if tasks:

        try:

            task_id = int(input("Enter task ID to complete: "))


            for task in tasks:

                if task["id"] == task_id:

                    task["status"] = "Completed"

                    save_tasks()

                    print("Task Completed!")

                    return


            print("Task not found!")


        except ValueError:

            print("Enter valid number!")





def delete_task():

    view_tasks()


    if tasks:

        try:

            task_id = int(input("Enter task ID to delete: "))


            for task in tasks:


                if task["id"] == task_id:


                    tasks.remove(task)

                    save_tasks()


                    print("Task Deleted!")

                    return


            print("Task not found!")


        except ValueError:

            print("Invalid input!")





def search_task():


    keyword = input("Search task: ").lower()


    found = False


    for task in tasks:


        if keyword in task["title"].lower():


            print(task)

            found = True


    if not found:

        print("No matching task found.")






while True:


    show_menu()


    choice = input("Enter choice: ")



    if choice == "1":

        add_task()


    elif choice == "2":

        view_tasks()


    elif choice == "3":

        complete_task()


    elif choice == "4":

        delete_task()


    elif choice == "5":

        search_task()


    elif choice == "6":

        print("\nProgram Closed")
        print("Thank you for using Task Manager!")

        break


    else:

        print("Invalid Choice!")
