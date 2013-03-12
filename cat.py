def test():
    matrix = [
        ['C', 'X', 'T', 'Z'],
        ['X', 'A', 'Y', 'Z'],
        ['W', 'X', 'Q', 'R'],
    ]
    assert [(0,0), (1,1), (0,2)] == find_string(matrix, 'CAT')

def find_string(matrix, s):
    substrings = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            c = matrix[row][col]
            if c == s[0]:
                if len(s) == 1:
                    return [(row, col)]
                substrings.append([(row, col)])
    while substrings:
        substring = substrings.pop()
        row, col = substring[-1]
        deltas = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]
        for rd, cd in deltas:
            rn = row + rd
            cn = col + cd
            if (rn, cn) in substring:
                # don't allow repeats
                continue
            try:
                c = matrix[rn][cn]
            except IndexError:
                continue
            if c != s[len(substring)]:
                continue
            new_substring = substring + [(rn,cn)]
            if len(new_substring) == len(s):
                return new_substring
            substrings.append(new_substring)
    return None
            
test()
