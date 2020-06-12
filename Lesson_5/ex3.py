try:
    l = []
    with open('text_3.txt', encoding='utf-8') as f_obj:
        for line in f_obj:
            d = float(line.split()[1])
            l.append(d)
            if d < 20000: print(line, end='')
    print(f'Средний доход: {sum(l) / len(l)}') if len(l) > 0 else print('Файл пуст')
except IOError:
    print('Что-то пошло не так((')