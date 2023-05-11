from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.View.BankAppView import BankAppView


class CreateLogin:
    bank_app_view = BankAppView

    def create(self):
        UserController(User(self.bank_app_view.inn_name(), self.bank_app_view.inn_email(),
                            self.bank_app_view.inn_password(), self.bank_app_view.inn_deposit()))
        self.bank_app_view.create_complete()
