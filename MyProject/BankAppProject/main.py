from BankAppProject.Model.User import User
from BankAppProject.Controller.UserController import UserController
from BankAppProject.Controller.BankAppController import BankAppController
from BankAppProject.View.BankAppView import BankAppView


user1 = User("Kirill", "kirill@bank.com", "123", 32000)
user2 = User("Rita", "rita@bank.com", "321", 12000)
user3 = User("Polina", "polina@bank.com", "777", 10000)

userController = UserController(user1)
userController.add_user("Rita", "rita@bank.com", "321", 0)
userController.__init__(user3)
print(userController)

bank_app_view = BankAppView
bank_app_controller = BankAppController(userController, bank_app_view)
bank_app_controller.start()




