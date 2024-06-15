class Task:
  def __init__(self, description, priority="low", due_date=None, is_completed=False):
    self.description = description
    self.priority = priority
    self.due_date = due_date
    self.is_completed = is_completed

  def __str__(self):
    status = "COMPLETED" if self.is_completed else "PENDING"
    return f"{status:<12} | {self.priority:<8} | {self.due_date:<12} | {self.description}"
