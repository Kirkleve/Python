import formating

def log_inn(string):
    with open('Phone_book.csv', 'a') as file:
        file.write('\n' + str(string))

def log_output():
    with open('Phone_book.csv', 'r') as file:
        print(file.read())

def output():
    with open('Phone_book.csv', 'r') as file:
        id = file.readline()
        action = input('Введите имя для поиска: ')
        for i in id:
            id_start = i.find(action)
            id_finish = i.find('\n', id_start)
            print(i[id_start - 8: id_finish - 1])
            break

def dell_info():
    with open('Phone_book.csv', 'r') as file:
        id = file.readline()
    action = input('Введите имя для поиска: ')
    for i in id:
        id_start = i.find(action)
        id_finish = i.find('\n', id_start)
        print(i[id_start - 8: id_finish - 1])
        new_book = i[:id_start - 9] + i[id_finish:]
        with open('Phone_book.csv', 'w') as file2:
            file2.writelines(new_book)
    print('Запись удалена')