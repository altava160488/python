try:
    i = 0
    with open('text_2.txt', encoding='utf-8') as f_obj:
        for line in f_obj:
            i += 1
            l = len(line.split())
            print(f'количество слов в строке {i}: {l}')
except IOError:
    print('Что-то пошло не так((')