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
    

def my_func(a,b,c):
    """
    Функция возвращает сумму 2-х наибольших слагаемых из входных параметров 
    
    """
    s = a + b + c - min([a, b, c])            
    return s


v = False
while not v :
    a = input("Введите 3 слагаемых отделяя их друг от друга пробелом:\n").split()
    if len(a) != 3 :
        print("Количество слагаемых не равно 3!")
    elif (is_number(a[0]) and is_number(a[1]) and is_number(a[2])) :
        v = True
    else :
        print("Формат слагаемых неверен!")

x = float(a[0].replace(',','.'))
y = float(a[1].replace(',','.'))
z = float(a[2].replace(',','.'))

print('вариант с именованной функцией: ',\
      my_func(x,y,z))

print('вариант с анонимной функцией ',\
      (lambda p1, p2, p3: p1 + p2 + p3 - min([p1, p2, p3]))(x,y,z))
