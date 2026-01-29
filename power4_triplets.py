def enumerate_power_of_4_triplets(until_callback):
    i = 0
    j = 1
    k = 2

    # We compute higher powers of 4 lazily, and k will
    # always be the last index index into the list
    # (i.e. K + 1 == len(powers))
    powers = [1, 4, 16]

    while k < 100:
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

answer = enumerate_power_of_4_triplets(
    until_callback=lambda n: n % 16773121 == 0
)
print(answer)
