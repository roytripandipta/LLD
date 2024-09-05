# Shopping Cart Rules for Shipping and Discounts

## Overview
This document describes the implementation of shipping and discount rules in a shopping cart service, using design patterns like Strategy, Chain of Responsibility, and Open/Closed Principle.

### Rules:
1. **Free 2-day shipping** on orders over $35 for non-prime members.
2. **Free 2-day shipping** on all orders for prime members.
3. **Free 1-day shipping** on orders over $125.
4. **Free 2-hour grocery shipping** for prime members on grocery orders over $25.
5. **10% discount** on items marked as "Subscribe and Save."

---

## Design Patterns:

### 1. **Strategy Pattern**
- The `ShippingStrategy` and `DiscountStrategy` abstract classes define contracts for different shipping and discount strategies.
- This pattern enables applying different rules based on the context (Prime membership, order total, grocery items, etc.).

#### Shipping Strategies:
- **Free2DayShippingNonPrime**: Free 2-day shipping for non-prime members if the order is over $35.
- **Free2DayShippingPrime**: Free 2-day shipping for all prime members.
- **Free1DayShipping**: Free 1-day shipping for orders over $125.
- **Free2HourGroceryPrime**: Free 2-hour shipping for prime members ordering groceries over $25.

#### Discount Strategies:
- **SubscribeAndSaveDiscount**: Applies a 10% discount to items marked as "Subscribe and Save."

### 2. **Chain of Responsibility Pattern**
- Shipping and discount rules are processed in sequence via chains (`ShippingRuleChain` and `DiscountRuleChain`).
- Each rule is evaluated until an applicable one is found, making it easy to enforce multiple rules in sequence.

### 3. **Open/Closed Principle (OCP)**
- The system follows the OCP, ensuring it's open for extension but closed for modification.
- New rules can be added by implementing the `ShippingStrategy` or `DiscountStrategy` classes and adding them to the chains, without modifying the existing code.

---

## Extending the System:
If new rules, such as holiday promotions or additional shipping rules, are needed, they can be added by implementing new strategy classes and incorporating them into the existing chains. This ensures flexibility and maintainability of the system.
