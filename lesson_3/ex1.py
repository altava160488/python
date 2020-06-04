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

def get_division(n_val,d_val):
    """
    Функция деления чисел

    n_val - числитель
    d_val - знаменатель
    
    """    
    if d_val == 0 :
        print("Делитель равен нулю!")
        return

    return round(n_val/d_val,2)

v = False
while not v :
    a = input("Введите делимое число:\n")
    v = True if is_number(a) else print("Делимое не является числом,")
    
v = False
while not v :
    b = input("Введите делитель:\n")
    v = True if is_number(b) and b != 0 else print("Делитель должен быть числом бОльшим нуля")

a = float(a.replace(',','.'))
b = float(b.replace(',','.'))

print(f"Результат позиционной функции: {get_division(a,b):.2f}")
print('Результат анонимной функции:',(lambda x,y: round(x/y,2))(a,b))

    
