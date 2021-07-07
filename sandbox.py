def Construct_ship(self):
    brd = Board()
    avlbl_pool = []
    print(brd.btfld)
    for h, dot in enumerate(brd.btfld):
        for v, point in enumerate(dot):
            if brd.btfld[h][v] == 0:
                avlbl_pool.append([h, v])

    print(*avlbl_pool, sep="\n")
    print(len(avlbl_pool[2]))
    print((avlbl_pool[randint(1, limit)]))

    for i in self.fleet:
        limit = self.size - i
        print(i)

    def Create_board(self):
        brd = Board()
        for i in self.fleet:
            brd.Add_Ship(self.Construct_ship(i))
        brd.Showbatlefield()

    def Construct_ship(self,decks=3):
        limit = self.size - decks
        ship = Ship(Dot(randint(1, limit), randint(1,limit)),decks, randint(0,1))
        #print(ship.build_ship)
        return ship.build_ship


# def surrounding_matrix_generator():
#     dots = [1,5]
#     for i in range(-1,2):
#         for t in range(-1,2):
#             print("Dots ",dots[0]+i, dots[1]+t)
#             print("i and t ",i,t)
#
# surrounding_matrix_generator()

# coordinates = {
#     "А": [0, 0, 0, 0, 0, 0],
#     "Б": [0, 0, 0, 0, 0, 0],
#     "В": [0, 0, 0, 0, 0, 0],
#     "Г": [0, 0, 0, 0, 0, 0],
#     "Д": [0, 0, 0, 0, 0, 0],
#     "Е": [0, 0, 0, 0, 0, 0]
# }
#
# dkey =[key for key in coordinates.keys()][2]
# print([key for key in coordinates.keys()][0])
# print(dkey)