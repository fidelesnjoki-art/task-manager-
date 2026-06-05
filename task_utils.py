def add_task(title, description, due_date):
    """Add a new task to the tasks list"""
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    print("Task added successfully!")
    return task

def mark_task_as_complete(index, tasks):
    """Mark a task as complete by index"""
    try:
        index = int(index)
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print("Task already completed")
                return False
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True
        else:
            print("Invalid task number")
            return False
    except ValueError:
        print("Please enter a valid number")
        return False

def view_pending_tasks(tasks):
    """Display all pending tasks"""
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks!")
    else:
        for i, task in enumerate(tasks):
            if not task["completed"]:
                print(f"{i}. {task['title']} | Due: {task['due_date']}")
                if task["description"]:
                    print(f" {task['description']}")
    return pending

def view_progress(tasks):
    """Display progress of completed vs total tasks"""
    if not tasks:
        print("No tasks yet!")
        return
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    print(f"Progress: {completed}/{total} tasks completed")