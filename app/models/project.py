from app.models.task import Task

class Project:
    _id_counter = 1
    def __init__(self, title, description="", due_date=None):
        self._id = Project._id_counter
        Project._id_counter += 1
        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    @property
    def id(self):
        return self._id

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "tasks": [t.to_dict() for t in self.tasks],
        }

    @classmethod
    def from_dict(cls, data):
        project = cls(data["title"], data["description"], data["due_date"])
        project._id = data["id"]
        cls._id_counter = max(cls._id_counter, project._id + 1)

        project.tasks = [Task.from_dict(t) for t in data["tasks"]]
        return project

    def __repr__(self):
        return f"Project(id={self.id}, title='{self.title}')"