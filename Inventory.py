# User registration and login module
users = {}

def register(username, password):
    if username not in users:
        users[username] = {"password": password, "items": {}}
        print("Registration successful.")
    else:
        print("Username already exists.")

def login(username, password):
    if username in users and users[username]["password"] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid credentials.")
        return False

# Inventory management module
def add_item(username, item_name, quantity, price):
    if username in users:
        if item_name in users[username]["items"]:
            print("Item already exists in your inventory.")
        else:
            users[username]["items"][item_name] = {"quantity": quantity, "price": price}
            print(f"Item '{item_name}' added to your inventory.")
    else:
        print("User not found.")

def delete_item(username, item_name):
    if username in users and item_name in users[username]["items"]:
        del users[username]["items"][item_name]
        print(f"Item '{item_name}' deleted from your inventory.")
    else:
        print("Item or user not found.")

def purchase_item(username, item_name, quantity):
    if username in users and item_name in users[username]["items"]:
        if users[username]["items"][item_name]["quantity"] >= quantity:
            total_price = users[username]["items"][item_name]["price"] * quantity
            users[username]["items"][item_name]["quantity"] -= quantity
            print(f"Purchased {quantity} units of '{item_name}' for {total_price} units.")
        else:
            print("Insufficient quantity in inventory.")
    else:
        print("Item or user not found.")

# Main program
while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password):
            while True:
                print("\nInventory Menu:")
                print("1. Add Item")
                print("2. Delete Item")
                print("3. Purchase Item")
                print("4. Logout")
                inventory_choice = input("Enter your choice: ")

                if inventory_choice == "1":
                    item_name = input("Enter item name: ")
                    quantity = int(input("Enter quantity: "))
                    price = float(input("Enter price per unit: "))
                    add_item(username, item_name, quantity, price)
                elif inventory_choice == "2":
                    item_name = input("Enter item name to delete: ")
                    delete_item(username, item_name)
                elif inventory_choice == "3":
                    item_name = input("Enter item name to purchase: ")
                    quantity = int(input("Enter quantity to purchase: "))
                    purchase_item(username, item_name, quantity)
                elif inventory_choice == "4":
                    break
                else:
                    print("Invalid choice.")
        else:
            print("Login failed.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
