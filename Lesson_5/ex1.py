import os

def f_available(path):
    if os.path.exists(path) and os.path.isfile((path)):
        return True
    else:
        return False

p = os.path.join(os.getcwd(),'text_1.txt')
if not f_available(p): open(p, 'w')

while True:
    r = input('Нажмите на латинице:\n\'a\' - для добавления записей в файл, \n\'w\' - если нужно перезаписать файл\n')
    if r.lower() in ['a', 'w']: break

try:
    print("Введите правки в файл, для выхода из режима правки нажмите 2 раза Enter:")
    with open(p, r, encoding='utf-8') as f_obj:
        while True:
            t = input()
            if len(t.split()) == 0 : break
            f_obj.write(f'{t}\n')
except:
    print('Обнаружена ошибка при записи в файл')