from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.View.BankAppView import BankAppView


class ActionWithAmount:
    @staticmethod
    def deposit(user):
        amount = int(BankAppView.get_amount())
        UserController.deposit(user, amount)
        print("$" + str(amount) + "  было зачислен на ваш счет.")

    @staticmethod
    def withdraw(user):
        amount = int(BankAppView.get_amount())
        UserController.withdraw(user, amount)
        print("$" + str(amount) + " было снято с вашего аккаунта.")
