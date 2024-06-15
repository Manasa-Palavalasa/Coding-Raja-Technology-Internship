from tasks import Task
from data import load_tasks, save_tasks

def main():
  tasks = load_tasks()

  while True:
    print("\nToDo List")
    print("-" * 50)
    print("1. List Tasks")
    print("2. Add Task")
    print("3. Mark Task Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
      display_tasks(tasks)
    elif choice == "2":
      add_task(tasks)
    elif choice == "3":
      mark_complete(tasks)
    elif choice == "4":
      save_tasks(tasks)
      print("Exiting...")
      break
    else:
      print("Invalid choice.")

def display_tasks(tasks):
  if not tasks:
    print("No tasks in the list.")
  else:
    print("{:<12} | {:<8} | {:<12} | {:<40}".format("Status", "Priority", "Due Date", "Description"))
    print("-" * 80)
    for task in tasks:
      print(task)

def add_task(tasks):
  description = input("Enter task description: ")
  priority = input("Enter priority (high, medium, low): ").lower()
  due_date = input("Enter due date (YYYY-MM-DD) (optional): ")
  tasks.append(Task(description, priority, due_date))
  print("Task added successfully!")

def mark_complete(tasks):
  display_tasks(tasks)
  if not tasks:
    return

  index = int(input("Enter the index of the task to mark complete: ")) - 1
  if index < 0 or index >= len(tasks):
    print("Invalid index.")
    return
  tasks[index].is_completed = True
  print("Task marked complete!")

if __name__ == "__main__":
  main()
