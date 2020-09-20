from itertools import zip_longest

def saddle_points(matrix):
    maxes = [max(row) for row in matrix]
    mins = [
             min(column) for column in
                [list(x) for x in list(zip_longest(*matrix))]
            ]
    return [num for num in maxes if num in mins]
