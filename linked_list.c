#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct node {
    struct node *next;
    char *value;
};
typedef struct node *PNODE;

typedef struct {
    PNODE head;
    PNODE tail;
} LIST;

LIST append_node(LIST orig, PNODE new_pnode) {
    LIST list;
    if (orig.head) {
        list.head = orig.head;
        orig.tail->next = new_pnode;
    }
    else {
        list.head = new_pnode;
    }
    list.tail = new_pnode;
    return list;
}

LIST append(LIST orig, char *s) {
    PNODE p;
    p = malloc(sizeof(*p));
    p->next = NULL;
    p->value = s;
    return append_node(orig, p);
}

void debug(PNODE pnode) {
    printf("--\n");
    while (pnode) {
        printf("%s\n", pnode->value);
        pnode = pnode->next;
    }
    printf("--\n");
}

LIST reverse(PNODE pnode) {
    LIST list; 
    if (pnode == NULL) {
        list.head = NULL;
        list.tail = NULL;
        return list;
    }
    if (pnode->next == NULL) {
        list.head = pnode;
        list.tail = pnode;
        return list;
    }
    LIST rest = reverse(pnode->next);
    list.head = rest.head;
    pnode->next->next = pnode;
    pnode->next = NULL;
    list.tail = pnode;
    return rest;
}

LIST concat(LIST list1, LIST list2) {
    if (!list1.head) return list2;
    if (!list2.head) return list1;

    list1.tail->next = list2.head;

    LIST result;
    result.head = list1.head;
    result.tail = list2.tail;
    return result;
}

LIST quicksort(LIST list) {
    if (!list.head) return list;
    PNODE head = list.head;
    char *pivot = head->value;
    LIST smalls;
    smalls.head = NULL;
    smalls.tail = NULL;
    LIST bigs;
    bigs.head = NULL;
    bigs.tail = NULL;
    PNODE p;
    PNODE p_next;

    for (p = head->next; p; p = p_next) {
        p_next = p->next;
        p->next = NULL;

        if (strcmp(p->value, pivot) > 0) {
            bigs = append_node(bigs, p);
        }
        else {
            smalls = append_node(smalls, p);
        }
    }
    head->next = NULL;
    bigs = quicksort(bigs);
    smalls = quicksort(smalls);
    return concat(append_node(smalls, head), bigs);
}


int main(int argc, char **argv) {
    LIST list;
    list.head = NULL;
    list.tail = NULL;
    list = append(list, "a");
    list = append(list, "b");
    list = append(list, "c");
    list = append(list, "d");
    list = append(list, "x");

    LIST list2;
    list2.head = NULL;
    list2.tail = NULL;
    list2 = append(list2, "y");
    list2 = append(list2, "e");
    list2 = append(list2, "f");

    list = concat(list, list2);

    list = reverse(list.head);
    debug(list.head);
    list = quicksort(list);
    debug(list.head);
    return 0;
}
