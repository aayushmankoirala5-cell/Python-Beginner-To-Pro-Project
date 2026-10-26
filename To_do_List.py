
#==============================================================
#==============================================================
"""
To-Do List App | Developed by Aayushman Koirala

This is a beginner to intermediate-level Python project
that helps practice functions, loops, lists, dictionaries,
conditional statements, and exception handling.

It allows users to add, view, complete, and delete tasks
through a simple command-line interface.
"""
#==============================================================
#==============================================================






#==============================================================
"""
You Can Update The code If you want To 

Please Make sure To summit the changes detail in the Comment 

Time Consumed to Do this Code 1:45 min 

Thank You 

"""
#==============================================================

def To_do_list_app(): #Main Application Function 

    tasks = []

    emoji = {
        "Add": "➕",
        "View": "👀",
        "Mark": "✅",
        "Delete": "⚠️",
        "Exit": "🙋‍♂️"
    }

    def line():
        print("=" * 40)

    def menu():
        line()
        print("===========MENU============")
        line()
        print(f"1. Add Task           : {emoji['Add']}")
        print(f"2. View Task          : {emoji['View']}")
        print(f"3. Mark Task As Done  : {emoji['Mark']}")
        print(f"4. Delete Task        : {emoji['Delete']}")
        print(f"5. Exit Task          : {emoji['Exit']}")
        line()

    def Add_task():

        while True:
            task = input("Add The New Task (Or type Exit to Stop): ").strip()

            if task.lower() == "exit":
                break





            

            elif task == "":
                print("Task Cannot Be Empty. Please Type Again.")
                continue

            else:
                tasks.append(task)
                print(f"Task Added Successfully {emoji['Mark']}")

    def View_task():

        line()
        print(f"Total Number of Tasks: {len(tasks)}")
        line()

        if len(tasks) == 0:
            print("No Tasks Available.")
            return

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        line()

    def Mark_task():

        while True:
            View_task()

            if len(tasks) == 0:
                break

            status_choice = input(
                "Which Task Number Do You Want to Mark? (Type Exit to Stop): "
            ).strip()

            if status_choice.lower() == "exit":
                break

            try:
                status_choice = int(status_choice)

                if 1 <= status_choice <= len(tasks):
                    index = status_choice - 1

                    if tasks[index].startswith(emoji['Mark']):
                        print("Task Is Already Marked.")

                    else:
                        tasks[index] = f"{emoji['Mark']} {tasks[index]}"
                        print(f"Task Marked Successfully {emoji['Mark']}")

                else:
                    print("Invalid Task Number.")

            except ValueError:
                print("Invalid Choice. Please Enter a Number.")

    def Delete_task():

        while True:
            View_task()

            if len(tasks) == 0:
                break

            Delete_choice = input(
                "Enter the Task Number You Want to Delete (Type Exit to Stop): "
            ).strip().lower()

            if Delete_choice == "exit":
                break

            try:
                Delete_choice = int(Delete_choice)

                if 1 <= Delete_choice <= len(tasks):
                    index = Delete_choice - 1

                    tasks.pop(index)
                    print(f"Task Has Been Deleted {emoji['Mark']}")

                else:
                    print("Invalid Task Number.")

            except ValueError:
                print("Please Choose a Valid Number.")

    def get_input():

        try:
            choice = int(input("Enter Your Choice: "))

        except ValueError:
            print(f"Look At Your Input Mate! {emoji['Delete']}")
            return True

        if choice == 1:
            Add_task()

        elif choice == 2:
            View_task()

        elif choice == 3:
            Mark_task()

        elif choice == 4:
            Delete_task()

        elif choice == 5:
            print("Program Terminated. Goodbye!")
            return False

        else:
            print("Invalid Choice. Please Choose 1-5.")

        return True

    def MainProgram():

        while True:
            menu()

            if get_input() == False:
                break

    MainProgram()

To_do_list_app()
