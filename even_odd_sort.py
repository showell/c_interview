def qsort(get_elem, put_elem, lo, hi, reverse):
    def partition(lo, hi):
        pivot = get_elem(hi)
        i = lo
        mid = lo
        for i in range(lo, hi):
            less_than = get_elem(i) <= pivot
            if reverse:
                less_than = not less_than
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

def even_odd_sort(lst):
    def get_even_elem(i):
        return lst[i*2]

    def put_even_elem(i, v):
        lst[i*2] = v

    def get_odd_elem(i):
        return lst[i*2+1]

    def put_odd_elem(i, v):
        lst[i*2 + 1] = v

    qsort(get_even_elem, put_even_elem, 0, (len(lst)-1) / 2, False)
    qsort(get_odd_elem, put_odd_elem, 0, len(lst) / 2 - 1, True)

lst = [4, 1, 2, 3, 0, 5, 6, 7]
even_odd_sort(lst)
print lst
