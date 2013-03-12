def qsort(get_elem, put_elem, lo, hi):
    def partition(lo, hi):
        pivot = get_elem(hi)
        i = lo
        mid = lo
        for i in range(lo, hi):
            less_than = get_elem(i) <= pivot
            if less_than:
                if mid < i:
                    tmp = get_elem(i)
                    put_elem(i, get_elem(mid))
                    put_elem(mid, tmp)
                mid += 1
        if mid < hi:
            tmp = get_elem(mid)
            put_elem(mid, get_elem(hi))
            put_elem(hi, tmp)
        return mid

    def _sort(lo, hi):
        if lo >= hi:
            return
        mid = partition(lo, hi)
        _sort(lo, mid - 1)
        _sort(mid + 1, hi)

    _sort(lo, hi)

def zig_zag_sort(lst):
    n = len(lst)
    def pos(i):
        if i < n / 2:
            return i * 2 + 1
        else:
            return (n - i - 1) * 2
        return i
    def get(i):
        return lst[pos(i)]
    def put(i, v):
        lst[pos(i)] = v
    qsort(get, put, 0, n-1)

lst = [4, 1, 2, 3, 0, 5, 6, 7, 8]
zig_zag_sort(lst)
print lst
