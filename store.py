import products


class Store:


    def __init__(self, product_list):
        """
        Creates the instance variables of the Store class.
        """
        self.products = product_list


    def add_product(self, product):
        """
        Adds an object from a product class to the product list.
        """
        self.products.append(product)


    def remove_product(self, product):
        """
        Removes product class object from the product list.
        """
        self.products.remove(product)


    def get_total_quantity(self):
        """
        Gets the total quantity of items in the store and returns it.
        """
        return f"There are {len(self.products)} items in the store."


    def get_all_products(self):
        """
        Creates a list with all active products
        in the store and returns it.
        """
        active_products = []
        for i in range(len(self.products)):
            if products.Product.is_active(self.products[i]):
                active_products.append(self.products[i])
        return active_products


    def order(self, shopping_list):
        """
        Counts the total price of an order and buys
        the products from the product list.
        Returns the total price.
        """
        price = 0
        for i in range(len(shopping_list)):
            price += products.Product.buy(shopping_list[i][0], shopping_list[i][1])
        return f"${price}"


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    all_products = store.get_all_products()
    print(store.get_all_products())
    print(store.get_total_quantity())
    print(store.order([(all_products[0], 1), (all_products[1], 2)]))


if __name__ == "__main__":
    main()
