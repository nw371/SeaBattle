# def surrounding_matrix_generator():
#     dots = [1,5]
#     for i in range(-1,2):
#         for t in range(-1,2):
#             print(dots[0]+i, dots[1]+t)
#             #print(i,t)
#
# surrounding_matrix_generator()

coordinates = {
    "А": [0, 0, 0, 0, 0, 0],
    "Б": [0, 0, 0, 0, 0, 0],
    "В": [0, 0, 0, 0, 0, 0],
    "Г": [0, 0, 0, 0, 0, 0],
    "Д": [0, 0, 0, 0, 0, 0],
    "Е": [0, 0, 0, 0, 0, 0]
}

dkey =[key for key in coordinates.keys()][2]
print([key for key in coordinates.keys()][0])
print(dkey)