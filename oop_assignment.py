"""
📝 Assignment: OOP in Python
Author: Oluwalayomi Jesuloluwa

This program demonstrates:
1. Creating a custom class with attributes, methods, and constructors.
2. Using inheritance and encapsulation.
3. Polymorphism with multiple classes sharing the same method but different behavior.
"""

# -------------------------------
# Activity 1: Design Your Own Class
# -------------------------------

class Smartphone:
    def __init__(self, brand, model, storage):
        # Attributes
        self.brand = brand
        self.model = model
        self.__storage = storage  # private attribute (encapsulation)

    # Method to show phone details
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.__storage}GB storage"

    # Method to upgrade storage
    def upgrade_storage(self, extra):
        self.__storage += extra
        print(f"🔒 Storage upgraded! New storage: {self.__storage}GB")

# Child class inheriting from Smartphone
class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, strap_color):
        # Call parent constructor
        super().__init__(brand, model, storage)
        self.strap_color = strap_color

    def watch_info(self):
        return f"{self.brand} {self.model} Smartwatch with {self.strap_color} strap"


# -------------------------------
# Activity 2: Polymorphism Challenge
# -------------------------------

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road...")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky...")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on the water...")


# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    # --- Activity 1 Demo ---
    phone = Smartphone("Apple", "iPhone 15", 128)
    print(phone.phone_info())
    phone.upgrade_storage(64)

    watch = Smartwatch("Samsung", "Galaxy Watch 6", 16, "Black")
    print(watch.watch_info())

    print("\n--- Polymorphism Demo ---")
    # --- Activity 2 Demo ---
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
