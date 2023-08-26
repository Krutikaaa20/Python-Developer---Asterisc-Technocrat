class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options):
            print(f"{i + 1}. {option}")

    def is_correct(self, user_answer):
        return user_answer == self.correct_option

class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def run(self):
        score = 0
        print(f"Welcome to the '{self.quiz_name}' Quiz!\n")
        for question in self.questions:
            question.display()
            user_answer = input("Your answer (enter option number): ")

            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(question.options):
                    if question.is_correct(user_answer):
                        print("Correct!\n")
                        score += 1
                    else:
                        print("Incorrect.\n")
                else:
                    print("Invalid option number.\n")
            else:
                print("Invalid input. Please enter a valid option number.\n")

        print(f"Quiz completed. Your score: {score}/{len(self.questions)}")
        return score

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.quizzes = []

    def create_quiz(self, quiz_name):
        quiz = Quiz(quiz_name)
        self.quizzes.append(quiz)
        return quiz

    def take_quiz(self, quiz):
        if quiz in self.quizzes:
            return quiz.run()
        else:
            print("You don't have permission to take this quiz.")
            return 0

users = {}  # Store user data in a dictionary (username -> User object)

def register_user():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return
    password = input("Enter a password: ")
    users[username] = User(username, password)
    print("User registered successfully!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username].password == password:
        return users[username]
    else:
        print("Invalid username or password.")
        return None

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            logged_in_user = login()
            if logged_in_user:
                while True:
                    print("\nUser Menu:")
                    print("1. Create a new quiz")
                    print("2. Take a quiz")
                    print("3. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        quiz_name = input("Enter the quiz name: ")
                        logged_in_user.create_quiz(quiz_name)
                        print(f"Quiz '{quiz_name}' created.")
                    elif user_choice == "2":
                        if not logged_in_user.quizzes:
                            print("You don't have any quizzes to take.")
                            continue
                        print("Select a quiz to take:")
                        for i, quiz in enumerate(logged_in_user.quizzes):
                            print(f"{i + 1}. {quiz.quiz_name}")
                        quiz_index = int(input("Enter quiz index: ")) - 1
                        if 0 <= quiz_index < len(logged_in_user.quizzes):
                            score = logged_in_user.take_quiz(logged_in_user.quizzes[quiz_index])
                            print(f"Your score for '{logged_in_user.quizzes[quiz_index].quiz_name}' quiz: {score}/{len(logged_in_user.quizzes[quiz_index].questions)}")
                        else:
                            print("Invalid quiz index.")
                    elif user_choice == "3":
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
