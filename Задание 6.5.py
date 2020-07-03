class Stationery:
    def __init__(self, title="Атрибут для рисования"):
        self.title = title

    def draw(self):
        print(f"Начинаем рисовать! {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Начинаем рисовать! с помощью {self.title} ручки")


class Pencil(Stationery):
    def draw(self):
        print(f"Начинаем рисовать! с помощью {self.title} карандаша")


class Handle(Stationery):
    def draw(self):
        print(f"Начинаем рисовать! с помощью {self.title} маркера")


start = Stationery()
start.draw()
pen = Pen("Синей")
pen.draw()
pencil = Pencil("Черного")
pencil.draw()
handle = Handle("Узкого")
handle.draw()
