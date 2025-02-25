todo_list = []

def display_tasks():
    if len(todo_list) == 0:
        print("No tasks to display.")
    else:
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    todo_list.append(task)
    print("Task added!")

def update_task():
    display_tasks()
    task_num = int(input("Enter the task number to update: "))
    if 1 <= task_num <= len(todo_list):
        new_task = input("Enter the updated task: ")
        todo_list[task_num - 1] = new_task
        print("Task updated!")
    else:
        print("Invalid task number!")

def remove_task():
    display_tasks()
    task_num = int(input("Enter the task number to remove: "))
    if 1 <= task_num <= len(todo_list):
        todo_list.pop(task_num - 1)
        print("Task removed!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Remove a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
