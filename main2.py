import copy

class GameExceptions(Exception):
    pass

class OutOfbattlefield(GameExceptions):
    def __str__(self):
        return "Out of coordinates"



class Dot:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def __eq__(self, other):
        return self.v == other.v and self.h == other.h

    def __repr__(self):
        return f'Точка({self.v},{self.h})'

class Ship:
    ship = []
    def __init__(self,origin,size,orientation):
        self.origin = origin
        self.size = size
        self.oritentation = orientation

    def build_ship(self):
        self.ship.append(copy.copy(self.origin))
        while len(self.ship) < self.size:
            if self.oritentation == "v":
                self.origin.v += 1
            elif self.oritentation == "h":
                self.origin.h += 1
            self.ship.append(copy.copy(self.origin))
        return self.ship

class Board:
    ship_sym = "S"
    fild_sym = 0
    hit_ship_sym = "X"
    miss_hit_sym = "Z"
    blind_sym = 8
    coordinates = {
        "А": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym],
        "Б": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym],
        "В": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym],
        "Г": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym],
        "Д": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym],
        "Е": [fild_sym,fild_sym,fild_sym,fild_sym,fild_sym,fild_sym]
    }
    def __init__(self):
        pass

    def form_field(self):
        row_to_print = [" "]
        for i in self.coordinates.keys():
            row_to_print.append(i)

        print(*row_to_print, sep=" | ", end=" |\n")
        for i in self.coordinates.keys():
            print("— | "*7)
            print([key for key in self.coordinates.keys()].index(i)+1, *self.coordinates[i], sep= " | ", end=" |\n")

    def change_dot(self,dot,look):
        print("Check point: ", dot)
        if dot.v-1 < 6 and dot.h-1 < 6:
            print("Check point 2: ", dot)
            v_coord = [key for key in self.coordinates.keys()][dot.v-1]
            if self.coordinates[v_coord][dot.h-1] != "S":
                self.coordinates[v_coord][dot.h-1] = look

    def place_ship(self,ship):
        for i in ship:
            self.change_dot(i,self.ship_sym)
            self.add_blinds(i)

    def add_blinds(self,dot):
        v_coord = [key for key in self.coordinates.keys()][dot.v - 1]
        h_coord = [dot.h-1]
        print(v_coord,h_coord)
        for i in range(-1, 2):
            for t in range(-1, 2):
                print([key for key in self.coordinates.keys()][dot.v - (1+i)],[dot.h-(1+t)])
                print(dot.v - (1+i),dot.h-(1+t))
                dtp = Dot((dot.v)+i,(dot.h)+t)
                self.change_dot(dtp,self.blind_sym)

        # for i in self.coordinates:
        #     for s in self.coordinates[i]:
        #         if s == "S":
        #             print(s,i)


so4 = Dot(2,2)
s1 = Ship(so4,4,"v")

d1 = Dot(2,3)
b1 =Board()
b1.form_field()
b1.change_dot(d1,"X")
b1.form_field()
b1.place_ship(s1.build_ship())
b1.form_field()
#b1.add_blinds(d1)

