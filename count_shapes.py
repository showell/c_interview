# In this solution as soon as we find a 1, we replace
# all the elements in the shape with 2 to avoid double
# counting the 1s.  Otherwise, it's simple iteration.  The
# current solution overwrites the matrix, but you could
# modify it easily to make its own copy of the matrix.
def count_shapes(m):
    num_shapes = 0
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c] == 1:
                fill_shape_with_twos(m, r, c)
                num_shapes += 1

    # restore the original values
    for r in range(len(m)):
        for c in range(len(m[0])):
            m[r][c] = m[r][c] / 2
    return num_shapes

def fill_shape_with_twos(m, r, c):
    m[r][c] = 2
    if r > 0 and m[r-1][c] == 1:
        fill_shape_with_twos(m, r-1, c)
    if r + 1 < len(m) and m[r+1][c] == 1:
        fill_shape_with_twos(m, r+1, c)
    if c > 0 and m[r][c-1] == 1:
        fill_shape_with_twos(m, r, c-1)
    if c + 1 < len(m[0]) and m[r][c+1] == 1:
        fill_shape_with_twos(m, r, c+1)


test_matrix = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
]

test_matrix2 = [
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 1, 0],
]

test_matrix3 = [
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1],
]

print count_shapes(test_matrix)
print count_shapes(test_matrix2)
print count_shapes(test_matrix3)

