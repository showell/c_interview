def test():
    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    tree = create_tree(lst)
    result = []
    traverse_tree(tree, result)
    assert result == lst
    head, tail = add_doubly_linked_list_pointers(tree)
    result = []
    traverse_dll(head, result)
    assert result == lst

def add_doubly_linked_list_pointers(tree):
    if tree is None:
        return None, None

    lhead, ltail = add_doubly_linked_list_pointers(tree.left)
    rhead, rtail = add_doubly_linked_list_pointers(tree.right)

    if lhead:
        ltail.next = tree
        head = lhead
    else:
        head = tree
    tree.prev = ltail

    if rhead:
        rhead.prev = tree
        tail = rtail
    else:
        tail = tree
    tree.next = rhead
        
    return head, tail

def traverse_tree(tree, lst):
    if tree is None:
        return
    traverse_tree(tree.left, lst)
    lst.append(tree.val)
    traverse_tree(tree.right, lst)

def traverse_dll(dll, lst):
    while dll:
        lst.append(dll.val)
        if dll.next:
            assert dll.next.prev == dll
        dll = dll.next

# Welcome to Python. :)  This is a class with no bondage or
# discipline.
#
# It merely give us some syntax sugar for attaching
# attributes.
class Node:
    pass

def create_tree(lst):
    def _maketree(low, high):
        # Making a balanced tree is simply a matter
        # of taking the middle value as the root
        # and recursively building the subtrees
        # on the left and right.
        if low > high:
            return None
        mid = (low + high) / 2
        tree = Node()
        tree.val = lst[mid]
        tree.left = _maketree(low, mid - 1)
        tree.right = _maketree(mid + 1, high)
        return tree
    return _maketree(0, len(lst) - 1)

test()
