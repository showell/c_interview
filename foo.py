def f(i):
    big = 1024
    small = 16
    if i < big:
        return i
    else:
        i -= big
        return big + f(i / small)

def test():
    last_v = 0
    big_n = 10 * 1000 * 1000
    for i in range(big_n, big_n + 3000000):
        v = f(i)
        if v < last_v:
            raise 'foo'
        if v > last_v:
            print i, v
        last_v = v

test()
