x = int(input('Введите число:\n'))

m = x % 10
x = x // 10

while x > 0 :
    if m == 9 : break
    if x % 10 > m : m = x % 10
    x = x // 10

res_str = f'Наибольшая цифра:\n{m}\n'    
print(res_str)

input('Для выхода нажмите любую клавишу..')


