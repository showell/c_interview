# Find the longest substring present in two different strings.
# This is kind of an overkill approach.
def test():
    s1 = "cbalaskdfjthe_answerlkounot_quitevo_lajslkj"
    s2 = "alnot_quitesoiuthe_answerjoiunoiuhkbiwi"
    assert "the_answer" ==  match(s1, s2)

def match(s1, s2):
    # This helper function takes a list of indexes
    # in a string and creates a dictionary whose
    # keys are letters and whose values are the
    # list of indexes immediately to the right
    # of occurrences of the letter in s1.
    def build_dict(subt):
        dct = {}
        for i in subt:
            if i < len(s1):
                c = s1[i]
                if c not in dct:
                    dct[c] = []
                dct[c].append(i+1)
        return dct
    # We lazily build a tree of all words in s1.
    # We only go one letter deep until we encounter
    # the letter in s2
    tree = build_dict(range(len(s1)))
    max_word = ''
    for i in range(len(s2)):
        word = ''
        t = tree
        for j in range(i, len(s2)):
            c = s2[j]
            if c not in t:
                break
            word += c
            subt = t[c]
            if type(subt) == list:
                dct = build_dict(subt)
                t[c] = dct
            t = t[c]
        if len(word) > len(max_word):
            max_word = word
    return max_word

test()
