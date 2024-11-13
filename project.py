class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_task_id = 1  # Start task IDs from 1

    def add_task(self, title, description, assigned_to, due_date=None):
        task_id = self.next_task_id
        new_task = Task(task_id, title, description, assigned_to, due_date=due_date)
        self.tasks[task_id] = new_task
        self.next_task_id += 1
        print(f"Task '{title}' added successfully!")
    
    def update_task_status(self, task_id, status):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            if status in ['Pending', 'In Progress', 'Completed']:
                task.status = status
                print(f"Task ID {task_id} status updated to {status}.")
            else:
                print("Invalid status. Status must be 'Pending', 'In Progress', or 'Completed'.")
        else:
            print("Task not found!")

    def update_task_assigned_user(self, task_id, new_assigned_to):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            task.assigned_to = new_assigned_to
            print(f"Task ID {task_id} has been reassigned to {new_assigned_to}.")
        else:
            print("Task not found!")

    def view_task(self, task_id):
        if task_id in self.tasks:
            print(self.tasks[task_id])
        else:
            print("Task not found!")

    def list_all_tasks(self):
        if self.tasks:
            for task in self.tasks.values():
                print(task)
        else:
            print("No tasks found.")
def main():
    task_manager = TaskManager()
    
    # Add tasks
    task_manager.add_task("Complete project report", "Write and submit the final project report", "Alice", "2024-11-20")
    task_manager.add_task("Review PR", "Review the pull request for the new feature", "Bob", "2024-11-18")
    task_manager.add_task("Prepare presentation", "Create a presentation for the meeting", "Alice", "2024-11-15")

    # List all tasks
    print("\nList of all tasks:")
    task_manager.list_all_tasks()

    # View a specific task
    print("\nView task with ID 2:")
    task_manager.view_task(2)

    # Update task status
    print("\nUpdating task with ID 2 status to 'In Progress':")
    task_manager.update_task_status(2, "In Progress")
    task_manager.view_task(2)

    # Reassign task
    print("\nReassigning task with ID 1 to 'Charlie':")
    task_manager.update_task_assigned_user(1, "Charlie")
    task_manager.view_task(1)

    # Mark task as completed
    print("\nUpdating task with ID 3 status to 'Completed':")
    task_manager.update_task_status(3, "Completed")
    task_manager.view_task(3)

    # List all tasks after updates
    print("\nList of all tasks after updates:")
    task_manager.list_all_tasks()

if __name__ == "__main__":
    main()
