
def find_min(f, lo_x, hi_x, max_error):
    x0 = lo_x
    x3 = hi_x
    x1 = (2*x0+1*x3) / 3.0
    x2 = (1*x0+2*x3) / 3.0
    while x2 - x1 > max_error:
        if f(x2) > f(x1):
            # The middle is increasing, so
            # prune the right interval.
            x3 = x2
            x2 = x1
            x1 = (x0+x1) / 2.0
        else:
            # The middle is decreasing, so
            # prune the left interval.
            x0 = x1
            x1 = x2
            x2 = (x2+x3) / 2.0
    return x1
        
f = lambda x: (x - 1.5) ** 2
guess = find_min(f, -10, 7, 0.0001)
assert abs(guess - 1.5) < 0.0001

f = lambda x: (x - 3.7) ** 4
guess = find_min(f, 0, 5, 0.00001)
assert abs(guess - 3.7) < 0.00001
