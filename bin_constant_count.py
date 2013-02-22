def incr_bin(num):
    if num[0] is None:
        # 0 -> 1
        num[i] = (1, 1)
        return
    num_bits, bit = num[0]
    if bit == 0:
        num_zeros = num_bits
        if num_zeros == 1:
            # 011 -> 111
            num_ones, _ = num[1]
            num[0] = (num_ones+1, 1)
        else:
            # 0001 -> 1001
            num[0] = (1,1)
            num[1] = (num_zeros-1, 0)
    else:
        num_ones = num_bits
        if num[num_ones] is None:
            # 1111 -> 00001
            num[0] = (num_ones, 0)
            num[num_ones] = (1,1)
        else:
            num_zeros, _ = num[num_ones]
            if num_zeros == 1:
                # 11101111 -> 0001111
                num_higher_ones, _ = num[num_ones+1]
                num[0] = (num_ones, 0)
                num[num_ones] = (num_higher_ones+1, 1)
            else:
                # 1001xxx -> 0101xxx
                num[0] = (num_ones, 0)
                num[num_ones] = (1, 1)
                num[num_ones+1] = (num_zeros-1, 0)

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
