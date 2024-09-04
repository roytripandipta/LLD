"""
Design a service to view/add/remove viewers of a document (like the feature in google doc)

class description:

Document: to add, remove, view, add_observer, notify_viewers, remove_observers

DocumentFacade: only to expose the required method to user like add, view, remove

DocumentService: to contains all the documents of a user (Singleton pattern)

Command: to execute the commands like add, remove,
"""

from abc import ABC, abstractmethod


class DocumentService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DocumentService, cls).__new__(cls)
            cls._instance._documents = {}

        return cls._instance

    def create_document(self, doc_id, content):
        if doc_id not in self._documents:
            self._documents[doc_id] = Document(doc_id, content)

    def get_document(self, doc_id):
        return self._documents.get(doc_id)


class Document:
    def __init__(self, doc_id, content):
        self.doc_id = doc_id
        self.content = content
        self._viewers = set()
        self._observers = set()

    def add_viewers(self, viewer):
        self._viewers.add(viewer)
        self.notify_observers(f"Viewer {viewer} added")

    def remove_viewers(self, viewer):
        self._viewers.remove(viewer)
        self.notify_observers(f"Viewer {viewer} removed")

    def register_observer(self, observer):
        self._observers.add(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def get_viewers(self):
        return list(self._viewers)


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Viewer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"Notification for {self.name}: {message}")

    def __repr__(self):
        return self.name


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddViewerCommand(Command):
    def __init__(self, document, viewer):
        self.document = document
        self.viewer = viewer

    def execute(self):
        self.document.add_viewers(self.viewer)
        self.document.register_observer(self.viewer)


class RemoveViewerCommand(Command):
    def __init__(self, document, viewer):
        self.document = document
        self.viewer = viewer

    def execute(self):
        self.document.remove_viewers(self.viewer)
        self.document.remove_observer(self.viewer)


class DocumentFacade:
    def __init__(self):
        self.doc_service = DocumentService()

    def add_viewer(self, doc_id, viewer):
        document = self.doc_service.get_document(doc_id)

        if document:
            command = AddViewerCommand(document, viewer)
            command.execute()

    def remove_viewer(self, doc_id, viewer):
        document = self.doc_service.get_document(doc_id)

        if document:
            command = RemoveViewerCommand(document, viewer)
            command.execute()

    def view_viewers(self, doc_id):
        document = self.doc_service.get_document(doc_id)

        if document:
            return document.get_viewers()

        return []


if __name__ == "__main__":
    doc_facade = DocumentFacade()

    doc_facade.doc_service.create_document("doc_1", "Hello World!")

    # create viewers
    Alice = Viewer("Alice")
    Bob = Viewer("Bob")

    doc_facade.add_viewer("doc_1", Alice)
    doc_facade.add_viewer("doc_1", Bob)

    # View current viewers
    print("Current viewers:", doc_facade.view_viewers("doc_1"))

    # Remove a viewer
    doc_facade.remove_viewer("doc_1", Bob)

    # View current viewers again
    print("Current viewers after removal:", doc_facade.view_viewers("doc_1"))




