def ways_to_make_change(amount, coins):
    # Assumption: coins[0] should be the smallest
    # denomination for optimal performance.
    solution = [0] * len(coins)
    amount_needed = amount
    while True:
        # To generate each new solution, we increase
        # at most one of the denominations and roll
        # the odometer back to zero for any smaller
        # coins.
        which_coin = 0
        while True:
            if coins[which_coin] > amount_needed:
                for i in range(which_coin+1):
                    amount_needed += solution[i] * coins[i]
                    solution[i] = 0
                which_coin += 1
                if which_coin >= len(coins):
                    return
            else:
                if which_coin == 0:
                    coins_needed = amount_needed / coins[which_coin]
                else:
                    coins_needed = 1
                amount_needed -= coins_needed * coins[which_coin]
                solution[which_coin] += coins_needed
                if amount_needed == 0:
                    yield solution
                break

coins = [1, 5, 10, 25]
amount = 27
for solution in ways_to_make_change(amount, coins):
    print solution
