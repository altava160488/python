class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


l = []
print("Введите целые числа для списка разделяя их Enter, для выхода нажимите 'q'")
while True:
    try:
        a = input()
        if a == 'q':
            print(l)
            break

        if a.isdigit():
            l.append(int(a))
        else:
            raise MyException("Введите число!")

    except MyException as err:
        print(err)