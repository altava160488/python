l = list(input("Введите значения для списка\n"))

print(l)

i = 0
while i < len(l) :
    if i % 2 > 0 :
        l.insert(i - 1, l[i])
        l.pop(i+1)
    i += 1

print(l)    
