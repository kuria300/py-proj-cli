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

    def __repr__(self):
        return f"Project(id={self.id}, title='{self.title}')"