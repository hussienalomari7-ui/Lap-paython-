# DS111 - Lab 2
# OOP and Files – Purchases Processing


# ---------------------------------------------------------
# Question 1: Implementing Purchase class
# ---------------------------------------------------------

class Purchase:
    def __init__(self, customer_name, product, price, quantity):
        self.customer_name = customer_name
        self.product = product
        self.price = float(price)
        self.quantity = int(quantity)

    # Getters and Setters
    def get_customer_name(self):
        return self.customer_name

    def set_customer_name(self, name):
        self.customer_name = name

    def get_product(self):
        return self.product

    def set_product(self, product):
        self.product = product

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = float(price)

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = int(quantity)

    # Total price for one purchase
    def get_total(self):
        return self.price * self.quantity


# Create the four objects required
obj1 = Purchase("Ahmad", "car", 999.99, 1)
obj2 = Purchase("Rana", "Mouse", 25.50, 2)
obj3 = Purchase("Charlie", "Keyboard", 45.00, 1)
obj4 = Purchase("Rama", "Mouse", 25.50, 1)


# ---------------------------------------------------------
# Question 2a: Read purchases from file
# ---------------------------------------------------------

def read_purchases(file_path):
    purchases_list = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            customer, product, price, quantity = line.split(",")

            purchase_obj = Purchase(customer, product, price, quantity)
            purchases_list.append(purchase_obj)

    return purchases_list


# ---------------------------------------------------------
# Question 2b: Find total revenue
# ---------------------------------------------------------

def Find_Total(purchases_list):
    total = 0
    for p in purchases_list:
        total += p.get_total()
    return total


# ---------------------------------------------------------
# Question 2c: Main function
# ---------------------------------------------------------

def main():
    # 1. Read dataset
    file_path = "purchases.txt"
    purchases = read_purchases(file_path)

    # 2. Compute total revenue
    total_revenue = Find_Total(purchases)

    print("Total Revenue =", total_revenue)


# Run the program
if __name__ == "__main__":
    main()
