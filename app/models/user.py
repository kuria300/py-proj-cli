from app.models.project import Project

class Person:
    def __init__(self, name):
        self.name = name


class User(Person):
    _id_counter = 1
    def __init__(self, name, email ,projects=None):
        super().__init__(name)
        self._id = User._id_counter
        User._id_counter += 1
        self._email = email
        self.projects = projects or []

    @property
    def id(self):
        return self._id

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        self._email = value

    def add_project(self, project):
        self.projects.append(project)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"