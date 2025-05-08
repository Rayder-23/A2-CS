# Inheritance in OOP allows new classes (child classes) to reuse and extend the functionality of existing
# classes (parent classes). This simplifies code maintenance, promotes code reuse, and facilitates the
# creation of hierarchical relationships between classes, making the code more organized and easier
# to understand.

# Parent Class
class Product:
    def __init__(self, name, price):
        self.__name = name 
        self.__price = price

    def display_info(self):
            print(f"Product: {self.__name}")
            print(f"Price: ${self.__price}")

# Defining a subclass/child class
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price)   # basically calls the constructor of the parent class
        # Constructors for sub classes must contain a 'super' call
        # super constructor, using this the child class inherits ALL the 
        # attributes and methods of the parent class. It cannot inherit select properties
        self._warranty_period = warranty_period

    def display_info(self):
        super().display_info()  # calls the method of the parent class
        print(f"Warranty Period: {self._warranty_period} months." )

    def check_warranty_status(self, current_date):
        if current_date <= self._warranty_period:
            print("Warranty is still valid.")
        else:
            print("Warranty has expired.")

class GroceryProduct(Product):
    def __init__(self, name, price, expiration_date):
        super().__init__(name, price)
        self._expiration_date = expiration_date

    def display_info(self):
        super().display_info()  # calls the method of the parent class, polymorphism
        print(f"Expiration Date: {self._expiration_date}" ) 
        # uses the parent method, then adding to it.

    def check_if_expired(self, current_date):
        if current_date > self._expiration_date:
            print("Product has expired.")
        else:
            print("Product is still within the expiration date.")

# Create instances of subclasses
elec_product = ElectronicProduct("Smartphone", 800, 12)
grocery_product = GroceryProduct("Milk", 2.5, "2024-02-10")

# Display the info for elec-product
print("Electronic Product Info:")
elec_product.display_info()

print("\n")
# Display the info for grocery-product
print("Grocery Product Info:")
grocery_product.display_info()

# Polymorphism is a core concpet in object-oriented programming (OOP) that allows objects 
# of different classes to be treated as objects of a common superclass. It enables methods in a 
# superclass to be implemented in different ways by its subclasses, providing flexibility and 
# enabling code reuse. Already has been applied above.
