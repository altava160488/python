from sys import argv
from itertools import count, cycle

py_script, num = argv

def f_count(n):
    try:
        n = int(n)
        for i in count(n, 2):
            if i > n + 10:
                break
            else:
                print(i)
    except ValueError:
        print('Формат вводимого значения неверен!')


def f_cycle(l, n):
    j = 0
    try:
        n = int(n)
        for i in cycle(l):
            if j > len(l) + n:
                break
            else:
                j += 1
                print(i)
    except ValueError:
        print('Формат вводимого значения неверен!')

l = list('В России предложили платить работникам 150 рублей в час !'.split())

print('Результат выполнения itertools.count:')
f_count(num)
print('Результат выполнения itertools.cycle:')
f_cycle(l, num)
