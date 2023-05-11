class User:
    name = ""
    email = ""
    password = ""
    balance = 0

    def __init__(self, name, email, password, balance):
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance

    def __se__(self, item):
        if item == "name":
            self.name = item
        elif item == "email":
            return self.email
        elif item == "password":
            return self.password
        elif item == "balance":
            return self.balance

    def set_name(self, name):
        self.name = name

    def __getattr__(self, item):
        if item == "name":
            return self.name
        elif item == "email":
            return self.email
        elif item == "password":
            return self.password
        elif item == "balance":
            return self.balance

    @staticmethod
    def set_balance(balance):
        setattr(User, balance, balance)

    def __repr__(self):
        return "\n" + " - " + self.name + "\nemail - " \
               + self.email + "\npassword - " \
               + self.password + "\nbalance - " + str(self.balance) + "$"
