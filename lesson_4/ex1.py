from sys import argv

name, hours, tax, bonus = argv


def f_salary(p_hrs, p_tax, p_bns):
    """

    Функция возвращает значение заработной платы по формуле - (p_hrs * p_tax) + p_bns,
    где
        p_hrs - выработка в часах
        p_tax - ставка в час
        p_bns - премия

    """
    try:
        return (int(p_hrs) * float(p_tax)) + float(p_bns)
    except ValueError:
        return 'Формат вводимых данных неверен'


print(f_salary(hours, tax, bonus))
