class Stationery:

    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print("Start drawing!")


class Pen(Stationery):

    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print(f"The {self.title} is ready to draw!")


class Pencil(Stationery):

    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print(f"The {self.title} is not ready to draw!")


class Handle(Stationery):

    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print(f"The {self.title} needs to be ready!")


t = Stationery("tassel")
p = Pen("pen")
s = Pencil("pencil")
h = Handle("handle")
