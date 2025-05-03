import pickle   # importing fuction to write in binary files
import os

# work around for keeping the file in the same folder, no need to understand this part
# Get the folder where the .py file is located
script_dir = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(script_dir, "product_data.dat")  # Create path for file in same folder

class Product():
    def __init__(self, name, price, expiration_date, is_dairy):
        self.name = name 
        self.price = price
        self.expiration_date = expiration_date
        self.is_dairy = is_dairy

product1 = Product("Milk", 2.99, "2024-02-10", True)

print(product1.name)
# Modifying
product1.name = "Australian Milk"
print(product1.name)

# Sequential File Processing
# Writing records to a file one after another. We can read the records 
# back into the array when the program is run again.

# Creating a list of 100 product records
products = []
for i in range(1,101):
    product = Product(name=f"Product{i}", price=i*1.5, expiration_date=f"2024-12-{i}", is_dairy=(i%2 == 0))  # make a product
    products.append(product)    # add it to the array

# Writing product records to a binary file
with open(file_path, 'wb') as file: # replaced "product_data.dat" with file_path for workaround
    # wb means write binary
    for product in products:
        pickle.dump(product, file)

print("File saved at:", file_path)


# Reading product records from the binary file and appending to a list
retrieved_products = []
with open(file_path, 'rb') as file:  # replaced "product_data.dat" with file_path for workaround
    while True:
        try:    # exception handling
            record = pickle.load(file)
            retrieved_products.append(record)
        except EOFError:
            break

# Printing the retrieved product records
print("\n")
for product in retrieved_products:
    print(f"Name: {product.name}, Price: {product.price}, Expiration Date: "
         f"{product.expiration_date}, Dairy: {product.is_dairy}")