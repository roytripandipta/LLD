# Design Patterns in Software Development

## 1. Observer Pattern
- **Purpose**: The Observer pattern is used to establish a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- **Key Components**:
  - **Subject**: The object being observed. It maintains a list of observers and notifies them of any state changes.
  - **Observer**: The objects that need to be notified when the subject changes state. These observers implement an interface that allows the subject to notify them of changes.
- **Use Case**: When an object’s state changes, and you want other objects to react or update themselves based on that change. For example, in a real-time application where UI components need to reflect changes in data immediately.
- **Example**: A stock market application where multiple screens (observers) display stock prices. When the price of a stock changes (subject), all screens (observers) are notified to update the displayed price.

## 2. Strategy Pattern
- **Purpose**: The Strategy pattern is used to define a family of algorithms, encapsulate each one, and make them interchangeable. It allows the algorithm to be selected at runtime.
- **Key Components**:
  - **Context**: The object that is using a strategy. It maintains a reference to a strategy object.
  - **Strategy Interface**: An interface that all concrete strategies must implement.
  - **Concrete Strategies**: Different implementations of the strategy interface, each representing a different algorithm or behavior.
- **Use Case**: When you have multiple algorithms or behaviors that a class should perform, and you want to choose which one to use dynamically at runtime.
- **Example**: A payment processing system where the strategy could be different payment methods (credit card, PayPal, UPI). The payment processor (context) uses the strategy interface to call the appropriate payment method (concrete strategy).

## 3. Factory Method Pattern
- **Purpose**: The Factory Method pattern is used to define an interface for creating an object, but allows subclasses to alter the type of objects that will be created. It delegates the instantiation process to subclasses.
- **Key Components**:
  - **Creator (Factory)**: A class that declares the factory method, which returns an object of a product type.
  - **Concrete Creator**: Subclasses that implement the factory method to return a specific product.
  - **Product Interface**: The interface or abstract class that defines the object created by the factory method.
  - **Concrete Product**: The actual product created by the factory method, which implements the product interface.
- **Use Case**: When a class cannot anticipate the type of objects it needs to create, or when you want to delegate the responsibility of instantiating objects to subclasses.
- **Example**: A document editor that can create different types of documents (e.g., Word, PDF, Text). Each type of document is created by a different factory method in the document creator class.

## Primary Differences

### Observer Pattern:
- **Purpose**: Manages state changes and notifications. It’s about communication between objects (one-to-many relationship).
- **When to Use**: Use it when you need multiple objects to react to changes in another object’s state.

### Strategy Pattern:
- **Purpose**: Encapsulates interchangeable behaviors or algorithms. It’s about selecting a behavior or algorithm at runtime (one-to-one relationship).
- **When to Use**: Use it when a class has multiple ways of performing an action and the way needs to be selected dynamically.

### Factory Method Pattern:
- **Purpose**: Provides a way to instantiate objects, allowing subclasses to determine the specific type of the created object. It’s about object creation and decoupling the client code from the specific classes.
- **When to Use**: Use it when the exact type of the object to be created is not known until runtime, or you want to centralize object creation to maintain flexibility.

Each pattern addresses a different design problem: communication between objects (Observer), dynamic behavior selection (Strategy), and flexible object creation (Factory Method).

## 1. Composite Pattern
- **Purpose**: The Composite pattern is used to treat individual objects and compositions of objects uniformly. It allows you to compose objects into tree structures to represent part-whole hierarchies. This pattern lets clients treat individual objects and compositions of objects uniformly.
- **Key Components**:
  - **Component**: The abstract class or interface that defines the common operations for both simple and complex objects.
  - **Leaf**: Represents the simplest form of an object in the hierarchy (an object with no children). It implements the Component interface.
  - **Composite**: A class that represents a complex object (a container of other components). It implements the Component interface and contains child components, which could be either Leafs or other Composites.
- **Use Case**: When you need to work with tree-like structures or hierarchies where individual elements and groups of elements need to be treated in the same way.
- **Example**: A graphical user interface (GUI) framework where buttons, text fields, and panels can all be treated as components. A panel (Composite) can contain buttons and text fields (Leafs), and you can perform operations on the panel as a whole, just as you would on an individual button.

## 2. Facade Pattern
- **Purpose**: The Facade pattern is used to provide a simplified interface to a complex subsystem, making it easier for clients to interact with the system. It hides the complexities of the system and provides a unified interface to the client.
- **Key Components**:
  - **Facade**: The class that provides a simple, unified interface to the complex subsystem. It delegates client requests to the appropriate subsystems.
  - **Subsystem Classes**: The classes that perform the actual work. These classes implement the subsystem's functionality and are hidden behind the facade.
- **Use Case**: When you have a complex system with many interacting components, and you want to provide a simple interface to the client to interact with the system without exposing the complexities.
- **Example**: A home theater system with many components like a DVD player, projector, sound system, and lights. The Facade might be a "HomeTheaterFacade" class that provides a simple method like `watchMovie()`, which internally turns on the DVD player, sets up the projector, dims the lights, and turns on the sound system.

## Primary Differences

### Composite Pattern:
- **Purpose**: Manages part-whole hierarchies and allows individual objects and their compositions to be treated uniformly. It’s about combining objects into tree structures and treating them as one.
- **When to Use**: Use it when you need to represent a tree structure where individual objects and groups of objects should be treated the same way.

### Facade Pattern:
- **Purpose**: Simplifies the interface of a complex system. It’s about providing a simplified interface to a set of complex subsystems.
- **When to Use**: Use it when you need to simplify interaction with a complex system by providing a single entry point or interface.

## Example Scenarios

### Composite Pattern:
- **Scenario**: You’re developing a document editor where documents can contain text elements, images, and tables. You want to allow operations like rendering and printing to be performed on both individual elements and entire documents. The Composite pattern lets you treat an entire document (a composition) just like a single text element (a leaf).

### Facade Pattern:
- **Scenario**: You’re building a complex e-commerce system with subsystems for inventory management, payment processing, and order tracking. Clients need a way to place orders without dealing with the details of each subsystem. The Facade pattern can provide a simple `placeOrder()` method that handles all the internal interactions.

## Summary
- The **Composite Pattern** is focused on the structure of objects, enabling you to work with tree structures and treat individual objects and groups uniformly.
- The **Facade Pattern** is focused on simplifying the interaction with a complex system by providing a unified and easier-to-use interface.
- These patterns solve different problems—Composite for managing part-whole hierarchies and Facade for simplifying complex systems.

