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
    __list_to_print = []

    def __init__(self):
        self.v_size = 6
        self.h_size = 6

    def __repr__(self):
        return f"Поле битвы"
        pass


bf1 = Battlefield()
print(bf1)


class Ship:
    def __init__(self, v_origin, h_origin, size, orientation):
        self.origin = [v_origin, h_origin]
        self.size = size
        self.set_orientation(orientation)
        self.ship = []

    def build_ship(self):
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

s1 = Ship(2,2,4,"v")
print(s1.orientation)
print(s1.build_ship())

class Game:
    pass

