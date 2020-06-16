class Road:
    weight = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self):
        return self._length * self._width * self.weight * self.thickness

a = Road(200, 10)
print(f'Для дороги длиной в {a._length}м и шириной в {a._width}м потребуетя {a.get_mass()}т асфальтв')
