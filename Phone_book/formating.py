from input_info import *

def format_A(info):
    count = 1
    inf = info
    print(f'Фамилия_{count}: {inf["Фамилия"]}\n'
          f'Имя_{count}: {inf["Имя"]}\n'
          f'Телефон_{count}: {inf["Телефон"]}\n'
          f'Коментарий_{count}: {inf["Коментарий"]}\n'
          f'--------------------------')

def format_B(info):
    print(';   '.join("{}: {}".format(k, v) for k, v in info.items()))

def inn_format(number_chose,form_a, form_b):
    if number_chose == 1:
        return form_a
    else:
        return form_b
