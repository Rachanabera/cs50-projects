# project.py

def main():
    tasks = []
    while True:
        print("\nTO-DO LIST MANAGER")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            task = input("Enter task: ")
            add_task(tasks, task)
            print("Task added.")
        elif choice == "3":
            index = int(input("Enter task number to mark as complete: ")) - 1
            complete_task(tasks, index)
            print("Task marked complete.")
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
            print("Task deleted.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def add_task(tasks, task):
    tasks.append({"task": task, "done": False})

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

if __name__ == "__main__":
    main()
