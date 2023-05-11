from operation import result
from log import log
from main import text

text()
while True:
    a = input()
    op = input()
    b = input()
    string = a + op + b + '=' + str(result(int(a), int(b), op))
    print(string)
    log(string)
