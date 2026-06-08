# =====================================
#       TO-DO TASK MANAGEMENT SYSTEM
#          Developed by Zahid
# =====================================


tasks = []


def show_menu():
    print("\n" + "=" * 45)
    print("        TO-DO TASK MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    print("=" * 45)



def add_task():
    task = input("Enter your task: ")

    tasks.append(task)

    print("\n Task Added Successfully!")


def view_tasks():

    print("\n========== YOUR TASKS ==========")

    if len(tasks) == 0:
        print("No tasks available.")

    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")



def delete_task():

    view_tasks()

    if len(tasks) > 0:

        number = int(input("\nEnter task number to delete: "))

        if number <= len(tasks):
            removed = tasks.pop(number - 1)

            print(f"\n Task Removed: {removed}")

        else:
            print("Invalid task number!")



while True:

    show_menu()

    choice = input("Enter your choice: ")


    if choice == "1":

        add_task()


    elif choice == "2":

        view_tasks()


    elif choice == "3":

        delete_task()


    elif choice == "4":

        print("\nProgram Closed")
        print("Thank you for using Task Manager!")

        break


    else:

        print("\nInvalid Choice! Try Again.")
