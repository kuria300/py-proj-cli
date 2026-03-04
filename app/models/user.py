from app.models.project import Project

class Person:
    def __init__(self, name):
        self.name = name


class User(Person):
    _id_counter = 1
    def __init__(self, name, email):
        super().__init__(name)
        self._id = User._id_counter
        User._id_counter += 1
        self._email = email
        self.projects = []

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

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects],
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(data["name"], data["email"])
        user._id = data["id"]
        cls._id_counter = max(cls._id_counter, user._id + 1)

        user.projects = [Project.from_dict(p) for p in data["projects"]]
        return user

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"