# User registration and login module
users = {}

def register(username, password):
    if username not in users:
        users[username] = {"password": password, "employees": {}}
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

# Employee management module
def add_employee(username, emp_id, emp_name):
    if username in users:
        if emp_id in users[username]["employees"]:
            print("Employee with the same ID already exists.")
        else:
            users[username]["employees"][emp_id] = {"name": emp_name, "salary": 0, "attendance": {}}
            print(f"Employee '{emp_name}' added.")
    else:
        print("User not found.")

def update_employee(username, emp_id, emp_name):
    if username in users and emp_id in users[username]["employees"]:
        users[username]["employees"][emp_id]["name"] = emp_name
        print(f"Employee '{emp_id}' updated.")
    else:
        print("Employee or user not found.")

def delete_employee(username, emp_id):
    if username in users and emp_id in users[username]["employees"]:
        del users[username]["employees"][emp_id]
        print(f"Employee '{emp_id}' deleted.")
    else:
        print("Employee or user not found.")

# Salary calculation module
def calculate_salary(username, emp_id, salary_amount):
    if username in users and emp_id in users[username]["employees"]:
        users[username]["employees"][emp_id]["salary"] = salary_amount
        print(f"Salary calculated for employee '{emp_id}'.")
    else:
        print("Employee or user not found.")

# Attendance tracking module
def mark_attendance(username, emp_id, date):
    if username in users and emp_id in users[username]["employees"]:
        users[username]["employees"][emp_id]["attendance"][date] = True
        print(f"Attendance marked for employee '{emp_id}' on {date}.")
    else:
        print("Employee or user not found.")

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
                print("\nEmployee Management Menu:")
                print("1. Add Employee")
                print("2. Update Employee")
                print("3. Delete Employee")
                print("4. Calculate Salary")
                print("5. Mark Attendance")
                print("6. Logout")
                emp_choice = input("Enter your choice: ")

                if emp_choice == "1":
                    emp_id = input("Enter employee ID: ")
                    emp_name = input("Enter employee name: ")
                    add_employee(username, emp_id, emp_name)
                elif emp_choice == "2":
                    emp_id = input("Enter employee ID to update: ")
                    emp_name = input("Enter updated employee name: ")
                    update_employee(username, emp_id, emp_name)
                elif emp_choice == "3":
                    emp_id = input("Enter employee ID to delete: ")
                    delete_employee(username, emp_id)
                elif emp_choice == "4":
                    emp_id = input("Enter employee ID to calculate salary: ")
                    salary = float(input("Enter salary amount: "))
                    calculate_salary(username, emp_id, salary)
                elif emp_choice == "5":
                    emp_id = input("Enter employee ID to mark attendance: ")
                    date = input("Enter date (YYYY-MM-DD): ")
                    mark_attendance(username, emp_id, date)
                elif emp_choice == "6":
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
