# Find the 2nd biggest by solving the general
# problem of finding the Nth largest element in a tree.
# The method is efficient, because it only traverses
# the left side of the tree when the right side
# has fewer than N-1 elements.

def test():
    tree123 = ((None, 1, None), 2, (None, 3, None))
    tree567 = ((None, 5, None), 6, (None, 7, None))
    tree = (tree123, 4, tree567)
    assert 6 == nth_element(tree, 2, 7) # second biggest
    assert 2 == nth_element(tree, 5, 6) # fifth biggest <= 6

def nth_element(tree, n, max):
    # Our inner function tries to return the nth largest
    # element <= max, but the tree might be too small, so we
    # also indicate the number of elements found.
    def nth_element_and_num_checked(tree, n):
        if tree is None:
            return None, 0
        left, val, right = tree
        if val > max:
            n_right = 0
        else:
            # For a big tree, we just recurse on the right tree.
            r_nth, n_right = nth_element_and_num_checked(right, n)
            if n_right == n:
                return r_nth, n
        if val <= max:
            n_right += 1
        # If the right side has exactly n-1 elements, the root
        # value is the solution.
        if n_right == n:
            return val, n
        # When we recurse to the left, we need to find a higher
        # ranking element than nth, depending on how many nodes
        # were on the right side.
        n_left = n - n_right
        result, n_left = nth_element_and_num_checked(left, n_left)
        return result, n_left + n_right
    result, num_checked = nth_element_and_num_checked(tree, n)
    if num_checked == n:
        return result
    else:
        raise Exception("tree too small")
    
test()
