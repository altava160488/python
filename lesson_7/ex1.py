class Matrix:

    def __init__(self, m_list):
        # проверим входной параметр
        try:
            if type(m_list) != type([]) or len(m_list) == 0 or type(m_list[0]) != type([]) or len(m_list[0]) == 0:
                print(f"нужен непустой список списков!")
            else:
                n = len(m_list[0])
                for i in m_list:
                    if len(i) != n:
                        print(f"нужен сисок списков одинаковой длины!")
        except ValueError:
            print("что-то не так с параметром списка..")

        # параметр прошел проверку, инициализируем атрибут
        self.m_list = m_list
        self.p_list = m_list

    def __str__(self):
        s = ""
        for i in self.p_list:
            for j in i:
                s += " " + str(j)
            s += "\n"
        return s

    def __add__(self, other):
        c = []
        for i in range(len(self.m_list)):
            c.append([x + y for x, y in zip(self.m_list[i], other.m_list[i])])
        self.p_list = c
        return Matrix(c)


l = [[1, 2, 3], [12, 23, 34]]
m = [[100, 200, 300], [10, 20, 30]]
n = [[11, 22, 33], [1, 2, 3]]

print(Matrix(l))
print(Matrix(m))
print(Matrix(n))
print(Matrix(l)+Matrix(m)+Matrix(n))
