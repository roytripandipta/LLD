"""
user can view, order, cancel, add, track food from a restaurant/multiple restaurant

"""
from abc import ABC, abstractmethod
from typing import List

"""
User - FactoryMethodPattern 
Order - ObserverPattern 
PaymentProcessing - StrategyPattern 
PlaceOrder - FacadePattern
"""


# Singleton Pattern: connect to db
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._connect_to_db()

        return cls._instance

    @staticmethod
    def _connect_to_db():
        return "Database Connected"


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass


class Customer(User):
    def get_role(self):
        return "Customer"


class RestaurantOwner(User):
    def get_role(self):
        return "Restaurant Owner"


# Factory Method: UserFactory
class UserFactory:
    @staticmethod
    def create_user(user_type: str, name: str):
        if user_type == "Customer":
            return Customer(name)

        elif user_type == "RestaurantOwner":
            return RestaurantOwner(name)

        else:
            print(f"Unknown User")
            return None


# MenuItem
class MenuItem(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass


class FoodItem(MenuItem):
    def get_description(self):
        return f"{self.name} - {self.price}"


# Restaurant Class
class Restaurant:
    def __init__(self, name: str, owner: RestaurantOwner):
        self.name = name
        self.owner = owner
        self.menu: List[MenuItem] = []

    def add_menu_item(self, item: FoodItem):
        self.menu.append(item)


# OrderStatusObserver
class OrderStatusObserver(ABC):
    @abstractmethod
    def update(self, order):
        pass


class UserInterface(OrderStatusObserver):
    def update(self, order):
        print(f"User Interface: Order {order.id} status updated to {order.status}")


class DeliverySystem(OrderStatusObserver):
    def update(self, order):
        print(f"Delivery System: Order {order.id} status updated to {order.status}")


# ObserverPattern
class Order:
    _id_counter = 0

    def __init__(self, user: Customer, restaurant: Restaurant, items: List[MenuItem]):
        self.id = Order._id_counter + 1
        self.user = user
        self.restaurant = restaurant
        self.items = items
        self.status = "New"
        self.observers: List[OrderStatusObserver] = []

    def add_observer(self, observer: OrderStatusObserver):
        self.observers.append(observer)

    def update_status(self, status):
        self.status = status
        self._notify_observers()

    def _notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    @property
    def total_cost(self):
        return sum(item.price for item in self.items)


# OrderFactory
class OrderFactory:
    @staticmethod
    def create_order(user: Customer, restaurant: Restaurant, items: List[MenuItem]) -> Order:
        return Order(user, restaurant, items)


# PaymentStrategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using UPI")


class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process_payment(self, amount: float):
        self.strategy.pay(amount)


# Facade Pattern
class OrderProcessingFacade:
    def __init__(self):
        self.db = DatabaseConnection()
        self.user_interface = UserInterface()
        self.delivery_system = DeliverySystem()

    def place_order(self, user: Customer, restaurant: Restaurant, items: List[MenuItem],
                    payment_method: PaymentStrategy) -> Order:
        order = OrderFactory.create_order(user, restaurant, items)
        order.add_observer(self.user_interface)
        order.add_observer(self.delivery_system)

        print(f"Placing order {order.id} for {user.name}")

        order.update_status("processing")
        payment_processor = PaymentProcessor(payment_method)
        payment_processor.process_payment(order.total_cost)
        order.update_status("completed")


if __name__ == "__main__":
    db = DatabaseConnection()
    print(db.connection)

    customer = UserFactory.create_user("Customer", "Alice")
    owner = UserFactory.create_user("RestaurantOwner", "Tripan")

    restaurant = Restaurant("Pizza Palace", owner)
    pizza = FoodItem("Pizza", 100)
    burger = FoodItem("Burger", 50)

    restaurant.add_menu_item(pizza)
    restaurant.add_menu_item(burger)

    order = OrderProcessingFacade()
    order.place_order(customer, restaurant, [pizza, burger], CreditCardPayment())
