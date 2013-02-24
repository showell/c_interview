#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct search_result {
    int found;
    int need;
    int val;
};

struct tree {
    int val;
    struct tree *left;
    struct tree *right;
};

struct search_result nth_biggest(struct tree *tree, int n) {
    struct search_result sr;
    if (!tree) {
        sr.found = 0;
        sr.need = n;
        return sr;
    }
    if (!tree->right) {
        if (n == 1) {
            sr.val = tree->val;
            sr.need = 0;
            sr.found = 1;
        }
        else {
            sr.need = n - 1;
            sr.found = 0;
        }
        return sr;
    }
    sr = nth_biggest(tree->right, n);
    if (sr.found) return sr;
    sr.need -= 1;
    if (sr.need == 0) {
        sr.found = 1;
        sr.val = tree->val;
        return sr;
    }
    return nth_biggest(tree->left, sr.need);
}

struct tree *make_node(int n) {
    struct tree *tree = malloc(sizeof(struct tree));
    tree->left = NULL;
    tree->right = NULL;
    tree->val = n;
    return tree;
}

int main(int argc, char **argv) {
    struct search_result sr;
    struct tree *t1 = make_node(1);
    struct tree *t2 = make_node(2);
    struct tree *t3 = make_node(3);
    struct tree *t4 = make_node(4);
    struct tree *t5 = make_node(5);
    struct tree *t6 = make_node(6);
    t2->left = t1;
    t2->right = t3;
    t4->left = t2;
    t4->right = t5;
    t5->right = t6;
    sr = nth_biggest(t4, 1);
    assert(sr.found && sr.val == 6);
    sr = nth_biggest(t4, 2);
    assert(sr.found && sr.val == 5);
    sr = nth_biggest(t4, 3);
    assert(sr.found && sr.val == 4);
    sr = nth_biggest(t4, 4);
    assert(sr.found && sr.val == 3);
    sr = nth_biggest(t4, 5);
    assert(sr.found && sr.val == 2);
    sr = nth_biggest(t4, 6);
    assert(sr.found && sr.val == 1);
    sr = nth_biggest(t4, 7);
    assert(!sr.found && sr.need == 1);
    sr = nth_biggest(t4, 8);
    assert(!sr.found && sr.need == 2);

    return 0;
}
