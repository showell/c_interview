#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct node {
    struct node *next;
    char *value;
};
typedef struct node *LIST;

LIST prepend(LIST list, char *s) {
    LIST new_list;
    new_list = malloc(sizeof(*new_list));
    new_list->next = list;
    new_list->value = s;
    return new_list;
}

void debug(LIST list) {
    while (list) {
        printf("%s\n", list->value);
        list = list->next;
    }
}

LIST reverse(LIST list) {
    if (list == NULL) return NULL;
    if (list->next == NULL) return list;
    LIST rest = reverse(list->next);
    list->next->next = list;
    list->next = NULL;
    return rest;
}

int main(int argc, char **argv) {
    LIST list = NULL;
    list = prepend(list, "c");
    list = prepend(list, "b");
    list = prepend(list, "a");
    list = reverse(list);
    debug(list);
    return 0;
}
