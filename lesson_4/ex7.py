def f_factorial(n):
    r = 1
    for i in range(n):
        r *= (i+1)
        yield r

for i in f_factorial(6):
    print(i)
