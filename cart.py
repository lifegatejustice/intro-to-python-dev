def display_menu():
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

# Function to add a new item to the cart
def add_item(items, prices):
    item_name = input("What item would you like to add? ")
    item_price = float(input(f"What is the price of '{item_name}'? $"))
    items.append(item_name)
    prices.append(item_price)
    print(f"'{item_name}' has been added to the cart.")

# Function to display the contents of the shopping cart
def display_cart(items, prices):
    print("\nThe contents of the shopping cart are:")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]} - ${prices[i]:.2f}")

# Function to remove an item from the cart
def remove_item(items, prices):
    try:
        item_number = int(input("Which item would you like to remove? ")) - 1
        if 0 <= item_number < len(items):
            del items[item_number]
            del prices[item_number]
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")

# Function to compute the total price of items in the cart
def compute_total(prices):
    total_price = sum(prices)
    print(f"\nThe total price of the items in the shopping cart is ${total_price:.2f}")

# Main function
def main():
    print("Welcome to the Shopping Cart Program!")

    items = []
    prices = []

    while True:
        display_menu()
        choice = input("Please enter an action: ")

        if choice == '1':
            add_item(items, prices)
        elif choice == '2':
            display_cart(items, prices)
        elif choice == '3':
            remove_item(items, prices)
        elif choice == '4':
            compute_total(prices)
        elif choice == '5':
            print("Thank you. Goodbye.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()


