def test():
    # Assume we have a list that is sorted, except that is
    # rotated by an unknown offset.  First, we build a helper
    # function to determine the position of the smallest
    # element in the list (aka the rotation offset).
    assert 0 == pos_smallest_element([0, 0, 0])
    assert 0 == pos_smallest_element([0, 1, 2])
    assert 1 == pos_smallest_element([2, 0, 1])
    assert 2 == pos_smallest_element([1, 2, 0])
    assert 3 == pos_smallest_element([4, 5, 6, 0, 1, 2, 3])
    # Once we know the smallest element, it's pretty trivial
    # to implement search in terms of a generic binary search.
    test_lst = [10, 2, 4, 6, 8]
    assert 0 == search(10, test_lst)
    assert 1 == search(2, test_lst)
    assert 2 == search(4, test_lst)
    assert 3 == search(6, test_lst)
    assert 4 == search(8, test_lst)
    assert None == search(0, test_lst)
    assert None == search(7, test_lst)
    assert None == search(11, test_lst)

def bsearch(val, lowest, highest, get):
    # A generic binary search uses a get() function, so
    # that we're not coupled to the storage scheme.  We
    # just need a guarantee that get(a) <= get(b) when a <= b.
    def f(low, high):
        if low > high:
            return None
        mid = (low+high) / 2
        mid_val = get(mid)
        if val == mid_val:
            return mid
        if val < mid_val:
            return f(low, mid-1)
        else:
            return f(mid+1, high)
    return f(lowest, highest)

def search(val, lst):
    offset = pos_smallest_element(lst)
    def actual_pos(i):
        return (i+offset) % len(lst)
    def get(i):
        return lst[actual_pos(i)]
    answer = bsearch(val, 0, len(lst)-1, get)
    if answer is None:
        return None
    return actual_pos(answer)

def pos_smallest_element(lst):
    def pos(low, high):
        if low == high:
            return low
        if low + 1 == high:
            if lst[low] <= lst[high]:
                return low
            else:
                return high
        mid = (low + high) / 2
        if lst[low] <= lst[mid] <= lst[high]:
            return low
        if lst[low] <= lst[mid]:
            return pos(mid, high)
        else:
            return pos(low, mid)
            
    return pos(0, len(lst) - 1)

test()
