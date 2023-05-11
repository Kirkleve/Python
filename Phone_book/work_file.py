import input_info
import menu
import log
import formating

def use():
    inn = 'да'
    while inn == 'да':
        res = menu.choice()
        if res == 1:
            add_phone_book = input_info.add_info()
            log.log_inn(add_phone_book)
        elif res == 2:
            log.output()
            log.log_output()
        elif res == 3:
            log.log_output()
        elif res == 4:
            log.dell_info()
        else:
            print('Неверная команда!!!')
        inn = input('Продолжить работу в телефонной книге(да/нет)?\n - ')
    print('До новых встреч')

use()