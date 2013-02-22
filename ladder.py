import random

class Runner:
    pass

def race(race_results, c1, c2):
    if (c1, c2) in race_results:
        return race_results[(c1, c2)]
    if random.random() < 0.5:
    # if c1 > c2:
        print '%d beats %d' % (c1, c2)
        race_results[(c1, c2)] = c1
        return c1
    else:
        print '%d beats %d' % (c2, c1)
        race_results[(c1, c2)] = c2
        return c2

def race_runners(race_results, runners, low, high):
    if low == high:
        return low, low
    if low + 1 == high:
        winner = race(race_results, low, high)
        if winner == low:
            runners[low].inferior = high
            runners[high].superior = low
            return low, high
        else:
            runners[low].superior = high
            runners[high].inferior = low
            return high, low
    mid = (low + high) / 2
    winner1, loser1 = race_runners(race_results, runners, low, mid)
    winner2, loser2 = race_runners(race_results, runners, mid + 1, high)
    print 'merge:'
    print_chain(runners, winner1)
    print_chain(runners, winner2)
    while winner2 is not None:
        on_deck = runners[winner2].inferior

        # Try to promote the winner of the second division
        # up through the ranks of the first division.
        defeated = None
        victor = None
        loser = loser1
        while loser is not None:
            winner = race(race_results, winner2, loser)
            if winner == winner2:
                defeated = loser
                loser = runners[loser].superior
            else:
                victor = loser
                break

        if defeated is None:
            # winner2 beat nobody, so
            # connect the ladders and we're done
            print 'simple connect'
            runners[loser1].inferior = winner2
            runners[winner2].superior = loser1
            break

        if victor is None:
            # we have a new alpha dog
            runners[defeated].superior = winner2
            runners[winner2].inferior = defeated
            print 'new alpha dog'
            winner1 = winner2
        else:
            # insert our new place
            print 'insertion'
            runners[victor].inferior = winner2
            runners[winner2].superior = victor
            runners[winner2].inferior = defeated
            runners[defeated].superior = winner2

        if on_deck is None:
            # top division loser couldn't hold off anybody
            loser2 = loser1
            break
        runners[on_deck].superior = None
        winner2 = on_deck

    print_chain(runners, winner1)
    return winner1, loser2


def print_chain(runners, head):
    chain = []
    while head is not None:
        chain.append(head)
        next = runners[head].inferior
        if next and runners[next].superior != head:
            print chain
            raise Exception('bad reverse linking')
        head = next
    print 'chain', chain

def ladder(num_runners):
    runners = []
    for i in range(num_runners):
        runner = Runner()
        runner.superior = None
        runner.inferior = None
        runners.append(runner)

    race_results = {}
    winner, loser = race_runners(race_results, runners, 0, num_runners-1)
    print_chain(runners, winner)

def test():
    for i in range(1, 25):
        print '-----'
        ladder(i)

test()
