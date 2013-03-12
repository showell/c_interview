def max_product(a):
    ans = pre_max = pre_min = a[0]
    for elem in a[1:]:
        new_min = pre_min*elem
        new_max = pre_max*elem
        pre_min = min([elem, new_max, new_min])
        pre_max = max([elem, new_max, new_min])
        ans = max([ans, pre_max])
    return ans

assert 0 == max_product([0,0,-2,0,0,0])
assert 8 == max_product([-2,1,1,8])
assert 18 == max_product([-2,-3,1,3])
assert 12 == max_product([-3,-4,0,1,2,3])
assert 720 == max_product([1,-1,10,-8, -9, 0])
assert 2 == max_product([-50, 0.5, 2])
assert 2 == max_product([-50, 2, 0.5])
