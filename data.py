import json

def load_tasks():
  try:
    with open("tasks.json", "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return []

def save_tasks(tasks):
  with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)
