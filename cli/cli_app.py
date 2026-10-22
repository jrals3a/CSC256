# cli/cli_app.py
from app.services.task_storage import load_tasks, save_tasks


def add_task() -> None:
    tasks = load_tasks()
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    # Why max() instead of len() + 1?
    # Sprint 1 used: task_id = len(tasks) + 1
    # That breaks with persistence! Example:
    #   tasks = [id:1, id:2, id:3] → delete id:2
    #   tasks = [id:1, id:3]       → len = 2, next id = 3 → COLLISION! ❌
    # max() finds the highest existing ID and adds 1 — safe even with gaps:
    #   tasks = [id:1, id:3]       → max = 3, next id = 4 → Safe! ✅
    task_id = max([task["id"] for task in tasks], default=0) + 1
    task = {"id": task_id, "title": title, "description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def view_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - {task['description']}")


def main() -> None:
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Quit")
        choice = input("Select: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
