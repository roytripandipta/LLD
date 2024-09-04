# Design Patterns Explanation

## Singleton Pattern:
The `DocumentService` class ensures that there is only one instance of the document management system. This is useful for maintaining a global state of documents and their viewers.

## Observer Pattern:
The `Document` class holds a list of observers (viewers), and when the document’s viewers are changed (adding or removing), it notifies all observers (viewers). This ensures that viewers can be alerted when any document-sharing changes occur.

## Facade Pattern:
The `DocumentFacade` class provides a simple interface to the client, exposing only the essential functions for adding, removing, and viewing document viewers. This hides the complexity of managing the document service and command execution.

## Command Pattern:
We encapsulate actions like adding and removing viewers into command classes (`AddViewerCommand` and `RemoveViewerCommand`). This makes it easy to extend or undo/redo operations in the future by manipulating commands.

# How it works:
1. First, we create a document using the `DocumentService`.
2. Users (viewers) can be added or removed to/from the document.
3. Notifications are sent to viewers when they are added or removed, thanks to the observer pattern.
4. The document service follows the singleton pattern to ensure global management.

# Conclusion:
This design is flexible and can be expanded with additional features, such as different types of permissions (view, edit, comment) or undo/redo functionalities for sharing operations.
