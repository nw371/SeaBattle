def surrounding_matrix_generator():
    dots = [1,5]
    for i in range(-1,2):
        for t in range(-1,2):
            print(dots[0]+i, dots[1]+t)
            #print(i,t)


surrounding_matrix_generator()