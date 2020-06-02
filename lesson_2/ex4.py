f = 0
while f == 0 :
    s = input("Введите строку из слов и пробелов\n")
    f = 1 if s.count(' ') > 0 and len(s.replace(' ', '')) > 0 else 0

l = list(s.split())
for n, e in enumerate(l,1) :
    print(n, e[:10])
