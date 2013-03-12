def test():
    assert 1.0 == probability_of_alive(5, 0, 0, 0)
    assert 0.5 == probability_of_alive(5, 1, 0, 0)
    assert 0.75 == probability_of_alive(5, 1, 1, 4)
    assert 1.0 == probability_of_alive(5, 2, 2, 2)
    assert 0.9375 == probability_of_alive(5, 3, 2, 2)

def probability_of_alive(N, n, x, y):
    dct = get_survival_dct(N, n)
    return 1.0 * lookup(dct, N, x, y) / (4**n)

def get_survival_dct(N, n):
    # This returns a dictionary where keys
    # are (x,y) tuples and it only has values
    # for the WNW octant of the island, since
    # other values can be calculated via
    # horizontal, vertical, and diagonal
    # reflection.  Values are probabilities
    # of survival * (4**n).
    dct = {}
    for i in range((N+1)/2):
        for j in range(i, (N+1)/2):
            dct[(i,j)] = 1
    for step in range(n):
        new_dct = {}
        for i in range((N+1)/2):
            for j in range(i, (N+1)/2):
                new_dct[(i,j)] = \
                    lookup(dct, N, i+1, j) + \
                    lookup(dct, N, i, j+1) + \
                    lookup(dct, N, i-1, j) + \
                    lookup(dct, N, i, j-1)
        dct = new_dct
    return dct

def lookup(dct, N, i, j):
    if N - i - 1< i: i = N - i - 1
    if N - j - 1< j: j = N - j - 1
    if j < i: i, j = j, i
    return dct.get((i,j), 0)

def print_probability_matrix(N, dct):
    for i in range(N):
        print [lookup(dct, N, i, j) for j in range(N)]

N = 5
for n in range(4):
    dct = get_survival_dct(N, n)
    print_probability_matrix(N, dct)
    print
test()

            

