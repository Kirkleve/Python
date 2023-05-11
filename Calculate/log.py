def log (string):
    with open('history.txt', 'a') as file:
        file.write(string + '\n')