class Ceil():

    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Ceil(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Ceil(self.number - other.number)
        else:
            print("Разность меньше нуля!")
            return Ceil(0)

    def __mul__(self, other):
        return Ceil(self.number * other.number)

    def __truediv__(self, other):
        return Ceil(self.number // other.number)

    def make_order(self, l):
        s = ""
        for _ in range(int(self.number) // l):
            s += ('*' * l) + '\n'
        return s + '*' * (int(self.number) % l)

c1 = Ceil(50)
c2 = Ceil(13)
c3 = c1/c2

print(c3.number)
print(c2.make_order(5))