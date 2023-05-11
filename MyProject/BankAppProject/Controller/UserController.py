from BankAppProject.Model.User import User
from BankAppProject.View.BankAppView import BankAppView


class UserController(User):
    users = []

    def __init__(self, user):
        self.User = super().__init__(user.name, user.email, user.password, user.balance)
        self.users.append(user)

    def add_user(self, name, email, password, balance):
        self.users.append(User(name, email, password, balance))

    def remove_user(self, user):
        self.users.remove(user)

    def get_users(self):
        return self.users

    def find_users_by_email(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    @staticmethod
    def deposit(user, amount):
        user.set_balance(str(user.balance + int(amount)))

    @staticmethod
    def withdraw(user, amount):
        if user.balance >= amount:
            user.set_balance(str(user.balance - int(amount)))
        else:
            print("Недостаточно средств")

    def __str__(self):
        return "База данных пользователей: " + str(self.users) + "\n"
