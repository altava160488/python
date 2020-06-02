l = [7, 5/2, 'cool', [], {}, set(range(-5,0))]
l[3].insert(0,-7)
l[3].append(list(range(2)))
l[4]['color'] ='blue'
l.append(frozenset(range(3)))

##поскольку списки упорядочены по индексам, использую последние для нумерации строк(как вариант решения)
for i in l :
    n = l.index(i) + 1
    print(f'{n:<5}{str(type(i)):<20}{str(i):>30}')

##или вариант общий/для всех типов, показанный на уроке
for x,e in enumerate(l,1) :
    print(f'{x:<5}{str(type(e)):<20}{str(e):>30}')

