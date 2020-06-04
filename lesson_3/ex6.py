def int_func(p_str):
    '''
    Функция принимает и возвращает слово p_str с заглавной буквой,
    если оно начинается с буквы(что-то вроде p_str.title())

    string -> String

    '''
    res = p_str
    if p_str[0].isalpha() :
        res = p_str[0].replace(p_str[0],chr(ord(p_str[0]) - 32)) + p_str[1:]
    return res

a = input("Введите слова, разделенные пробелом:\n").split()

for i in range(len(a)) :
    a[i] = int_func(a[i])

print(' '.join(a))
