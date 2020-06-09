from random import randint

l = [i + randint(1, 100) for i in range(15)]
print(l)

r = [l[i] for i in range(1, len(l)) if l[i] > l[i-1]]
print(r)