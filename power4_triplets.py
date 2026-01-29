def enumerate_power_of_4_triplets(until_callback):
    i = 0
    j = 1
    k = 2

    # We compute higher powers of 4 lazily, and k will
    # always be the last index index into the list
    # (i.e. K + 1 == len(powers))
    powers = [1, 4, 16]

    while k < 200:
        assert k + 1 == len(powers)

        triplet_sum = powers[i] + powers[j] + powers[k]

        # for debugging
        # print(i, j, k, triplet_sum)

        if until_callback(triplet_sum):
            return triplet_sum

        # Our invariant is that i < j < k,
        # and we try to always bump the smallest
        # number we can.
        if i + 1 < j:
            i += 1
        elif j + 1 < k:
            j += 1
            i = 0
        else:
            powers.append(4 * powers[k])
            k += 1
            i = 0
            j = 1

def seek_bad_numbers():
    bad_numbers = set()

    for i in range(2, 50):
        # Skip redundant answers. If 5 doesn't work, neither will
        # 10, 15, 20, etc.
        if any(i % bad_number == 0 for bad_number in bad_numbers):
            continue
        answer = enumerate_power_of_4_triplets(
            until_callback=lambda n: n % i == 0
        )
        if answer is None:
            bad_numbers.add(i)
            print(f"{i} does not seem to divide any triplets")

seek_bad_numbers()
