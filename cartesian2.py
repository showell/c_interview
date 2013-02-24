def test():
    strings = [
        'abcd',
        '123',
        'XY'
    ]
    for s in cartesian(strings):
        print s

def cartesian(strings):
    max_indexes = map(len, strings)
    for indexes in odometer(max_indexes):
        letters = [strings[i][j] for i, j in enumerate(indexes)]
        yield ''.join(letters)

def odometer(max_indexes):
    odometer = [0] * len(max_indexes)
    def advance_odometer():
        i = len(odometer) - 1
        while i >= 0:
            odometer[i] += 1
            if odometer[i] < max_indexes[i]:
                return True
            else:
                # roll over to next index
                odometer[i] = 0
                i -= 1
                if i < 0:
                    return False
    while True:
        yield odometer
        if not advance_odometer():
            break
test()
