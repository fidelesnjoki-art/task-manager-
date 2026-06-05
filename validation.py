from datetime import datetime

def validate_date(date_string):
    """Validate date format is YYYY-MM-DD and is not in the past"""
    try:
        date_obj = datetime.strptime(date_string, "%Y-%m-%d")
        if date_obj.date() < datetime.now().date():
            return False
        return True
    except ValueError:
        return False

def validate_title(title):
    """Validate title is not empty"""
    return len(title.strip()) > 0