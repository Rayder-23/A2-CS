# Object-Oriented Programming

# Main Rules/Principles:
# 1) Encapsulation: hides the internal state and functionality of an object and only exposes 
# what’s necessary through public methods.

# 2) Abstraction: simplifies complex systems by modeling classes based only on relevant data and behavior.

# 3) Inheritance: allows a class to inherit properties and methods from another class, promoting code reuse.

# 4) Polymorphism: lets objects of different classes be treated as instances of the same class 
# through a common interface.


# Classes in OOP
# in OOP, a class is a blueprint for objects. It groups together the data structure and the
# subroutines that operate on the data items in this data struture.

# -Attributes represent the object's state. They are referred to as 'private'.
# -Methods define its behaviour. Methods are referred to as 'public'.
# Encapsulation is maintained by accessing attributes only through methods.

# A constructor is a special method called __init__() that automatically runs when 
# a new object is created, used to initialize the object’s attributes.

# A method is a function that is defined inside a class and acts on objects (instances) of 
# that class — it usually takes self as the first parameter to refer to the specific object calling it.

class Product:
    def __init__(self, product_id, name, price, quantity, manufacture_date):
        self.__product_id = product_id  # the double underscore (.__) signifies that this value is private
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__manufacture_date = manufacture_date
    # All this data above is private, aka it cannot be access via the normal way of accessing
    # data in objects/dictionaries

    # All this below is public, therefore it can be used
    # Getter Methods
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    # A property in a Python class allows defining getter, setter and deleter methods.
    @property
    def price(self):
        return self.__price
    
    @property
    def quantity(self):
        return self.__quantity
    
    def get_manufacture_date(self):
        return self.__manufacture_date
    
    # Setter Methods
    def set_price(self, price):
        if price >= 0:
            self.__price = price

    @quantity.setter    # in order to use the setter version, the property must first be defined above
    def quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity

    # Additional Method for displaying all the information
    def display_info(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: {self.__price}")
        print(f"Quantity: {self.__quantity}")
        print(f"Manufacture Date: {self.__manufacture_date}")

# Create an object
product1 = Product(product_id=1, name="Laptop", price=1200, quantity=5,manufacture_date="2023-01-15")

# Access and Display Information
print("Product Info:")
print("Product ID:", product1.get_product_id())
print("Name:", product1.get_name())
print("Price:", product1.price)   # property so no () needed, access it like a variable
print("Quantity:", product1.quantity)
print("Manufacture Date:", product1.get_manufacture_date())
# print(product1[name])  # can't use Square Bracket Notation now

print("\n")
# Update price and quantity using setter methods
product1.set_price(1000)
product1.quantity = 10 # use property setter like assigning a variable
print("Product Info:- "), product1.display_info()
