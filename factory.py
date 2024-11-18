from enum import Enum


class Permissions(Enum):
    BASIC = "Basic"
    ADVANCED = "Advanced"
    ADMIN = "Admin"


class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Permissions: {self.permissions.value}"


class Student(User):
    def __init__(self, name):
        super().__init__(name, Permissions.BASIC)


class Teacher(User):
    def __init__(self, name):
        super().__init__(name, Permissions.ADVANCED)


class Librarian(User):
    def __init__(self, name):
        super().__init__(name, Permissions.ADMIN)


class UserFactory:
    @staticmethod
    def create_user(user_type, name):
        if user_type == "student":
            return Student(name)
        elif user_type == "teacher":
            return Teacher(name)
        elif user_type == "librarian":
            return Librarian(name)
        else:
            raise ValueError(f"Unknown user type: {user_type}")
