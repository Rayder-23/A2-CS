import pickle   # importing fuction to write in binary files
import os

# work around for keeping the file in the same folder, no need to understand this part
# Get the folder where the .py file is located
script_dir = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(script_dir, "random_access_data.dat")  # Create path for file in same folder



# Random-Access File Processing
# Allows direct access to specific locations within a file, enabling reading or writing of data 'at any 
# position' without the need to sequentially process the entire file.

# It is achieved by using 'hash functions' to compute file offsets or positions based on unique identifiers,
# allowing direct access to specific data locations within the file.

class Product():
    def __init__(self, name, price, expiration_date, is_dairy):
        self.name = name 
        self.price = price
        self.expiration_date = expiration_date
        self.is_dairy = is_dairy

# Writing a single instance of each product record to a random access binary file
products = [
    Product("Milk", 2.99, "2024-02-10", True),
    Product("Cheese", 5.99, "2024-03-15", True),
    Product("Bread", 1.49, "2024-02-05", False)
]

with open(file_path, 'wb') as file: # replaced "random_access_data.dat" with file_path
    for product in products:
        address = hash(product.name) % (2**10 - 1)  # changed 31 to 10 due to insane 1.64GB file size
        file.seek(address)
        pickle.dump(product, file)

# Reading a specific product record from the random access binary file based on the hash function
search_product_name = "Cheese"
search_offset = hash(search_product_name) % (2**10 - 1) # changed 31 to 10 due to insane 1.64GB file size

with open(file_path, 'rb') as file: # replaced "random_access_data.dat" with file_path
    file.seek(search_offset)
    try:
        retrieved_product = pickle.load(file)
        print(f"Retrieved Product: {product.name}, Price: {product.price}, Expiration Date: "
         f"{product.expiration_date}, Dairy: {product.is_dairy}")
    except EOFError:
        print(f"No product found with the name: {search_product_name}")