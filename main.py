from IPython.display import clear_output


def my_cart():
    while True:
        print('''             ***********
        ***LIST OF OPTIONS***
        Enter the number you would like to perform:
        1. View all options
        2. Add item to shopping cart
        3. Remove item from shopping cart
        4. Review shopping cart
        5. Clear shopping cart
        6. Checkout
        7. Exit
        ''')
        number = input("Make your selection: ")
        clear_output()
        if number == "1":
            displaylist()
        elif number == "2":
            add()
        elif number == "3":
            remove()
        elif number == "4":
            check_cart()
        elif number == "5":
            clear()
        elif number == "6":
            checkout()
        elif number == "7":
            break
        else:
            print('Selection is invalid, please enter 1-7')
shopping_list = {
    "Apple": '1.00',
    "Banana": '.50',
    'Milk': '1.75',
    'Egg 1 Dozen': '1.50',
    "Pizza Rolls": '3.20',
    "Oranges": '2.75',
    "Potato Chip": '2.00',
    "Ice Cream": '10.99'
}
def displaylist():
    print("--Shopping List--")
    for i, y in shopping_list.items():
        print("* "+i, y)
cart = []
def add():
    for i, y in shopping_list.items():
        print("* "+i, y)
    item = input("What item would you like to add to cart? ").title()
    while item not in shopping_list.keys():
        print(f"Sorry we don't sell {item}")
        item = input("What item would you like to add to cart? ").title()
    price = input(f"What is the price of {item}'s?  $")
    while price not in shopping_list.values():
        print(f"Sorry, we don't have products for this price: {price}")
        price = input(f"What is the price of {item}'s  $")
    quantity = input(f"How many {item}'s would you like? ")
    total = float(price) * int(quantity)
    new = [item, quantity+'x',total]
    cart.append(new)
    clear_output()
    print(f" {item}'s Added to cart")
def remove():
    print(cart)
    item = input("What item would you like to remove from cart? ").title()
    for i in cart:
        if i[0]== item:
            cart.remove(i)
            clear_output()
            print(f"{item} - has been removed")
    else:
        print (f"{item} is not in cart")
def check_cart():
    print(cart)
def clear():
    double_check =input("Are you sure you want to clear your shopping cart? Y/N ").lower()
    while double_check not in {'y', 'n'}:
        double_check = input("Invalid repsonse. Please enter Y/N ").lower
        if double_check == 'n':
            break
    if double_check == "y":
        cart.clear()
        print("Cart has been cleared")
def checkout():
    print(cart)
    s = 0
    for i in cart:
        for y in i:
            if type(y) == float:
                s += y
            print(f"your total is {s}")
    would_you = input('Would you like to continue? Y/N').title()
    while would_you not in {'Y', 'N'}:
        would_you = input('Invalid response. Please enter Y/N').title()
        if would_you == 'N':
            break
    if would_you == 'y':
        print("Your order has been placed. Thank You!")
my_cart()