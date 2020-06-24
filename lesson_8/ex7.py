class ComplexNum():

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, other):
        return self.r + other.r + (self.i + other.i) * 1j

    def __sub__(self, other):
        return self.r - other.r + (self.i - other.i) * 1j

    def __mul__(self, other):
        return (self.r * other.r - self.i * other.i) + (self.i * other.r + other.i * self.r) * 1j

    def __truediv__(self, other):
        return (self.r * other.r + self.i * other.i) / (other.r ** 2 + other.i ** 2) + ((self.i * other.r - self.r * other.i) / (other.r ** 2 + other.i ** 2) ) * 1j

a = ComplexNum(-5,-1)
b = ComplexNum(-1,1)
print(f"{complex(a.r,a.i)} + {complex(b.r,b.i)} = {a+b}")
print(f"{complex(a.r,a.i)} - {complex(b.r,b.i)} = {a-b}")
print(f"{complex(a.r,a.i)} * {complex(b.r,b.i)} = {a*b}")
print(f"{complex(a.r,a.i)} / {complex(b.r,b.i)} = {a/b}")