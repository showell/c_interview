def test():
    test_strings = [
        ('a1b1c1', 'abc'),
        ('a1b3c5', 'abbbccccc'),
        ('a5b3c1', 'aaaaabbbc'),
        ('a5b5c5', 'aaaaabbbbbccccc'),
    ]

    for s, expected_result in test_strings:
        # strings are immutable in Python, so make this a list
        lst = list(s)
        expand(lst)
        assert expected_result == ''.join(lst)

def expand(a):
    # i = input index
    # j = output index
    # In our first pass, we compress the 1s
    # and compute how much space we'll have.
    i = 0
    j = 0
    new_len = 0
    while i < len(a):
        c = a[i]
        cnt = int(a[i+1])
        new_len += cnt
        i += 2
        a[j] = c
        j += 1
        if cnt > 1:
            a[j] = str(cnt)
            j += 1
    # Set the array to correct length.
    while len(a) > new_len:
        a.pop()
    # Note that this is the only place we append
    # to the list.  Everything is in-place, and we
    # have constant storage for the locals: i, j, cnt, new_len.
    while len(a) < new_len:
        a.append(None) 
    # In the second pass, we work backward through
    # the string and write out the final result.  By
    # working backward, we know we'll have room.
    i = j - 1 # last element in compress string
    j = new_len - 1 # where we write
    while i >= 0:
        c = a[i]
        i -= 1
        try:
            cnt = int(c)
            c = a[i]
            i -= 1
        except:
            cnt = 1
        while cnt > 0:
            a[j] = c
            j -= 1
            cnt -= 1

test()
