from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

def add_task(title, description, due_date):
    """Create a validated task dictionary."""
    if not validate_task_title(title):
        print("Task title is required.")
        return None
    if not validate_task_description(description):
        print("Task description is required.")
        return None
    if not validate_due_date(due_date):
        print("Task due date must be in YYYY-MM-DD format and not in the past.")
        return None

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date,
        "completed": False
    }
    print("Task added successfully!")
    return task


def mark_task_as_complete(index, tasks):
    """Mark a task as complete by index."""
    try:
        index = int(index)
        if 0 <= index < len(tasks):
            if tasks[index]["completed"]:
                print("Task already completed")
                return False
            tasks[index]["completed"] = True
            print("Task marked as complete!")
            return True
        print("Invalid task number")
        return False
    except ValueError:
        print("Please enter a valid number")
        return False


def view_pending_tasks(tasks):
    """Display all pending tasks."""
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks!")
        return pending

    for index, task in enumerate(tasks):
        if not task["completed"]:
            print(f"{index}. {task['title']} | Due: {task['due_date']}")
            if task["description"]:
                print(f"  {task['description']}")
    return pending


def calculate_progress(tasks):
    """Display the completed task progress."""
    if not tasks:
        print("No tasks yet!")
        return 0
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    percent = int((completed / total) * 100)
    print(f"Progress: {completed}/{total} tasks completed ({percent}%)")
    return percent
