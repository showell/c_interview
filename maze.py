# This is an iterative solution for traversing a maze. We try
# to extend our path as long as we can, but then backtrack
# when we hit a dead end or solution.

def solve(maze):
    num_solutions = 0
    traversal = {}
    traversal['directions'] = ''
    traversal['point'] = (0, 0)
    endpoint = (len(maze)-1, len(maze[0])-1)
    forbidden = ''
    while True:
        new_traversal = extend_traversal(maze, traversal, forbidden)
        if not new_traversal:
            if traversal['directions'] == '':
                print 'NO MORE OPTIONS'
                break
            traversal, forbidden = backtrack(maze, traversal)
            continue
        forbidden = ''
        traversal = new_traversal
        r, c = traversal['point']
        if (r, c) == endpoint:
            print 'solution:', traversal['directions']
            num_solutions += 1
    return num_solutions

def extend_traversal(maze, t, forbidden):
    new_t = {}
    r, c = t['point']
    if 'D' not in forbidden:
        if can_go_down(maze, r, c):
            new_t['directions'] = t['directions'] + 'D'
            new_t['point'] = (r+1, c)
            maze[r+1][c] = 2
            return new_t
    if 'U' not in forbidden:
        if can_go_up(maze, r, c):
            new_t['directions'] = t['directions'] + 'U'
            new_t['point'] = (r-1, c)
            maze[r-1][c] = 2
            return new_t
    if 'R' not in forbidden:
        if can_go_right(maze, r, c):
            new_t['directions'] = t['directions'] + 'R'
            new_t['point'] = (r, c+1)
            maze[r][c+1] = 2
            return new_t
    if 'L' not in forbidden:
        if can_go_left(maze, r, c):
            new_t['directions'] = t['directions'] + 'L'
            new_t['point'] = (r, c-1)
            maze[r][c-1] = 2
            return new_t
    return None

def backtrack(maze, t):
    new_t = {}
    last_dir = t['directions'][-1]
    r, c = t['point']
    maze[r][c] = 0
    new_t['directions'] = t['directions'][:-1]
    if last_dir == 'D':
        new_t['point'] = (r-1, c)
        return new_t, 'D'
    if last_dir == 'U':
        new_t['point'] = (r+1, c)
        return new_t, 'DU'
    if last_dir == 'R':
        new_t['point'] = (r, c-1)
        return new_t, 'DUR'
    if last_dir == 'L':
        new_t['point'] = (r, c+1)
        return new_t, 'DURL'

def can_go_left(maze, r, c):
    return c-1 >= 0 and maze[r][c-1] == 0

def can_go_right(maze, r, c):
    return c+1 < len(maze[0]) and maze[r][c+1] == 0

def can_go_down(maze, r, c):
    return r+1 < len(maze) and maze[r+1][c] == 0

def can_go_up(maze, r, c):
    return r-1 >= 0 and maze[r-1][c] == 0

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
]
num_solutions = solve(maze)
print num_solutions

