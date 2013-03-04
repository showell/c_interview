def best_string(strings, good_chars):
    # let's assume ascii, and the challenge
    # here is to make finding "good" characters
    # be O(1).
    good_char_lst = [False] * 128
    for c in good_chars:
        good_char_lst[ord(c)] = True
    def goodness(s):
        # In our goodness function use a list
        # so we don't double-count good characters.
        # For small words, the list shouldn't grow
        # unwieldy.
        our_good_chars = []
        for c in s:
            if good_char_lst[ord(c)]:
                if c not in our_good_chars:
                    our_good_chars.append(c)
        return len(our_good_chars)
    # Python has a function that returns
    # the max element in a list using a key
    # function.
    return max(strings, key=goodness)

strings = [
    "apple",
    "banana",
    "carrot",
    "dog",
    'sassy',
    't-rex',
    'yours truly',
    # assume a much bigger dictionary
]

good_chars = ['a', 's', 'x', 'y']
assert 'sassy' == best_string(strings, good_chars)
