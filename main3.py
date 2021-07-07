import copy
from random import randint


class Dot:
    def __init__(self, h, v):
        """
        Создаёт обьект точки
        :param h: горизонтальная координата
        :param v: вертикальная координата
        """
        self.v = v
        self.h = h

    def __eq__(self, other):
        """
        Сравнение двух точек
        :param other: координаты точки для сравнения
        :return: Boolean
        """
        return self.v == other.v and self.h == other.h

    def __repr__(self):
        """
        Выводит точку на печать
        :return: String
        """
        return f'Точка({self.v},{self.h})'

    def swap(self):
        """
        Переставляет местами координаты у точки.
        """
        self.v, self.h = self.h, self.v


class Ship:
    decks = []

    def __init__(self, origin, size, orientation):
        """
        Создаёт объект корабля
        :param origin: Нос корабля. Точка отсчёта
        :param size: Размер корабля в точках
        :param orientation: Расположение корабля 1=вертикаль, 0=горизонталь
        """
        self.origin = origin
        self.size = size
        self.oritentation = orientation

    @property
    def build_ship(self):
        """
        Создаёт корабль отсчитывая размер от носа по направлению ориентации
        :return: Координаты всех палуб корабля в виде списка объектов точек
        """
        while len(self.decks) < self.size:

            self.decks.append(copy.deepcopy(self.origin))

            if self.oritentation == 1:
                self.origin.v += 1

            elif self.oritentation == 0:
                self.origin.h += 1

        return self.decks


class Board:

    def __init__(self):
        """
        Создаёт объект доски
        Все переменные собраны в конструкторе класса, для лёгкости управления
        """
        self.ship_sym = "■"
        self.fild_sym = 0
        self.hit_ship_sym = "X"
        self.miss_hit_sym = "Z"
        self.blind_sym = "*"
        self.size = 6
        self.huco = ["А", "Б", "В", "Г", "Д", "Е"]
        self.separator = " | "
        self.blind_spots = []
        self.btfld = [[self.fild_sym] * self.size for _ in range(self.size)]

    def Showbatlefield(self, mode=0):
        """
        Отрисовывает играовое поле
        :param mode: Видимость кораблей на поле: 1 спрятаны, 0 видны
        """
        print(" ", *self.huco, sep=self.separator, end=" |\n")
        for i, dot in enumerate(self.btfld):
            print("— | " * 7)
            if mode:
                print(i + 1, *[self.fild_sym if x == self.ship_sym else x for x in dot], sep=self.separator, end=" |\n")
            else:
                print(i + 1, *dot, sep=self.separator, end=" |\n")

    def Add_Ship(self, ship):
        """
        Добавляет точки корабля в список поля
        :param ship: Объект корабля
        """
        for i in ship:
            self.btfld[i.v - 1][i.h - 1] = self.ship_sym
            self.Define_blinds(i)

    def Define_blinds(self, blind):
        """
        Выставвляет "мёртвую зону" вокруг корабля
        :param blind: Объект точки вокруг которой нужна мёртвая зона
        """
        for i in range(-1, 2):
            for t in range(-1, 2):
                if 0 <= (blind.v) - 1 + i < self.size and 0 <= (blind.h) - 1 + t < self.size:
                    if self.btfld[blind.v - 1 + i][blind.h - 1 + t] != self.ship_sym:
                        self.blind_spots.append(Dot((blind.v) - 1 + i, (blind.h) - 1 + t))
                        # следующая строка на время разработки, чтобы видеть правильность мёртвой зоны
                        self.btfld[blind.v - 1 + i][blind.h - 1 + t] = self.blind_sym


class Game:
    def __init__(self):
        """
        Объект игры
        """
        self.game = 0
        self.size = 6
        self.fleet = [3, 2, 2, 1, 1, 1, 1]

    def Construct_board(self):
        """
        Создаёт игровое поле, и размещает на нём корабли.
        :return: Игровое поле с кораблями
        """
        brd = Board()

        for decks in self.fleet:

            avlbl_pool = []
            limit = self.size - decks
            orient = randint(0, 1)

            for h, dot in enumerate(brd.btfld):
                for v, point in enumerate(dot):
                    if point == 0:
                        avlbl_pool.append(Dot(h + 1, v + 1))

            while True:
                gl = randint(0, len(avlbl_pool) - 1)

                print("AVALABLE POOL", avlbl_pool)
                if (avlbl_pool[gl].v < limit or avlbl_pool[gl].h < limit):
                    if decks == 3:
                        if (((avlbl_pool[gl + decks - 1].h - avlbl_pool[gl + decks - 2].h == 1 and avlbl_pool[
                            gl + decks - 2].h - avlbl_pool[gl + decks - 3].h == 1) or (
                                     avlbl_pool[gl + decks - 1].v - avlbl_pool[gl + decks - 2].v == 1 and avlbl_pool[
                                 gl + decks - 2].v - avlbl_pool[
                                         gl + decks - 3].v == 1))):
                            print("3 decks", avlbl_pool[gl], avlbl_pool[gl + 1], avlbl_pool[gl + 2])

                            break
                    if decks == 2:
                        if ((avlbl_pool[gl + decks - 1].h - avlbl_pool[gl + decks - 2].h == 1) or (
                                avlbl_pool[gl + decks - 1].v - avlbl_pool[gl + decks - 2].v == 1)):
                            print("2 decks", avlbl_pool[gl], avlbl_pool[gl + 1])
                            break
                    if decks == 1:
                        print("1 deck", avlbl_pool[gl])
                        break

            if orient and avlbl_pool[gl].h > avlbl_pool[gl].v and decks > 1:
                avlbl_pool[gl].swap
            elif not orient and avlbl_pool[gl].h < avlbl_pool[gl].v:
                avlbl_pool[gl].swap
            if avlbl_pool[gl].v == 0:
                avlbl_pool[gl].v += 1
            if avlbl_pool[gl].h == 0:
                avlbl_pool[gl].h += 1
            ref_point = avlbl_pool[gl]

            brd.Add_Ship(Ship(ref_point, decks, orient).build_ship)

        brd.Showbatlefield()
        return brd



g1 = Game()
g1.Construct_board()

