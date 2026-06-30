import os
TODO_LIST = 'tasks.txt'


def load_tasks():
    if not os.path.exists(TODO_LIST):
        return []
    with open(TODO_LIST, "r") as f:
        return [line.strip() for line in f.readlines()]


def save_tasks(tasks):
    with open(TODO_LIST, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!\n")
        return

    print("\nYour tasks:\n")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ")
    if task.strip():
        tasks.append(task.strip())
        print("Task added!\n")
    else:
        print("Empty task not added.\n")


def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter Task Number to delete "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted: {removed}\n")
        else:
            print("Invalid number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    tasks = load_tasks()

    while True:
        print("=== To-Do List ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")
    if__name__ == "__main__":
    main()
