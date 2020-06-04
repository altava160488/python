def is_number(val):
    """
    Функция проверяет входное значение val на число
    
    Возвращает :
        True - если val является числом
        False - если val не число
        
    """
    try :
        float(val.replace(',','.'))
        return True
    except ValueError :
        return False

s = 0
is_first_iter = True
is_exit = False

while not is_exit :
    
    if is_first_iter :
        a = list(input("Введите числа разделяя их пробелом:\n").split())
        is_first_iter = False
    else :
        print(s)
        a = list(input("\n").split())
        
    i = 0
    while i < len(a) :
        if is_number(a[i]) :
            s += float(a[i].replace(',','.'))
        else :
            print(s)
            is_exit = True
            break
        i += 1
