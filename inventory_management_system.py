class Product:
    def __init__(self, product_id, name, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def restock(self, amount):
        self.quantity_in_stock += amount

    def sell(self, quantity):
        if quantity > self.quantity_in_stock:
            print("Not enough stock!")
        else:
            self.quantity_in_stock -= quantity

    def get_total_value(self):
        return self.price * self.quantity_in_stock

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price} | Stock: {self.quantity_in_stock}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def list_products(self):
        for product in self.products.values():
            print(product)

    def sell_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].sell(quantity)
        else:
            print("Product not found.")

    def restock_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].restock(quantity)
        else:
            print("Product not found.")

    def total_inventory_value(self):
        total_value = 0
        for product in self.products.values():
            total_value += product.get_total_value()
        return total_value



def display_menu():
    print("\n1. Add Product")
    print("2. Sell Product")
    print("3. List Products")
    print("4. Restock Product")
    print("5. Show Total Inventory Value")
    print("6. Exit")


def main():
    inventory = Inventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity_in_stock = int(input("Enter Product Quantity: "))

            product = Product(product_id, name, price, quantity_in_stock)
            inventory.add_product(product)
            print(f"Product {name} added.")

        elif choice == "2":
            product_id = input("Enter Product ID to Sell: ")
            quantity = int(input("Enter Quantity to Sell: "))
            inventory.sell_product(product_id, quantity)

        elif choice == "3":
            inventory.list_products()

        elif choice == "4":
            product_id = input("Enter Product ID to Restock: ")
            quantity = int(input("Enter Quantity to Restock: "))
            inventory.restock_product(product_id, quantity)

        elif choice == "5":
            print(f"Total Inventory Value: ${inventory.total_inventory_value()}")

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
