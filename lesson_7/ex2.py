from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def raschod(self):
        pass

class Coat(Clothes):

    def __init__(self, v):
        self.v = float(v)

    @property
    def raschod(self):
        return round(self.v/6.5 + 0.5, 2)


class Jacket(Clothes):

    def __init__(self, h):
        self.h = float(h)

    @property
    def raschod(self):
        return round(2 * self.h + 0.3, 2)


m = Coat(50)
j = Jacket(50)
print(m.raschod + j.raschod)
