def f_power(p_num,p_pow):
    ''' Функция возвращает число p_num, возведенное в степень p_pow '''
    
    try :
        l_num = int(p_num)
    except ValueError :
        return 'Формат числа, возводимого в степень, неверен!'
    
    try :
        l_pow = int(p_pow)
    except ValueError :
        return 'Степень должна быть целочисленной!'

    
    def f_pow():
        ''' Функция возведения в степень путем перемножения в цикле '''
        nonlocal l_num
        nonlocal l_pow
        l_res = l_num      
        for i in range(1, abs(l_pow)) : l_res *= l_num
        return l_res
        
    res = 0
        
    if l_pow == 0 : res = 1
    elif l_pow == 1 : res = p_num
    elif l_pow < 0 : res = 1 / f_pow()
    else : res = f_pow()

    return res

        
a = input("Введите любое(+/-) целое число:\n")
b = input("Введите любую(+/-) степень:\n")

print(f_power(a,b))
