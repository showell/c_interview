#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct search_result {
    int found;
    int val;
};

struct tree {
    int val;
    struct tree *left;
    struct tree *right;
};

struct search_result biggest(struct tree *tree) {
    struct search_result sr;
    if (!tree) {
        sr.found = 0;
        return sr;
    }
    if (tree->right) return biggest(tree->right);
    sr.found = 1;
    sr.val = tree->val;
    return sr;
}

struct search_result successor(struct tree *tree, int val) {
    struct search_result sr_not_found;
    sr_not_found.found = 0;
    if (!tree) {
        return sr_not_found;
    }
    if (tree->val == val) {
        return biggest(tree->left);
    }
    if (tree->val < val) {
        if (!tree->right) return sr_not_found;
        if (tree->right->val == val && !tree->right->left) {
            if (tree->right->val != val) return sr_not_found;
            struct search_result sr;
            sr.found = 1;
            sr.found = 1;
            sr.val = tree->val;
            return sr;
        }
        return successor(tree->right, val);
    }
    else {
        return successor(tree->left, val);
    }
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

    sr = successor(NULL, 3);
    assert(!sr.found);

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

    sr = successor(t1, 1);
    assert(!sr.found);

    sr = successor(t2, 2);
    assert(sr.found && sr.val == 1);

    sr = successor(t2, 3);
    assert(sr.found && sr.val == 2);

    sr = successor(t4, 5);
    assert(sr.found && sr.val == 4);

    sr = successor(t4, 4);
    assert(sr.found && sr.val == 3);

    sr = successor(t4, 3);
    assert(sr.found && sr.val == 2);

    return 0;
}
