from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.View.BankAppView import BankAppView
from BankAppProject.Controller.Account.ActionWithAmount import ActionWithAmount


class UserMenu(User):
    user_menu = User
    users_controller = UserController
    bank_app_view = BankAppView
    action_with_amount = ActionWithAmount
    choice = 0

    def __init__(self, user):
        self.user_menu = user
        self.bank_app_view.welcome_message()
        while self.choice != 4:
            self.bank_app_view.display_menu()
            self.choice = int(self.bank_app_view.get_choice_amount())
            if self.choice == 1:
                self.action_with_amount.deposit(user)
            elif self.choice == 2:
                self.action_with_amount.withdraw(user)
            elif self.choice == 3:
                print("Ваш баланс: " + str(user.balance))
            elif self.choice == 4:
                self.bank_app_view.exit()
            else:
                self.bank_app_view.error_chose()
