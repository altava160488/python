v = False
while v == False :
    a = input("Хотите ввести товар? Y/N\n")
    v = a.upper() in ['Y','N']

if a.upper() == 'N' : exit()

l = []

is_single_v = False
while not is_single_v :
    
    v = False
    while v == False :
        name = input("Введите наименование товара:\n")
        v = name.isalpha()
        if not v : print("Используйре буквы в наименовании")

    v = False
    while v == False :
        price = input(f"Введите цену товара - {name}:\n")
        try :
            float(price)
            v = True
        except ValueError:
            print(f'Используйте цифры и знак \'.\' в качестве разделителя')
            v = False

    v = False
    while v == False :
        quantity = input(f"Введите количество товара -{name}:\n")
        v = quantity.isdigit()
        if not v : print("Количество должно быть целочисленным") 

    v = False
    while v == False :
        unit = input(f"Введите ед.изменерения товара -{name}:\n")
        v = name.isalpha()
        if not v : print("Используйре буквы в ед.изменерении")

    s = {}
    s['Наименование'] = name
    s['Цена'] = price
    s['Количество'] = quantity
    s['Ед.изм.'] = unit

    l.append((len(l) + 1, s))
    
    v = False
    while not v :
        a = input("Хотите еще добавить товар? Y/N\n")
        v = a.upper() in ['Y', 'N']

    is_single_v = a.upper() in ['N']


v = False
while not v :
    a = input("Вывести аналитику? Y/N\n")
    if a.upper() == 'N' :
        v = True
        print("Вы ввели нижеследующий(-ие) товар(-ы):\n", l)
    if a.upper() == 'Y' :
        v = True
        r = {}
        i = 0

        for key in l[i][1].keys() :
            r[key] = []

        while i < len(l) :
            for k,v in l[i][1].items() :
                r[k].append(v)
            i += 1

print(r)
