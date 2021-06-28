class GameExceptions(Exception):
    pass


class Dot:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def __eq__(self, other):
        return self.v == other.v and self.h == other.h

    def __repr__(self):
        return f'Точка({self.v},{self.h})'


d1 = Dot(6, 5)
d2 = Dot(6, 5)
print(d1)
print(d2)
print(d1 == d2)


class Battlefield:
    btfld = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]
    ]

    def __init__(self):
        self.v_size = 6
        self.h_size = 6


    def place_ship(self,ship):
        for i in range(0,(int(len(ship)/2)-1)):
            self.btfld[ship[i][0]][ship[i][1]] = 1


    def __repr__(self):
        return f"Поле битвы '\n' {self.btfld}"





class Ship:
    def __init__(self, h_origin, v_origin, size, orientation):
        self.origin = [v_origin, h_origin]
        self.size = size
        self.set_orientation(orientation)
        self.ship = []

    def body(self):
        self.ship.append(self.origin.copy())
        for i in range(1, self.size):
            self.origin[self.orientation] += 1
            self.ship.append(self.origin.copy())
        return self.ship

    def set_orientation(self, orientation):
        if orientation == "v":
            self.orientation = 0
        elif orientation == "h":
            self.orientation = 1


s1 = Ship(2, 2, 4, "v")
print(s1.orientation)
print(s1.body())
bf1 = Battlefield()
bf1.place_ship(s1.body())
#print(bf1.place_ship(s1.body()))
print(bf1)


class Game:
    pass
