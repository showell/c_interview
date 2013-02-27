def strategy(pots):
    cache = {}
    def s(i, j):
        # Given: pots from i to j
        # Assuming rational players, return this tuple 
        # to represent your strategy:
        #   only, L, R
        #   how much gold in this pot
        #   1st player bounty
        #   2nd player bounty
        #   rest of the game
        if i == j:
            return ('only', pots[i], pots[i], 0, None)
        if (i,j) in cache:
            return cache[(i,j)]
        l_next = s(i+1, j)
        r_next = s(i, j-1)
        _, _, l1, l2, _ = l_next
        _, _, r1, r2, _ = r_next
        l_outcome = pots[i] + l2
        r_outcome = pots[j] + r2
        if l_outcome > r_outcome:
            result = ('L', pots[i], l_outcome, l1, l_next)
        else:
            result = ('R', pots[j], r_outcome, r1, r_next)
        cache[(i,j)] = result
        return result
    return s(0, len(pots)-1)

pots = [6, 2, 3, 4, 7]
print pots
print strategy(pots)
