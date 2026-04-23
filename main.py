import json 
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return[]

    with open(FILE_NAME,"r",encoding="utf-8") as file:
        return json.load(file)
def save_tasks(tasks):
    with open(FILE_NAME,"w",encoding="utf-8") as file:
        json.dump(tasks,file,indent=4)


def show_menu():
    print("\nTask Tracker")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")  
    print("5. Exit")    


def main():
    tasks= load_tasks()


    while True:
        show_menu()

        def get_next_id(tasks):
            if not tasks:
                return 1
            
            max_id = max(task["id"] for task in tasks)
            return max_id +1

        def add_task(tasks):
            title = input ("Enter task title:").strip()

            if not title:
                print("Task title cannot be empty.")
                return

            new_task = {
                "id": get_next_id(tasks),
                "title": title,
                "completed": False
            }    

            tasks.append(new_task)
            print(f"Task '{title}' added successfully.")









        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            pass    
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()                  


        