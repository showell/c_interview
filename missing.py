# Assume lst has no repeated elements other than
# the duplicates in a pair, but don't assume integers,
# to make it more challenging
def unique(lst):
    lo = 0
    hi = len(lst) - 1
    while True:
        if lo == hi:
            return lst[lo] 
        offset = (hi - lo) / 4 * 2
        mid = lo + offset
        if lst[mid] == lst[mid+1]:
            lo = mid + 2
        else:
            hi = mid

assert 17 == unique([10, 10, 13, 13, 15, 15, 17, 18, 18, 19, 19, 24, 24])
assert 9 == unique([9])
assert 9 == unique([9, 13, 13])
assert 5 == unique([-1, -1, 5])
assert 5 == unique([-1, -1, 3, 3, 5])
