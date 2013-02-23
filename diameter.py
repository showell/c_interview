def diameter_height(tree):
    if tree is None: return (0,0)
    left, val, right = tree
    ld, lh = diameter_height(left)
    rd, rh = diameter_height(right)
    d = max([ld, rd, lh+rh+1])
    h = max([lh+1, ld+1])
    return d, h

def diameter(tree):
    d, h = diameter_height(tree)
    return d

assert 0 == diameter(None)
assert 1 == diameter((None, 1, None))
three_node_tree = ((None, 0, None), 1, (None, 2, None))
assert 3 == diameter(three_node_tree)
seven_node_tree = (three_node_tree, 'foo', three_node_tree)
assert 5 == diameter(seven_node_tree)
imbalanced_tree = (seven_node_tree, 'bar', None)
assert 5 == diameter(imbalanced_tree)
