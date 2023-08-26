# User registration and login module
users = {}

def register(username, password):
    if username not in users:
        users[username] = {"password": password, "tasks": []}
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

# Task management module
def add_task(username, task):
    users[username]["tasks"].append(task)

def update_task(username, task_index, new_task):
    if 0 <= task_index < len(users[username]["tasks"]):
        users[username]["tasks"][task_index] = new_task
        print("Task updated.")
    else:
        print("Invalid task index.")

def delete_task(username, task_index):
    if 0 <= task_index < len(users[username]["tasks"]):
        deleted_task = users[username]["tasks"].pop(task_index)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

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
                print("\nTask Menu:")
                print("1. Add Task")
                print("2. Update Task")
                print("3. Delete Task")
                print("4. Logout")
                task_choice = input("Enter your choice: ")

                if task_choice == "1":
                    task = input("Enter task description: ")
                    add_task(username, task)
                elif task_choice == "2":
                    task_index = int(input("Enter task index to update: "))
                    new_task = input("Enter updated task description: ")
                    update_task(username, task_index, new_task)
                elif task_choice == "3":
                    task_index = int(input("Enter task index to delete: "))
                    delete_task(username, task_index)
                elif task_choice == "4":
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
