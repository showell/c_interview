#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

struct Node {
    int val;
    struct Node *left;
    struct Node *right;
};
typedef struct Node Node;

struct search_result {
    int need;
    struct Node *node;
};

struct search_result kth_biggest_result(Node *root, int k) {
    struct search_result sr;
    sr.need = k;
    sr.node = NULL;
    if (!root) {
        return sr;
    }
    if (root->right) {
        sr = kth_biggest_result(root->right, k);
        if (sr.need == 0) return sr;
    }
    sr.need -= 1; // root
    if (sr.need == 0) {
        sr.node = root;
        return sr;
    }
    return kth_biggest_result(root->left, sr.need);
}

Node *kth_biggest(Node *root, int k) {
    struct search_result sr;
    sr = kth_biggest_result(root, k);
    return sr.node;
}

Node *make_node(int n) {
    Node *Node = malloc(sizeof(struct Node));
    Node->left = NULL;
    Node->right = NULL;
    Node->val = n;
    return Node;
}

int main(int argc, char **argv) {
    Node *node;
    Node *t1 = make_node(1);
    Node *t2 = make_node(2);
    Node *t3 = make_node(3);
    Node *t4 = make_node(4);
    Node *t5 = make_node(5);
    Node *t6 = make_node(6);
    t2->left = t1;
    t2->right = t3;
    t4->left = t2;
    t4->right = t5;
    t5->right = t6;
    node = kth_biggest(t4, 1);
    assert(node->val == 6);
    node = kth_biggest(t4, 2);
    assert(node->val == 5);
    node = kth_biggest(t4, 3);
    assert(node->val == 4);
    node = kth_biggest(t4, 4);
    assert(node->val == 3);
    node = kth_biggest(t4, 5);
    assert(node->val == 2);
    node = kth_biggest(t4, 6);
    assert(node->val == 1);
    node = kth_biggest(t4, 7);
    assert(!node);
    node = kth_biggest(t4, 8);
    assert(!node);

    return 0;
}
