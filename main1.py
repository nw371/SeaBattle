import copy


class Dot:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def __eq__(self, other):
        return self.v == other.v and self.h == other.h

    def __repr__(self):
        return f'Точка({self.v},{self.h})'

so4 = Dot(2,3)
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


s1 = Ship(so4,4,"h")
print(s1.build_ship())
print(len(s1.build_ship()))