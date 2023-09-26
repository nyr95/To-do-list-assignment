from datetime import datetime
import sys


# Memento Pattern
class TaskMemento:
    def __init__(self, task):
        self.task = task

    def get_state(self):  # used to store the state of the list
        return self.task.get_state()


# Task class with Builder Pattern
class Task:
    def __init__(self, description, due_date=None):  #intialise task object
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def get_state(self):
        return {
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date
        }

    class Builder:   #used for building tasks
        def __init__(self, description):
            self.task = Task(description)

        def set_due_date(self, due_date):
            self.task.due_date = due_date
            return self

        def build(self):
            return self.task


# Task List Manager:used to manage various tasks
class TaskListManager:
    def __init__(self):
        self.tasks = []
        self.history = []

    def add_task(self, task):
        self.tasks.append(task)
        self.save_state()

    def mark_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                self.save_state()
                return

    def delete_task(self, description):
        self.tasks = [task for task in self.tasks if task.description != description]
        self.save_state()

    def view_tasks(self, filter_type='all'):
        if filter_type == 'completed':
            
            return [task for task in self.tasks if task.completed]
        elif filter_type == 'pending':
            return [task for task in self.tasks if not task.completed]
        elif filter_type == 'all':



            return self.tasks
        else:
            print("Invalid filter type. Use 'all', 'completed', or 'pending'.")
            return []

        if not tasks:
            print("No tasks found.")

    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            self.tasks = self.history[-1].get_state()

    def redo(self):
        if len(self.history) > 1:
            self.history.pop()
            self.tasks = self.history[-1].get_state()

    def save_state(self):
        self.history.append(TaskMemento(list(self.tasks)))


# User Interface
if __name__ == "__main__":
    task_list_manager = TaskListManager()

    try:
        while True:
            print("\nMenu:")
            print("1. Add Task")
            print("2. Mark Completed")
            print("3. Delete Task")
            print("4. View Tasks")
            print("5. Undo")
            print("6. Redo")
            print("7. Exit")
            print("please enter the choices as single digits from 1 to 7 ex:1")

            choice = input("Enter your choice: ")

            if choice == '1':
                description = input("Enter task description: ")
                due_date = input("Enter due date (YYYY-MM-DD) [Optional]: ")
                if due_date:
                    due_date = datetime.strptime(due_date, "%Y-%m-%d")
                    task = Task.Builder(description).set_due_date(due_date).build()
                    task_list_manager.add_task(task)
            elif choice == '2':
                    description = input("Enter task description to mark as completed: ")
                    task_list_manager.mark_completed(description)
            elif choice == '3':
                    description = input("Enter task description to delete: ")
                    task_list_manager.delete_task(description)
            elif choice == '4':
                    filter_type = input("Enter filter type (all/completed/pending): ")
                    tasks = task_list_manager.view_tasks(filter_type)
                    for task in tasks:
                        if task:
                            status = "Completed" if task.completed else "Pending"
                            due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "N/A"
                            print(f"{task.description} - {status}, Due: {due_date}")
                        else:
                             print("No tasks are present currently")
            elif choice == '5':
                    task_list_manager.undo()
            elif choice == '6':
                    task_list_manager.redo()
            elif choice == '7':
                    print("Exiting the To-Do List Manager. Goodbye!")
                    break
            else:
                    print("Invalid choice. Please select a valid option.")
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Exiting the To Do List . Goodbye!")
        sys.exit(0)
