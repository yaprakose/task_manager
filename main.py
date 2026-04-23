from db import (
    create_table,
    add_task_db,
    list_tasks_db,
    get_task_by_id,
    complete_task_db,
    delete_task_db
)


def show_menu():
    print("\n--- TASK TRACKER ---")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    add_task_db(title)
    print("Task added successfully.")


def list_tasks():
    tasks = list_tasks_db()

    if not tasks:
        print("No tasks found.")
        return

    print("\n--- TASK LIST ---")
    for task in tasks:
        task_id, title, completed = task
        status = "[x]" if completed == 1 else "[ ]"
        print(f"{task_id}. {status} {title}")


def complete_task():
    tasks = list_tasks_db()

    if not tasks:
        print("No tasks to complete.")
        return

    list_tasks()

    try:
        task_id = int(input("Enter task id to mark as done: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = get_task_by_id(task_id)

    if task is None:
        print("Task not found.")
        return

    if task[2] == 1:
        print("Task is already completed.")
        return

    complete_task_db(task_id)
    print("Task marked as completed.")


def delete_task():
    tasks = list_tasks_db()

    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()

    try:
        task_id = int(input("Enter task id to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    task = get_task_by_id(task_id)

    if task is None:
        print("Task not found.")
        return

    delete_task_db(task_id)
    print("Task deleted successfully.")


def main():
    create_table()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()       


        