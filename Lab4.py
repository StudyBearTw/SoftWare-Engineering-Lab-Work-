class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        return f"{self.name}: ${self.price} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} removed from cart.")
        else:
            print("Product not found in cart.")

    def calculate_total(self):
        return sum(p.price for p in self.products)


class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = sum(item.price for item in items)

    def display_order(self):
        item_list = ", ".join([item.name for item in self.items])
        return f"Order {self.order_id}: {item_list} - Total: ${self.total}"


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def register(self):
        print(f"User {self.name} registered with email {self.email}.")

    def place_order(self, cart):
        new_order = Order(len(self.orders) + 1, cart.products)
        self.orders.append(new_order)
        cart.products = []  # Clear cart after order
        print(f"Order placed: {new_order.display_order()}")


# 測試程式碼
product1 = Product("Laptop", 999.99, 5)
product2 = Product("Mouse", 25.50, 20)

cart = ShoppingCart()
user = User("John Doe", "john@example.com")

user.register()
cart.add_product(product1)
cart.add_product(product2)

user.place_order(cart)