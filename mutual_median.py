def nth_smallest(lst1, lo1, hi1, lst2, lo2, hi2, n):
    if lo1 == hi1:
        return lst2[lo2+n]
    if lo2 == hi2:
        return lst1[lo1+n]
    if n == 0:
        return min(lst1[lo1], lst2[lo2])
    offset1 = min([n/2, hi1 - lo1 - 1])
    offset2 = min([n/2, hi2 - lo2 - 1])
    print offset1, offset2
    if lst1[lo1+offset1] < lst2[lo2+offset2]:
        return nth_smallest(
            lst1, lo1+offset1+1, hi1,
            lst2, lo2, hi2,
            n-offset1-1)
    else:
        return nth_smallest(
            lst1, lo1, hi1,
            lst2, lo2+offset2+1, hi2,
            n-offset2-1)

def mutual_median(l1, l2):
    n = len(l1) + len(l2)
    mid = n / 2
    return nth_smallest(l1, 0, len(l1), l2, 0, len(l2), mid)

lst1 = list(range(100))
lst2 = range(-999, -980)
median = mutual_median(lst1, lst2)
print 'answer', median
