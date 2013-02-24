# Find the longest substring present in two different strings.
# This is kind of an overkill approach.
def test():
    s1 = "cbalaskdfjthe_answerlkounot_quitevo_lajslkj"
    s2 = "alnot_quitesoiuthe_answerjoiunoiuhkbiwi"
    assert "the_answer" ==  match(s1, s2)

def word_tree(s):
    # build a tree of words in N*N time
    tree = {}
    for i in range(len(s)):
        t = tree
        for j in range(i, len(s)):
            c = s[j]
            if c not in t:
                t[c] = {}
            t = t[c]
    return tree

def match(s1, s2):
    tree = word_tree(s1)
    # find max word in N*M time, where M
    # is average length of matching words
    max_word = ''
    for i in range(len(s2)):
        word = ''
        t = tree
        for j in range(i, len(s2)):
            c = s2[j]
            if c not in t:
                break
            word += c
            t = t[c]
        if len(word) > len(max_word):
            max_word = word
    return max_word

test()
