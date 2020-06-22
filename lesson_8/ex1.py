class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_format(cls, date, format):
        '''
        Функция  извлекает день, месяц, год и преобразовывает их тип к типу «Число»

        :param date_str: дата в формате строки дд-мм-гггг
        :return: ответ int
        '''
        try:
            l = list(map(int, date.split('-')))
            if format == 'day':
                return l[0]
            elif format == 'month':
                return l[1]
            elif format == 'year':
                return l[2]
            else:
                print("Неверный формат(day,month,year)!")
        except TypeError:
            print("Значение даты не соответствует шаблону(дд-мм-гггг)!")
        except ValueError:
            print("Что-то пошло не так...",ValueError)

    @staticmethod
    def is_valid(date_str):
        '''
        Фукция проверки валидности даты в строковом представлении

        :param date_str: дата в формате строки дд-мм-гггг
        :return: ответ Trгe/False

        '''
        r = False
        try:
            d = list(map(int, date_str.split('-')))
            if d[1] in range(1, 13):
                if d[1] == 2:
                    r = (d[0] in range(1, 29) or (d[0] == 29 and d[2] % 4 == 0))
                else:
                    r = (d[0] in range(1, 31) or (d[0] == 31 and d[1] in [1, 3, 5, 7, 8, 10, 12]))
        except TypeError:
            print("Дата не соответстует шаблону(дд-мм-гггг)!")
        except ValueError:
            print(ValueError)
            print("Что-то пошло не так..")

        return r


# print(Date.is_valid('06-1982'))

a = Date('06-088-1982')
a.date_format(a.date,'month')
print(a.date_format(a.date,'month'))