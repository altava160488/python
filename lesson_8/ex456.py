from abc import ABC, abstractmethod

class Stock:

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.warehouse = {}

    # общий объем хранения в куб.м.(30% помещения на служебно-хозяйственные нужды)
    @staticmethod
    def storage_area(length, width, height):
        return length * width * height * 0.7

    # доступный объем хранения в куб.м.
    @property
    def free_storage_area(self):
        s = 0
        for v in self.warehouse.values():
            s += v["capacity"]
        return Stock.storage_area(self.height, self.width, self.length) - s

    def imprt(self, equipment):
        '''
        Метод фиксации прихода оргтехники на слад

        :param equipment: объект класса Equipment
        :return: None
        '''
        try:
            x = int(self.free_storage_area // (equipment.capacity))
            if x == 0:
                print("Мест на складе больше нет!")
                return
            self.warehouse[equipment.serial_number] = {}
            self.warehouse[equipment.serial_number]["type"] = equipment.get_type()
            self.warehouse[equipment.serial_number]["model"] = equipment.model
            self.warehouse[equipment.serial_number]["capacity"] = equipment.capacity
        except ValueError as err:
            print(err)


    def exprt(self, serial_number):
        '''
        Метод фиксации передачи оргтехники из склада

        :param serial_number: идентификатор оргтехники
        :return: None
        '''
        try:
            del self.warehouse[serial_number]
        except KeyError:
            pass

    def show_equipment(self):
        '''
        Вывод на экран всего что есть на складе

        :return: None
        '''
        types = []
        for v in self.warehouse.values():
            if v["type"] not in types: types.append(v["type"])
        if len(types) == 0: return

        model_type = {}
        for v in self.warehouse.values():
            model_type[v["model"]] = v["type"]

        print("Состояние склада:")
        for t in types:
            m = {}
            qt = 0
            for k, v in model_type.items():
                if v == t:
                    qm = 0
                    for i in self.warehouse.values():
                        if i["model"] == k and i["type"] == v:
                            qm += 1
                            qt += 1
                    m[k] = qm
            print(f"--- {t}: {qt} шт.")
            for i, j in m.items():
                print(i, j)

        print(f"Объем доступного хранения {self.free_storage_area} куб.метров")


    def show_seiral_number(self, model = None, type = None):
        for k, v in self.warehouse.items():
            print(f"номер: {k} модель: {v['model']} тип: {v['type']}")



class Equipment(ABC):

    number = 0

    def __init__(self, model, length = 100, width = 100, height = 100, color_print = False):
        self.model = model
        self.width = width
        self.length = length
        self.height = height
        Equipment.number += 1
        self.serial_number = Equipment.number

    @abstractmethod
    def action(self):
        print("Техника должна что-то делать")

    @property
    def capacity(self):
        return self.width * self.length * self.height * 0.0000001 # куб.м.

    @classmethod
    def get_type(cls):
        return cls.get_type_val("Оргтехника")

    @classmethod
    def get_type_val(cls, arg):
        return arg


class Printer(Equipment):

    def __init__(self, model, length = 100, width = 100, height = 100, color_print = True):
        super().__init__(model, length, width, height, color_print)

    def action(self):
        print(f"выводит печать на бумагу")

    @classmethod
    def get_type(cls):
        return cls.get_type_val("Принтер")

class Scaner(Equipment):

    def action(self):
        print(f"считывает изображение на бумаге для создания его электронной копии")

    @classmethod
    def get_type(cls):
        return cls.get_type_val("Сканер")

class Xerox(Equipment):

    def action(self):
        print(f"копирует изображение на бумаге")

    @classmethod
    def get_type(cls):
        return cls.get_type_val("Ксерокс")

s = Stock(200,200,200)
print(f"Объем хранения {Stock.storage_area(200, 200, 200)} куб.метров")
print(f"Объем доступного хранения {s.free_storage_area} куб.метров")

while True:
    begin = input("Хотите ввести товар? Y/N\n")
    if begin.upper() == 'N' : exit()
    if begin.upper() == 'Y' : break

while True:
    while True:
        equip_type = input("Введите тип оргтехники:\n(p - Принтер; s - Сканер; x - Ксерокс)\n")
        if equip_type.lower() in ['p', 's', 'x'] : break

    equip_model = input("Введите модель:\n")

    while True:
        equip_capacity = input("Введите физические параметры в см через дефис: длина-ширина-высота\nили нажимите на Enter, если хотите оставить размеры по-умолчанию(1м-1м-1м)\n")
        try:
            equip_params = list(map(int,equip_capacity))
            if len(equip_params) == 0: break
            if len(l) != 3 : print("Неверные длина-ширина-высота коробки")
        except:
            print("Введены неверные данные")

    while True:
        try:
            equip_quantity = int(input("Введите количество:\n"))
            break
        except:
            pass


    for _ in range(equip_quantity):
        if equip_type.lower() == 'p':
            if len(equip_params) == 0: e = Printer(equip_model)
            else: e = Printer(equip_model, equip_params[0], equip_params[1], equip_params[2])
        elif equip_type.lower() == 's':
            if len(equip_params) == 0: e = Scaner(equip_model)
            else: e = Scaner(equip_model, equip_params[0], equip_params[1], equip_params[2])
        else:
            if len(equip_params) == 0: e = Xerox(equip_model)
            else: e = Xerox(equip_model, equip_params[0], equip_params[1], equip_params[2])
        s.imprt(e)

    n = input("Хотите еще добавить товар? Y/N\n")
    if n.lower() == 'n':
        break
    if n.lower() != 'y':
        print("Нажмите на клавишу с буквой 'y'")

s.show_equipment()

while True:
    if len(s.warehouse) == 0 : break
    r = input("Хотите списать товар? Y/N\n")
    if r.lower() == 'n':
        s.show_equipment()
        break
    if r.lower() == 'y':
        s.show_seiral_number()
        try:
            a = int(input("Укажите номер товара:\n"))
            s.exprt(a)
        except ValueError:
            print("Номер товара неверен!")
