class GameExceptions(Exception):
    pass

# class ValueError(GameExceptions):
#     def __init__(self, message):
#         self.message = message
#         if self.message == "1 is not in list":
#             pass

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
        for i in range(0,(int(len(ship)/2))):
            self.btfld[ship[i][0]-1][ship[i][1]-1] = 1

    def place_blind_spots(self):
        control_line = 0
        for rows in self.btfld:
            try:
                dot_index = rows.index(1)
                #if control_line == 0:
                print(f"This is rows: {self.btfld.index(rows)}")
                    # (rows-1)[dot_index-1] = 8
                rows[dot_index-1] = 8
                rows[dot_index+1] = 8
            except ValueError as e:
                print(f"Error happened: {e}")

                continue


    def __repr__(self):
        print('\n'.join(map(str, self.btfld)))
        return f"Поле битвы"



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
bf1.place_blind_spots()
print(bf1)
print(bf1.place_blind_spots())

class Game:
    pass
