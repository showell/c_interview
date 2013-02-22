def incr_bin(num, i = 0):
    if num[i] is None:
        num[i] = (1, 1)
        return
    num_bits, bit = num[i]
    if bit == 1:
        num[i] = (num_bits, 0)
        if num[i+num_bits] is None:
            print 'ROLL'
            num[i+num_bits] = (1,1)
        else:
            print 'RECURSE'
            incr_bin(num, i + num_bits)
    else:
        if num_bits == 1:
            num_ones, _ = num[i+1]
            num[i] = (num_ones+1, 1)
        else:
            num[i] = (1,1)
            num[i+1] = (num_bits-1, 0)

numbers = {
    0: [None],
    1: [(1,1), None],
    2: [(1,0), (1,1), None],
    3: [(2,1), None,  None],
    4: [(2,0), None,  (1,1), None],
    5: [(1,1), (1,0), (1,1), None],
    6: [(1,0), (2,1), None,  None],
    7: [(3,1), None,  None,  None],
    8: [(3,0), None,  None,  (1,1), None],
    9: [(1,1), (2,0), None,  (1,1), None],
   10: [(1,0), (1,1), (1,0), (1,1), None],
}

def to_decimal(bin_lst, i=0):
    if bin_lst[i] is None:
        return 0
    result = 0
    num_bits, bit = bin_lst[i]
    if bit == 1:
        result = 2 ** num_bits - 1
    return result + (2 ** num_bits) * to_decimal(bin_lst, i+num_bits)

for k, v in numbers.items():
    assert k == to_decimal(v)

num = [None] * 9 # pre-allocate for 8-bit number
for i in range(256):
    print 'about to verify', i, num
    assert i == to_decimal(num)
    incr_bin(num)
print num
print 'DONE!'
