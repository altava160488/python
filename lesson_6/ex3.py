class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


a = Position('Иван', 'Петров', 'учитель', 50000, 10000)
print(f'Господин {a.get_full_name()} должен получить {a.get_total_income()} рублей')
