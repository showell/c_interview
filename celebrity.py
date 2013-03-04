def max_by(lst, cmp):
    candidate = 0
    for i in range(1, len(lst)):
        if cmp(lst[candidate], lst[i]) > 0:
            candidate = i
    return lst[candidate]

def find_celebrity(lst):
    # Simplifying assumption: assume the most famous
    # person is indeed a celebrity.
    return max_by(lst, famous_cmp)

def famous_cmp(i, j):
    if know(i, j):
        return 1
    else:
        return -1

def know(i, j):
    # 40 is our celebrity
    if i == 40:
        return False
    if j == 40:
        return True
    # For others, return something
    # predictable
    return  i == j + 10 or i == j - 10

print find_celebrity([10, 20, 30, 40, 50])
