f = 0
while f == 0 :
    n = input("Введите целое число\n")
    f = int(n.isdigit())

n = int(n)
l = [15, 7, 5, 5, 2]
print(l)

i = 0
e = len(l)

while i < e :
    if n > l[i] :
        l.insert(i,n)
        break
    if i == e - 1 : l.append(n)
    i += 1
    
print(l)
