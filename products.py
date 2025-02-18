class Product:


    def __init__(self, name, price, quantity):
        """
        Creates the instance variables of the Product class (active is set to True).
        If something is invalid (empty name / negative price or quantity),
        raises an exception.
        """
        if name == "":
            raise ValueError("The name is empty.")
        else:
            self.name = name
        if price < 0:
            raise ValueError("The price is negative.")
        else:
            self.price = price
        if quantity < 0:
            raise ValueError("The quantity is negative.")
        else:
            self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """
        Gets the quantity of the product and returns it.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Sets the quantity based on the given quantity parameter.
        If quantity reaches 0, deactivates the product
        """
        self.quantity += quantity
        if self.quantity == 0:
            self.deactivate()


    def is_active(self):
        """
        Checks if a product is active or not.
        Returns True if the product is active, otherwise False.
        """
        return self.active


    def activate(self):
        """
        Activates a product (sets the active status to True).
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates a product (sets the active status to False).
        """
        self.active = False


    def show(self):
        """
        Returns a string that represents the product.
        """
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        Updates the quantity and buys the given quantity of the product.
        Returns the total price of the purchase.
        Raises exception, if the quantity is larger than what exists.
        """
        if (self.quantity - quantity) >= 0:
            self.set_quantity(-quantity)
            total_price = float(self.price * quantity)
            return total_price
        elif (self.quantity - quantity) < 0:
            raise ValueError("Error with your order! Quantity larger than what exists.")


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()