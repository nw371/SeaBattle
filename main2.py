class Board:
    coordinates = {
        "А": [0,0,0,0,0,0],
        "Б": [0,0,0,0,0,0],
        "В": [0,0,0,0,0,0],
        "Г": [0,0,0,0,0,0],
        "Д": [0,0,0,0,0,0],
        "Е": [0,0,0,0,0,0]
    }

    def __init__(self):
        pass

    def form_field(self):
        row_to_print = [" "]
        for i in self.coordinates.keys():
            row_to_print.append(i)
            #row_to_print.append(" | ")

        print(*row_to_print, sep=" | ", end=" |\n")
        for i in self.coordinates.keys():
            print([key for key in self.coordinates.keys()].index(i)+1, *self.coordinates[i], sep= " | ", end=" |\n")





b1 =Board()
b1.form_field()

# class Gameboard:
#     v_coord = ["А", "Б", "В", "Г", "Д", "Е"]
#     h_coord = [1, 2, 3, 4, 5, 6]
#     v_sep = " | "
#     h_sep = "--"
#     empt_field = "О"
#     shp_filed = "■"
#     miss_field = "-"
#     hit_field = "+"
#     gm_board = []
#     brd_row = []
#     def __init__(self):
#         pass
#
#     def Createboard(self):
#         self.brd_row.append(self.v_sep * 2)
#         for i in self.v_coord:
#             self.brd_row.append(i)
#             self.brd_row.append(self.v_sep)
#
#         self.gm_board.append(self.brd_row.copy())
#
#         for i in self.h_coord:
#             self.brd_row = []
#             self.brd_row.append(i)
#             for x in range(0,6):
#                 self.brd_row.append(self.v_sep)
#                 self.brd_row.append(self.empt_field)
#             self.brd_row.append(self.v_sep)
#             self.gm_board.append(self.brd_row.copy())
#         unpacked_poard = print(*self.gm_board,sep="\n")
#         #return "\n".join(map(str, self.gm_board))
#         return  unpacked_poard
# gmb1=Gameboard()
# print(gmb1.Createboard())

