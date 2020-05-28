a = float(input('Введите результат первого дня в км:\n'))
b = float(input('Введите цель в км:\n'))

i = 0
while int(a) <= int(b) :
    i += 1
    if a >= b : break
    a = a + a * 0.1

if i == 2 or 5 < i < 9:
    d = 'ой'
elif i == 3:
    d = 'ий'
else :
    d = 'ый'
    
res_str = f'Цель будет достигнута на {i}-{d} день\n'
print(res_str)

input('Для выхода нажмите любую клавишу..')


