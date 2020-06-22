from abc import ABC, abstractmethod

class Stock:
    # параметры склада
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.equipment = {}

    # общий объем хранения
    @staticmethod
    def storage_area(length, width, height):
        return length * width * height * 0.7

    # доступный объем хранения
    @property
    def free_storage_area(self):
        s = 0
        for v in self.equipment.values():
            s += v["capacity"] * v["quantity"] * 0.001

        return Stock.storage_area(self.height,self.width,self.length) - s

    # приход оборудования
    def imprt(self, e, quantity):
        x = int(self.free_storage_area // (e.capacity * 0.001))
        d = {}
        if x == 0:
            print("Мест на складе нет!")
        elif x < quantity:
            while True:
                a = input(f"Место для {e.model} есть только в количестве {x}\n Хотите добавить?(Y/N)\n")
                if a.lower() == 'y':
                    d["type"] = e.type
                    d["capacity"] = e.capacity
                    d["quantity"] = x
                    for k, v in self.equipment.items():
                        if k == e.model:
                            d["quantity"] = x + v["quantity"]
                    self.equipment[e.model] = d
                if a.lower() in ['y','n']: break
        else:
            d["type"] = e.type
            d["capacity"] = e.capacity
            d["quantity"] = quantity
            for k, v in self.equipment.items():
                if k == e.model:
                    d["quantity"] += v["quantity"]
            self.equipment[e.model] = d

    # уход оборудования
    def exprt(self, e, quantity):
        x = self.equipment[e.model]["quantity"] - quantity
        if x >= 0:
            self.equipment[e.model]["quantity"] -= quantity
        else:
            while True:
                a = input(f"Осталось только {quantity - x} шт. Хотите продолжить?(Y/N)")
                if a.lower() == 'y' : self.equipment[e.model]["quantity"] -= (quantity - x)
                if a.lower() in ['y','n']: break

    # витрина
    def show_equipment(self):
        print(self.equipment)

    # количество оргтехники определенного типа
    def type_quantity(self, type):
        s = 0
        for k in self.equipment.keys():
            s += self.equipment[k]['quantity'] if self.equipment[k]['type'] == type else 0
        return s

    # количество оргтехники
    def model_quantity(self, model):
        s = 0
        for k in self.equipment.keys():
            s += self.equipment[k]['quantity'] if k == model else 0
        return s

class Equipment(ABC):
    def __init__(self, model, price, length, width, height, type = None):
        self.model = model
        self.price = price
        self.width = width
        self.length = length
        self.height = height
        self.type = type

    @abstractmethod
    def action(self):
        print("Техника должна что-то делать")

    @property
    def capacity(self):
        return self.width * self.length * self.height

    @classmethod
    def get_type(cls):
        cls.print_type("Оргтехника")

    @classmethod
    def print_type(cls, arg):
        return arg

class Printer(Equipment):
    def __init__(self,model,price,length,width,height,type = 'printer'):
        super().__init__(model,price,length,width,height,type)

    def action(self):
        print(f"выводит печать на бумагу")

    @classmethod
    def get_type(cls):
        return cls.print_type("Принтер")

class Scaner(Equipment):

    def __init__(self,model,price,length,width,height,type = 'scaner'):
        super().__init__(model,price,length,width,height,type)

    def action(self):
        print(f"считывает изображение на бумаге для создания его электронной копии")

    @classmethod
    def get_type(cls):
        return cls.print_type("Сканер")

class Xerox(Equipment):

    def __init__(self,model,price,length,width,height,type = 'xerox'):
        super().__init__(model,price,length,width,height,type)

    def action(self):
        print(f"копирует изображение на бумаге")

    @classmethod
    def get_type(cls):
        return cls.print_type("Ксерокс")


sklad = Stock(500,500,500)
print(f"Объем хранения {Stock.storage_area(500, 500, 500)} квадратных метров")
print(f"Объем доступного хранения {sklad.free_storage_area} квадратных метров")

p = Printer("hp2020", 5000, 50, 50, 50)
pp = Printer("canon2020", 1000, 55, 55, 55)
sc = Scaner("hp200", 15000, 50, 50, 50)
sklad.imprt(p, 1200)
sklad.imprt(p, 200)
sklad.imprt(pp, 200)
sklad.imprt(sc, 200)
print()
print("Наличие товаров на складе:")
print(f'{Printer.get_type()} - ', sklad.type_quantity("printer"))
print(f'{Scaner.get_type()} - ', sklad.type_quantity("scaner"))
print()
print("Наличие hp2020:\n", sklad.model_quantity("hp2020"))

print()
sklad.show_equipment()
print()
print(f"Объем доступного хранения {sklad.free_storage_area} квадратных метров")

