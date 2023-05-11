from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.View.BankAppView import BankAppView
from BankAppProject.Controller.Account.UserMenu import UserMenu


class AccountUser(User):
    @staticmethod
    def input_login():
        bank_app_view = BankAppView
        user_menu = UserMenu

        email = bank_app_view.inn_email()
        password = bank_app_view.inn_password()
        user = UserController(User).find_users_by_email(email)
        if user is None:
            bank_app_view.error_inn_login()
        elif user.password == password:
            user_menu(user)





