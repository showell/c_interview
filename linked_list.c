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

LIST append(LIST orig, char *s) {
    PNODE new_pnode;
    new_pnode = malloc(sizeof(*new_pnode));
    new_pnode->next = NULL;
    new_pnode->value = s;
    LIST list;
    if (orig.head) {
        list.head = orig.head;
        list.tail->next = new_pnode;
    }
    else {
        list.head = new_pnode;
    }
    list.tail = new_pnode;
    return list;
}

void debug(PNODE pnode) {
    while (pnode) {
        printf("%s\n", pnode->value);
        pnode = pnode->next;
    }
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
    list2 = append(list2, "e");
    list2 = append(list2, "f");

    list = concat(list, list2);

    list = reverse(list.head);
    debug(list.head);
    return 0;
}
