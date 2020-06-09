from random import randrange

l = [i+randrange(5) for i in range(15)]
r = [i for i in l if l.count(i) == 1]

print(l)
print(r)