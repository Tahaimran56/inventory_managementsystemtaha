Inventory Management System
This is a Python-based Inventory Management System designed to manage different types of products, handle stock operations, sales, and persist data. The system is built using Object-Oriented Programming (OOP) principles and includes functionality for adding products, selling products, searching, restocking, and saving/loading inventory data.

Key Features:
Product Types: Supports managing different types of products such as Electronics, Grocery, and Clothing.

Stock Operations: Allows you to restock and sell products while maintaining a correct inventory.

Data Persistence: Product data is saved to and loaded from JSON files for persistence.

Custom Exceptions: Handles edge cases like insufficient stock, duplicate product IDs, and invalid data from files.

CLI Interface: Provides a command-line interface for interacting with the system.

System Overview
1. Abstract Base Class: Product
The Product class serves as an abstract base class for all products. It contains common attributes and methods for all product types, including:

_product_id: Unique identifier for each product.

_name: Name of the product.

_price: Price per unit of the product.

_quantity_in_stock: Number of units of the product available in inventory.

Methods in Product Class:
restock(amount): Restocks the product with a specified amount.

sell(quantity): Sells a specified quantity of the product.

get_total_value(): Calculates the total value of the stock (price * quantity).

__str__(): Displays the product information in a formatted way.

2. Subclasses of Product
We define three subclasses that inherit from the Product class, each with additional attributes and custom behavior.

Electronics: Has warranty_years and brand attributes.

Grocery: Includes expiry_date and an is_expired() method that checks if the product is past its expiration date.

Clothing: Contains size and material attributes.

3. Class: Inventory
The Inventory class manages a collection of products. It provides methods to add, remove, sell, restock, and search for products in the inventory.

Methods in Inventory Class:
add_product(product): Adds a new product to the inventory.

remove_product(product_id): Removes a product by its ID.

search_by_name(name): Searches for products by name.

search_by_type(product_type): Searches for products by their type (e.g., Electronics, Grocery, Clothing).

list_all_products(): Lists all the products in the inventory.

sell_product(product_id, quantity): Sells a specified quantity of a product.

restock_product(product_id, quantity): Restocks a product with a specified quantity.

total_inventory_value(): Returns the total value of all products in the inventory.

remove_expired_products(): Removes expired products (specific to Grocery).

4. Custom Exceptions
The following custom exceptions are used for error handling:

ProductNotFoundException: Raised when a product cannot be found in the inventory.

InsufficientStockException: Raised when there is not enough stock to sell.

DuplicateProductIDException: Raised when attempting to add a product with a duplicate ID.

InvalidProductDataException: Raised when loading invalid product data from a file.

5. Command Line Interface (CLI)
The system includes a simple CLI that allows users to interact with the inventory. The menu options are:

Add Product: Allows the user to add new products to the inventory.

Sell Product: Allows the user to sell a specified quantity of a product.

List Products: Lists all the products currently in the inventory.

Restock Product: Allows the user to restock a product with a specified quantity.

Total Inventory Value: Displays the total value of all products in the inventory.

Save Inventory: Saves the inventory data to a JSON file.

Load Inventory: Loads the inventory data from a JSON file.

Exit: Exits the program
