weight = int(input('Ваш вес в кг:\n'))   
height = int(input('Ваш рост в см:\n'))

res = weight / (height / 100) ** 2
res_str = 'Ваш ИМТ:\n%.2f\n'%res

print(res_str)

input('Для выхода нажмите любую клавишу..')


