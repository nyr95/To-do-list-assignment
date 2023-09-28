class TaskBuilder:
    def __init__(self, description):
        self.task = Task()
        self.task.description = description

    def with_due_date(self, due_date):
        self.task.due_date = due_date
        return self

    def build(self):
        return self.task

class Task:
    def __init__(self):
        self.description = ""
        self.due_date = None
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"

class TaskMemento:
    def __init__(self, tasks):
        self.tasks = tasks

class TaskListManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        if task.description:
            self.tasks.append(task)
            self.save_state()
        else:
            print("Error: Task description cannot be empty.")

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                self.save_state()
                return
        print(f"Error: Task '{description}' not found.")

    def delete_task(self, description):
        found = False
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                found = True
                break
        if found:
            self.save_state()
        else:
            print(f"Error: Task '{description}' not found.")

    def save_state(self):
        self.history.append(TaskMemento(list(self.tasks)))

    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            previous_state = self.history[-1]
            self.tasks = previous_state.tasks
        else:
            print("Error: Cannot undo further.")

    def display_tasks(self, filter_type=None):
        if filter_type == "completed":
            filtered_tasks = [task for task in self.tasks if task.completed]
        elif filter_type == "pending":
            filtered_tasks = [task for task in self.tasks if not task.completed]
        else:
            filtered_tasks = self.tasks

        if not filtered_tasks:
            print("No tasks to display.")
        else:
            for task in filtered_tasks:
                print(task)

def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nExiting the To-Do List Manager. Goodbye!")
        exit()

def print_menu():
    print("\n=== To-Do List Manager Menu ===")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Delete Task")
    print("4. View All Tasks")
    print("5. View Completed Tasks")
    print("6. View Pending Tasks")
    print("7. Undo")
    print("8. Exit")

def main():
    manager = TaskListManager()
    
    while True:
        try:
            print_menu()
            choice = safe_input("Enter your choice: ")
        
            if choice == "1":
                description = safe_input("Enter task description: ")
                due_date = safe_input("Enter due date (optional): ")
                task_builder = TaskBuilder(description)
                if due_date:
                    task_builder.with_due_date(due_date)
                task = task_builder.build()
                manager.add_task(task)
            
            elif choice == "2":
                description = safe_input("Enter the task you completed: ")
                manager.mark_completed(description)
            
            elif choice == "3":
                description = safe_input("Enter the task you want to delete: ")
                manager.delete_task(description)
            
            elif choice == "4":
                manager.display_tasks()
            
            elif choice == "5":
                manager.display_tasks("completed")
            
            elif choice == "6":
                manager.display_tasks("pending")
            
            elif choice == "7":
                manager.undo()
            
            elif choice == "8":
                print("Exiting the To-Do List Manager. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

