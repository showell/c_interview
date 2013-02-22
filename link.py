# You can simulate linked lists in Python with tuples.
# You want the least significant bit to be the head of
# the list.
def test():
    one = (1, None)
    two = (0, (1, None))
    three = (1, (1, None))
    six = (0, (1, (1, None)))
    seven = (1, (1, (1, None)))
    thirteen = (1, (0, (1, (1, None))))
    assert three ==  sum(one, two)
    assert thirteen == sum(six, seven)
    assert 15 == to_decimal(sum(two, sum(six, seven)))

def sum(lst1, lst2, carry=0):
    if lst1 is None and lst2 is None:
        if carry:
            return (1, None)
        else:
            return None
    if lst1 is None:
        b1, lst1 = 0, None
    else:
        b1, lst1 = lst1
    if lst2 is None:
        b2, lst2 = 0, None
    else:
        b2, lst2 = lst2
    b = b1 + b2 + carry
    if b >= 2:
        return (b-2, sum(lst1, lst2, 1))
    else:
        return (b, sum(lst1, lst2, 0))
    
def to_decimal(lst):
    if lst is None:
        return 0
    b, rest = lst
    return b + 2 * to_decimal(rest)

test()
