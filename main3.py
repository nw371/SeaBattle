import copy

class Dot:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def __eq__(self, other):
        return self.v == other.v and self.h == other.h

    def __repr__(self):
        return f'Точка({self.v},{self.h})'

class Ship:
    decks = []
    def __init__(self,origin,size,orientation):
        self.origin = origin
        self.size = size
        self.oritentation = orientation

    @property
    def build_ship(self):
        self.decks.append(copy.deepcopy(self.origin))

        while len(self.decks) < self.size-1:

            if self.oritentation == 1:
                self.origin.v += 1

            elif self.oritentation == 0:
                self.origin.h += 1

            self.decks.append(copy.deepcopy(self.origin))

        return self.decks

class Board:

    def __init__(self):
        self.ship_sym = "S"
        self.fild_sym = 0
        self.hit_ship_sym = "X"
        self.miss_hit_sym = "Z"
        self.blind_sym = 8
        self.size = 6
        self.huco = ["А","Б","В","Г","Д","Е"]
        self.separator = " | "

        self.btfld = [[self.fild_sym] * self.size for _ in range(self.size)]

    def Showbatlefield(self):
        print(" ",*self.huco, sep=self.separator, end=" |\n")
        for i,dot in enumerate(self.btfld,1):
            print("— | " * 7)
            print(i, *dot, sep=self.separator,end=" |\n")

    def Add_Ship(self,ship):
        print(ship)
        # for i in ship:
        #     print(i)

d1 = Dot(1,2)
s1 = Ship(d1,3,1)
s1.build_ship
b1 = Board()
b1.Showbatlefield()
b1.Add_Ship(s1.build_ship)