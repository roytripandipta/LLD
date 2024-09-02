"""
Problem statement:

Design a system like Jira. It should have the following functionalities :

User should be able to create Task of type Story, Feature, Bugs. Each can have their own status.
Stories can further have subtracts.
Should be able to change the status of any task.
User should be able to create any sprint. Should be able to add any task to sprint and remove from it.
User should be able to print
Delayed task
Sprint details
Tasks assigned to the user
"""

"""
TaskFactory - create tasks of different types 
SprintManager - manage sprint of various tasks 
Task - will have assignee, status (set and update), task details, 

Flow - 

you should be able to create a sprint, add tasks (feature, bug, story) in the sprint, change status 
"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    TODO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


class Task(ABC):
    def __init__(self, name, assignee):
        self.name = name
        self.status = TaskStatus.TODO
        self.assignee = assignee
        self.create_at = datetime.now()

    def change_status(self, status: TaskStatus):
        print(f"Changing status from  {self.status} to {status}")
        self.status = status

    @abstractmethod
    def print_details(self):
        pass


class TaskFactory:
    @staticmethod
    def create_task(task_type, name, assignee=None):
        if task_type == "Story":
            return Story(name, assignee)

        elif task_type == "Feature":
            return Feature(name, assignee)

        elif task_type == "Bug":
            return Bug(name, assignee)

        else:
            print(f"Unknown task name")


class Feature(Task):
    def print_details(self):
        print(f"Feature: {self.name}, Status: {self.status.name}, Assignee: {self.assignee}")


class Bug(Task):
    def print_details(self):
        print(f"Feature: {self.name}, Status: {self.status.name}, Assignee: {self.assignee}")


class Story(Task):
    def __init__(self, name, assignee=None):
        super().__init__(name, assignee)
        self.subtasks = []

    def add_subtask(self, task: Task):
        self.subtasks.append(task)

    def print_details(self):
        print(f"Feature: {self.name}, Status: {self.status.name}, Assignee: {self.assignee}")


class Sprint:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, name):
        self.tasks.remove(name)

    def print_details(self):
        for task in self.tasks:
            task.print_details()


class SprintManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SprintManager, cls).__new__(cls)
            cls._instance.sprints = []

        return cls._instance

    def create_sprint(self, name):
        sprint = Sprint(name)
        self.sprints.append(sprint)
        return sprint

    def print_delayed_task(self):
        for sprint in self.sprints:
            for task in sprint.tasks:
                if task.status != TaskStatus.DONE:
                    print(f"Task: {task.name}, Status: {task.status.name}")

    def print_sprint_details(self):
        for sprint in self.sprints:
            sprint.print_details()

    def print_user_tasks(self, assignee):
        for sprint in self.sprints:
            for task in sprint.tasks:
                if task.assignee == assignee:
                    task.print_details()


story = TaskFactory.create_task("Story", "User Authentication")
feature = TaskFactory.create_task("Feature", "Login Page", assignee="Alice")
bug = TaskFactory.create_task("Bug", "Fix Login Button", assignee="Bob")

# Adding subtasks to a story
subtask1 = TaskFactory.create_task("Feature", "Design Login Form", assignee="Charlie")
subtask2 = TaskFactory.create_task("Feature", "Implement Login Logic", assignee="Dave")
story.add_subtask(subtask1)
story.add_subtask(subtask2)

# Creating a Sprint and adding tasks
sprint_manager = SprintManager()
sprint = sprint_manager.create_sprint("Sprint 1")
sprint.add_task(story)
sprint.add_task(feature)
sprint.add_task(bug)

# Changing status of a task
bug.change_status(TaskStatus.IN_PROGRESS)

# Print Sprint details
sprint_manager.print_sprint_details()

# Print delayed tasks
sprint_manager.print_delayed_task()

# Print tasks assigned to a user
sprint_manager.print_user_tasks("Bob")


