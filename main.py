import products
import store


def show_products(best_buy):
    """
    Displays all products in the store.
    """
    products_in_store = best_buy.get_all_products()
    for i in range(len(products_in_store)):
        print(f"{i + 1}. {products_in_store[i].show()}")


def show_total_amount(best_buy):
    """
    Displays the total amount of products in the store.
    """
    print(store.Store.get_total_quantity(best_buy))


def make_order(best_buy):
    """
    Creates a shopping list and makes an order.
    """
    products_in_store = best_buy.get_all_products()
    shopping_list = []
    user_chose_product = True
    while user_chose_product:
        try:
            for i in range(len(products_in_store)):
                print(f"{i + 1}. {products_in_store[i].show()}")
            print(f"{"-" * 55}\nWhen you want to finish order, enter empty text.")
            chosen_product = input("Which product # do you want? ")
            chosen_amount = input("What amount do you want? ")
            if chosen_product == "" and chosen_amount == "":
                print(f"{"*" * 40}\nOrder made! Total price: {best_buy.order(shopping_list)}\n{"*" * 40}")
                user_chose_product = False
            elif int(chosen_product) > len(products_in_store) or int(chosen_product) <= 0 or int(chosen_amount) < 0:
                raise ValueError("The product you choose is not in the store or the amount you choose is negative!")
            else:
                chosen_order = (products_in_store[int(chosen_product) - 1], int(chosen_amount))
                shopping_list.append(chosen_order)
                print("Product added to list!\n")
        except ValueError as e:
            print(e)
            user_chose_product = False


def start():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = store.Store(product_list)

    shopping = True
    while shopping:
        try:
            print("\nStore Menu"
                f"\n{"-" * 30}"
                "\n1. List all products in store"
                "\n2. Show total amount in store"
                "\n3. Make an order"
                "\n4. Quit")
            user_input = input("Please choose a number: ")
            if user_input == "1":
                show_products(best_buy)
            elif user_input == "2":
                show_total_amount(best_buy)
            elif user_input == "3":
                make_order(best_buy)
            elif user_input == "4":
                print("You have exit the store.")
                shopping = False
            else:
                raise ValueError("Error with your choice! Try again!")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    start()