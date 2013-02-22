def search(m, v):
    # Search for v in a matrix where
    # it is guaranteed that
    #  m[r+1][c] >= m[r][c] and
    #  m[r][c+1] >= m[r][c]
    # Start in the upper right corner
    # and go left or down.

    r = 0
    c = len(m[0]) - 1
    while True:
        if m[r][c] == v:
            return (r, c)
        if v < m[r][c]:
            # go left (column eliminated)
            c -= 1
            if c < 0: return None
        else:
            # go down (row eliminated)
            r += 1
            if r >= len(m): return None
    
test_matrix = [
    [1, 2, 3, 14, 20],
    [4, 6, 10, 15, 30],
    [5, 7, 12, 16, 42],
    [8, 9, 13, 27, 43],
]

for r in range(len(test_matrix)):
    for c in range(len(test_matrix)):
        v = test_matrix[r][c]
        assert search(test_matrix, v) == (r, c)
assert search(test_matrix, 99) is None

