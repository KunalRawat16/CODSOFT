import os

class ToDoList:
    def __init__(self, filename='todo_list.txt'):
        """
        Initialize the ToDoList with a specified file for storage.
        If the file exists, load the existing tasks; otherwise, start with an empty list.

        :param filename: The file where tasks are stored.
        """
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """
        Load tasks from the specified file.

        :return: A list of tasks loaded from the file.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [line.strip() for line in file]
        return []

    def save_tasks(self):
        """
        Save the current list of tasks to the specified file.
        """
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        """
        Add a new task to the list and save it.

        :param task: The task to be added.
        """
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{task}" added.')

    def delete_task(self, task_number):
        """
        Delete a task by its number in the list.

        :param task_number: The position of the task in the list (1-based index).
        """
        try:
            task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f'Task "{task}" deleted.')
        except IndexError:
            print(f'Invalid task number: {task_number}.')

    def update_task(self, task_number, new_task):
        """
        Update an existing task by its number in the list.

        :param task_number: The position of the task in the list (1-based index).
        :param new_task: The new task description.
        """
        try:
            self.tasks[task_number - 1] = new_task
            self.save_tasks()
            print(f'Task {task_number} updated to "{new_task}".')
        except IndexError:
            print(f'Invalid task number: {task_number}.')

    def list_tasks(self):
        """
        List all tasks in the current to-do list.
        """
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

def display_menu():
    """
    Display the main menu options for the To-Do List application.
    """
    print("\nTo-Do List Application")
    print("1. List all tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

def main():
    """
    The main function to run the To-Do List application.
    It handles user input and interacts with the ToDoList class.
    """
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            todo_list.list_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                todo_list.update_task(task_number, new_task)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            try:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
