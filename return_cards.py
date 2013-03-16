def strategy(n):
    # A user draws a card from 1 to 10, and if
    # he doesn't like it, he can return the card
    # for up to n turns.  He acts rationally.
    # Return a tuple of the cards he keeps and
    # his mean expected outcome.
    if n == 0:
        return ([1,2,3,4,5,6,7,8,9,10], 5.5)
    next_keepers, next_outcome = strategy(n-1)

    # This next bit of code could be generalized, but
    # I'm leaving it explicit for clarity.
    if next_outcome < 6:
        return ([6,7,8,9,10], 0.5*8 + 0.5*next_outcome)
    elif next_outcome < 7:
        return ([7,8,9,10], 0.4*8.5 + 0.6*next_outcome)
    elif next_outcome < 8:
        return ([8,9,10], 0.3*9 + 0.7*next_outcome)
    elif next_outcome < 9:
        return ([9,10], 0.2*9.5 + 0.8*next_outcome)
    else:
        return ([10], 0.1*10 + 0.9*next_outcome)

for n in range(10):
    keepers, outcome = strategy(n)
    print n, '%.2f' % outcome, keepers

