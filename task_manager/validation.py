from datetime import datetime

def validate_task_title(title):
    """Validate the task title is not empty."""
    return isinstance(title, str) and len(title.strip()) > 0


def validate_task_description(description):
    """Validate the task description is not empty."""
    return isinstance(description, str) and len(description.strip()) > 0


def validate_due_date(due_date):
    """Validate the due date format is YYYY-MM-DD and not in the past."""
    if not isinstance(due_date, str):
        return False
    try:
        date_obj = datetime.strptime(due_date, "%Y-%m-%d")
        return date_obj.date() >= datetime.now().date()
    except ValueError:
        return False
