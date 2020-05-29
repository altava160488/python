a = input('Введите число:\n')

a1 = int(a)
a2 = int(a + a)
a3 = int(a + a + a)
res1 = a1 + a2 + a3

a = int(a)
i = 0
j = a
while j > 0 :
    i += 1
    j = j // 10
res2 = a * (3 * 1 ** i + 2 * 10 ** i + 1 * 100 ** i)   


print(res1, res2)

input('Для выхода нажмите любую клавишу..')


