class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = float(input("Введите делимое:\n"))
    b = float(input("Введите делитель:\n"))
    if b == 0:
        raise MyException("Делитель должен быть отличным от нуля!")
    else:
        print(f"Результат деления равен:\n{round(a/b, 2)}")
except MyException as err:
    print(err)
except:
    print("Формат вводимых данных не является числом!")