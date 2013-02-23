def sorted2(lst, key1, key2):
    def f(v): return (key1(v), key2(v))
    return sorted(lst, key=f)

list = [207, 101, 103, 104, 208]
key1 = lambda i: i / 100
key2 = lambda i: 10 - (i % 100)
print sorted2(list, key1, key2)
