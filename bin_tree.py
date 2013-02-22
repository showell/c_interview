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

def traverse(tree):
    if tree is None:
        return
    left, val, right = tree
    traverse(left)
    print val
    traverse(right)

def tree_height(tree):
    if tree is None:
        return 0
    left, val, right = tree
    lh = tree_height(left)
    rh = tree_height(right)
    return max([lh, rh]) + 1

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tree = create_tree(lst)
print tree
assert 4 == tree_height(tree)
traverse(tree)
