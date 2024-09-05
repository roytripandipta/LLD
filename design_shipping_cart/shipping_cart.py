"""
Write code that will be used by a Shopping cart service to enforce rules on the order

eg. Offer free 2 day shipping on orders > $35 if customer is not a prime member
Offer free 2 day shipping on all orders if customer is a prime member
Offer free 1 day shipping for order that are > $125 Offer free 2 hour shipping for prime customer that have > $25 and the items are grocery items

Make this extensible to add other rules in the future Apply a 10% discount if an item has been marked for subscribe and save
"""

"""
to process offer and discount, use chain of responsibility, if one offer is applied, return the offer and do not apply another offer

to create rules for offer and discount, use strategy pattern
"""

from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def get_shipping_offer(self, order):
        pass


class Free2DayShippingNonPrime(ShippingStrategy):
    def get_shipping_offer(self, order):
        if not order.customer.is_prime and order.total > 35:
            return "Free 2-Day Shipping"
        return None


class Free2DayShippingPrime(ShippingStrategy):
    def get_shipping_offer(self, order):
        if order.customer.is_prime:
            return "Free 2-Day Shipping"
        return None


class Free1DayShipping(ShippingStrategy):
    def get_shipping_offer(self, order):
        if order.total > 125:
            return "Free 1-Day Shipping"
        return None


class Free2HourGroceryPrime(ShippingStrategy):
    def get_shipping_offer(self, order):
        if order.customer.is_prime and order.total > 25 and order.contains_groceries:
            return "Free 2-Hour Grocery Shipping"
        return None


class ShippingRuleChain:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule: ShippingStrategy):
        self.rules.append(rule)

    def get_best_shipping_offer(self, order):
        for rule in self.rules:
            offer = rule.get_shipping_offer(order)
            if offer:
                return offer

        return "Standard Shipping"


class DiscountStrategy:
    @abstractmethod
    def apply_discount(self, order):
        pass


class SubscribeAndSaveDiscount(DiscountStrategy):
    def apply_discount(self, order):
        for item in order.items:
            if item.is_subscribe_and_save:
                item.price = item.price * 0.90  # Apply 10% discount


class DiscountRuleChain:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def apply_discounts(self, order):
        for rule in self.rules:
            rule.apply_discount(order)


class Customer:
    def __init__(self, is_prime):
        self.is_prime = is_prime


class Item:
    def __init__(self, name, price, is_subscribe_and_save=False, is_grocery=False):
        self.name = name
        self.price = price
        self.is_subscribe_and_save = is_subscribe_and_save
        self.is_grocery = is_grocery


class Order:
    def __init__(self, customer, items):
        self.customer = customer
        self.items = items
        self.total_price = sum(item.price for item in items)
        self.contains_groceries = any(item.is_grocery for item in items)


if __name__ == "__main__":
    Alice = Customer(is_prime=True)

    items = [
        Item("Laptop", 1500),
        Item("Bananas", 5, is_grocery=True),
        Item("Shampoo", 8, is_subscribe_and_save=True)
    ]

    order = Order(Alice, items)

    # Setup shipping rules
    shipping_rule_chain = ShippingRuleChain()
    shipping_rule_chain.add_rule(Free2DayShippingPrime())
    shipping_rule_chain.add_rule(Free2DayShippingNonPrime())
    shipping_rule_chain.add_rule(Free1DayShipping())
    shipping_rule_chain.add_rule(Free2HourGroceryPrime())

    discount_rule_chain = DiscountRuleChain()
    discount_rule_chain.add_rule(SubscribeAndSaveDiscount())

    discount_rule_chain.apply_discounts(order)
    print(f"Order total after discounts: ${order.total_price:.2f}")

    shipping_offer = shipping_rule_chain.get_best_shipping_offer(order)
    print(f"Shipping offer: {shipping_offer}")

    # Print final order details
    print("Final Order Summary:")
    for item in order.items:
        print(f" - {item.name}: ${item.price:.2f}")
    print(f"Total: ${order.total_price:.2f}")
    print(f"Shipping: {shipping_offer}")

