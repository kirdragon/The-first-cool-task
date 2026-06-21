import json
from task import Task

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tasks], f, ensure_ascii=False, indent=4)

    def add_task(self, text):
        self.tasks.append(Task(text))
        self.save()

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            self.save()

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle()
            self.save()

    def get_tasks(self):
        return self.tasks