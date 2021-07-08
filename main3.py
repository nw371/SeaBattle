import copy
from random import randint

class GameException(Exception):
    pass
    #raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))
    #ValueError: empty range for randrange()(0, 0, 0)

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
    def __init__(self, decks):#origin, size, orientation):
        """
        Создаёт объект корабля
        :param origin: Нос корабля. Точка отсчёта
        :param size: Размер корабля в точках
        :param orientation: Расположение корабля 1=вертикаль, 0=горизонталь
        """
        # self.origin = origin
        # self.size = size
        # self.orientation = orientation
        self.decks = decks

    @property
    def build_ship(self):
        """
        Создаёт корабль отсчитывая размер от носа по направлению ориентации
        :return: Координаты всех палуб корабля в виде списка объектов точек
        """
        # while len(self.decks) < self.size:
        #
        #     self.decks.append(copy.deepcopy(self.origin))
        #
        #     if self.orientation == 1:
        #         self.origin.v += 1
        #
        #     elif self.orientation == 0:
        #         self.origin.h += 1

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

    def show_battlefield(self, mode=0):
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

    def add_ship(self, ship):
        """
        Добавляет точки корабля в список поля заменяя сымвол поля на сымвол корабля.
        :param ship: Объект корабля
        """
        print("THIS IS SHIP ", ship)
        for i in ship:
            self.btfld[i.v][i.h] = self.ship_sym
            self.define_blinds(i)

    def define_blinds(self, blind):
        """
        Выставвляет "мёртвую зону" вокруг корабля
        :param blind: Объект точки вокруг которой нужна мёртвая зона
        """
        for i in range(-1, 2):
            for t in range(-1, 2):
                if 0 <= blind.v + i < self.size and 0 <= blind.h + t < self.size:
                    if self.btfld[blind.v + i][blind.h + t] != self.ship_sym:
                        self.blind_spots.append(Dot(blind.v + i, blind.h + t))
                        # следующая строка на время разработки, чтобы видеть правильность мёртвой зоны
                        self.btfld[blind.v + i][blind.h + t] = self.blind_sym


class Game:
    def __init__(self):
        """
        Объект игры
        """
        self.game = 0
        self.size = 6
        self.fleet = [3, 2, 2, 1, 1, 1, 1]

    def construct_board(self):
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
                        print("POOL DATA: ",h,dot,v,point)
                        avlbl_pool.append(Dot(v, h))

            while True:
                gl = randint(0, len(avlbl_pool) - 1)
                print("THIS IS BOARD: ", brd.btfld)
                print("AVALABLE POOL", avlbl_pool)
                print("SIZE OF POOL", len(avlbl_pool))
                if avlbl_pool[gl].v < limit or avlbl_pool[gl].h < limit:

                    if decks == 3:
                        if (((avlbl_pool[gl + decks - 1].h - avlbl_pool[gl + decks - 2].h == 1 and
                              avlbl_pool[gl + decks - 2].h - avlbl_pool[gl + decks - 3].h == 1) or
                             (avlbl_pool[gl + decks - 1].v - avlbl_pool[gl + decks - 2].v == 1 and
                              avlbl_pool[gl + decks - 2].v - avlbl_pool[gl + decks - 3].v == 1))):
                            brd.add_ship(Ship(avlbl_pool[gl:gl+decks]).build_ship)
                            print("3 decks", avlbl_pool[gl], avlbl_pool[gl + 1], avlbl_pool[gl + 2])
                            print("ORIENT: ",orient)
                            break

                    if decks == 2:
                        if ((avlbl_pool[gl + decks - 1].h - avlbl_pool[gl + decks - 2].h == 1) or
                                (avlbl_pool[gl + decks - 1].v - avlbl_pool[gl + decks - 2].v == 1)):
                            brd.add_ship(Ship(avlbl_pool[gl:gl + decks]).build_ship)
                            print("2 decks", avlbl_pool[gl], avlbl_pool[gl + 1])
                            print("ORIENT: ", orient)
                            break

                    if decks == 1:
                        brd.add_ship(Ship(avlbl_pool[gl:gl + decks]).build_ship)
                        print("1 deck", avlbl_pool[gl])
                        print("ORIENT: ", orient)
                        break

            # if orient and avlbl_pool[gl].h < avlbl_pool[gl].v and decks > 1:
            #     orient = not(orient)
            #
            # elif not orient and avlbl_pool[gl].h > avlbl_pool[gl].v:
            #     orient = not(orient)
            #
            # ref_point = avlbl_pool[gl]
            # print("REF ", ref_point)
            #
            # brd.add_ship(Ship(ref_point, decks, orient).build_ship)

        brd.show_battlefield()
        return brd


g1 = Game()
g1.construct_board()
