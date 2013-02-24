def test():
    lst = [1,2,3,4,4,5,6,7,7,7,8,9,10,11,12,13,14,15]
    tree = create_tree(lst)
    assert [4,4,5,6,7,7,7,8,9,10,11,12] == list(traverse_range(tree, 4, 12))
    assert [] == list(traverse_range(tree, 16, 100))
    assert lst == list(traverse_range(tree, 0, 100))
    assert [12,13,14] == list(traverse_range(tree, 12, 14))
    assert [7,7,7] == list(traverse_range(tree, 7, 7))

def traverse_range(tree, min, max):
    stack = []
    while tree or stack:
        if tree:
            left, val, right = tree
            if val <= max:
                stack.append(tree)
            tree = left
            if val < min:
                tree = None
        else:
            tree = stack.pop()
            left, val, right = tree
            if val > max:
                return
            if min <= val:
                yield val
            tree = right

# In Python a simple way to represent a binary
# tree is as a tuple: (left_tree, val, right_tree)
def create_tree(lst):
    def _maketree(low, high):
        # Making a balanced tree is simply a matter
        # of taking the middle value as the root
        # and recursively building the subtrees
        # on the left and right.
        if low > high:
            return None
        if low == high:
            return (None, lst[low], None)
        mid = (low + high) / 2
        val = lst[mid]
        left = _maketree(low, mid - 1)
        right = _maketree(mid + 1, high)
        return (left, val, right)
    return _maketree(0, len(lst) - 1)

test()
