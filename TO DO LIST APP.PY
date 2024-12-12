def display_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def get_user_choice():
    try:
        choice = int(input("Please select an option (1-5): "))
        if choice not in range(1, 6):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        return None

tasks = []

def add_task():
    task = input("Enter the task title: ")
    tasks.append({"title": task, "status": "Incomplete"})
    print(f"Task '{task}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {task['status']}")

def mark_task_complete():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if task_num < 1 or task_num > len(tasks):
            raise ValueError
        tasks[task_num - 1]["status"] = "Complete"
        print(f"Task '{tasks[task_num - 1]['title']}' marked as complete.")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if task_num < 1 or task_num > len(tasks):
            raise ValueError
        removed_task = tasks.pop(task_num - 1)
        print(f"Task '{removed_task['title']}' deleted.")
    except ValueError:
        print("Invalid input! Please enter a valid task number.")  
def main():
    while True:
        display_menu()
        choice = get_user_choice()
        if choice is None:
           "continue" 
        elif choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_complete()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Thank you for using the To-Do List App!")
            break

if __name__ == "__main__":
    main()

        
