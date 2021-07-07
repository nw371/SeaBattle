import copy
from random import randint


class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"

class BoardWrongShipException(BoardException):
    pass

class Dot:
    def __init__(self, h, v):
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

        while len(self.decks) < self.size:

            self.decks.append(copy.deepcopy(self.origin))

            if self.oritentation == 1:
                self.origin.v += 1

            elif self.oritentation == 0:
                self.origin.h += 1

        return self.decks

class Board:

    def __init__(self):
        self.ship_sym = "■"
        self.fild_sym = 0
        self.hit_ship_sym = "X"
        self.miss_hit_sym = "Z"
        self.blind_sym = "*"
        self.size = 6
        self.huco = ["А","Б","В","Г","Д","Е"]
        self.separator = " | "
        self.blind_spots = []

        self.btfld = [[self.fild_sym] * self.size for _ in range(self.size)]

    def Showbatlefield(self,mode=0):

        print(" ",*self.huco, sep=self.separator, end=" |\n")
        for i,dot in enumerate(self.btfld):
            print("— | " * 7)
            if mode:
                print(i+1, *[self.fild_sym if x == self.ship_sym else x for x in dot], sep=self.separator,end=" |\n")
            else:
                print(i+1, *dot, sep=self.separator, end=" |\n")

    def Add_Ship(self,ship):

        for i in ship:
            if self.out_of_board(i) or self.is_not_legal(i):
                raise BoardWrongShipException()
        for i in ship:
            self.btfld[i.v-1][i.h-1] = self.ship_sym
            self.Define_blinds(i)

    def Define_blinds(self,blind):


        for i in range(-1, 2):
            for t in range(-1, 2):
                  if 0 <= (blind.v)-1+i < self.size and 0 <= (blind.h)-1+t < self.size:
                    if self.btfld[blind.v-1+i][blind.h-1+t] != self.ship_sym:
                        self.blind_spots.append(Dot((blind.v)-1+i,(blind.h)-1+t))
                        self.btfld[blind.v -1+ i][blind.h -1+ t] = self.blind_sym

    def out_of_board(self, check):
        return not((0<= check.v-1 < self.size) and (0 <= check.h-1 < self.size))

    def is_not_legal(self,check):
        return not ((self.btfld[check.v-1][check.h-1] != self.ship_sym) and (check not in self.blind_spots))


class Game:
    def __init__(self):
        self.game = 0
        self.size = 6
        self.fleet = [3]#,2,2,1,1,1,1]

    # def Create_board(self):
    #     brd = Board()
    #     for i in self.fleet:
    #         brd.Add_Ship(self.Construct_ship(i))
    #     brd.Showbatlefield()

    def Construct_ship(self):
        brd = Board()
        #for i in self.fleet:
        limit = self.size - 3
        orient = randint(0,1)
        h = randint(1, limit)
        v = randint(1, self.size)
        if orient:
            h,v = v,h

        ship = Ship(Dot(h,v),3, orient)
        brd.Add_Ship(ship.build_ship)
        avlbl_pool = []
        print(brd.btfld)
        for h, dot in enumerate(brd.btfld):
            for v, point in enumerate(dot):
                if brd.btfld[h][v] == 0 and h < limit+3 and v < limit+3:
                    avlbl_pool.append([h, v])

        print(*avlbl_pool, sep="\n")
        print(len(avlbl_pool))

        brd.Showbatlefield()



        #print(ship.build_ship)
        #return ship.build_ship



# d1 = Dot(2,2)
# print(d1)
# s1 = Ship(d1,3,1)
# s1.build_ship
# b1 = Board()
# b1.Showbatlefield()
# b1.Add_Ship(s1.build_ship)
# b1.Showbatlefield()
# print(len(b1.blind_spots))
g1 = Game()
# print(g1.Construct_ship())
g1.Construct_ship()
# g1.Create_board()