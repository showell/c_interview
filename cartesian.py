def cartesian(lst):
    if not lst: return
    def f(i, prefix):
        if i == len(lst) - 1:
            for c in lst[i]:
                yield prefix + c
        else:
            for c in lst[i]:
                for s in f(i+1, prefix+c):
                    yield s
    for s in f(0, ''):
        yield s
        
strings = [
    'abcd',
    '123',
    'XY'
]
for s in cartesian(strings):
    print s
