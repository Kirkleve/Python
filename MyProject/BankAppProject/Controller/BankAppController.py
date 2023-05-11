from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.View.BankAppView import BankAppView
from BankAppProject.Controller.Account.AccountUser import AccountUser
from BankAppProject.Controller.Account.CreateLogin import CreateLogin


class BankAppController:
    account_user = AccountUser
    user = User
    user_controller = UserController(user)
    bank_app_view = BankAppView()
    choice = 0

    def __init__(self, user_controller, bank_app_view):
        self.user_controller = user_controller
        self.bank_app_view = bank_app_view

    def start(self):
        self.bank_app_view.welcome_message()
        while self.choice != 5:
            self.bank_app_view.start_message()
            self.choice = int(self.bank_app_view.get_choice_login())
            if self.choice == 1:
                self.account_user.input_login()
            elif self.choice == 2:
                CreateLogin().create()
            elif self.choice == 3:
                self.user_controller.remove_user(self.user_controller.find_users_by_email
                                                 (self.bank_app_view.inn_email()))
                print("Пользователь удалён!")
            elif self.choice == 4:
                print(self.user_controller.get_users())
            elif self.choice == 5:
                self.bank_app_view.exit()
            else:
                self.bank_app_view.error_chose()
