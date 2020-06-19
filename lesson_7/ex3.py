class Ceil():

    def __init__(self, number):
        self.number = float(number)

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return round(self.number // other.number)

    def make_order(self, l):
        s = ""
        for _ in range(int(self.number) // l):
            s += ('*' * l) + '\n'
        return s + '*' * (int(self.number) % l)

c1 = Ceil(50)
c2 = Ceil(13)
print(c1/c2)
print(c2.make_order(5))