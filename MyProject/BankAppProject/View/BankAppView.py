
class BankAppView:
    @staticmethod
    def welcome_message():
        print("Добро пожаловать в банк!")

    @staticmethod
    def start_message():
        print("\nВыберете действие: ")

    @staticmethod
    def inn_email():
        print("Введите email: ")
        return input()

    @staticmethod
    def inn_password():
        print("Введите пароль: ")
        return input()

    @staticmethod
    def inn_name():
        print("Введите имя: ")
        return input()

    @staticmethod
    def create_complete():
        print("Логин создан!")

    @staticmethod
    def inn_deposit():
        print("Депозит: ")
        return input()

    @staticmethod
    def display_menu():

        print("1. Депозит")
        print("2. Вывод средств")
        print("3. Показать баланс")
        print("4. Выход")

    @staticmethod
    def get_choice_login():
        print("1 - Вход\n" +
              "2 - Создать логин и пароль\n" +
              "3 - Удалить логин\n" +
              "4 - Показать пользователей\n" +
              "5 - Выход\n")
        return input()

    @staticmethod
    def get_choice_amount():
        print("Выберете от 1 до 4: ")
        return input()

    @staticmethod
    def get_amount():
        print("Пожалуйста, введите сумму: ")
        return input()

    @staticmethod
    def error_inn_login():
        print("Неверный адрес электронной почты или пароль.")

    @staticmethod
    def error_chose():
        print("Неверный выбор!")

    @staticmethod
    def exit():
        print("Выход...")
