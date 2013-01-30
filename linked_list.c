#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct node {
    struct node *next;
    char *value;
};
typedef struct node *LIST;

struct result {
    LIST head;
    LIST tail;
};

struct result append(struct result orig, char *s) {
    LIST new_list;
    new_list = malloc(sizeof(*new_list));
    new_list->next = NULL;
    new_list->value = s;
    struct result result;
    if (orig.head) {
        result.head = orig.head;
        result.tail->next = new_list;
    }
    else {
        result.head = new_list;
    }
    result.tail = new_list;
    return result;
}

void debug(LIST list) {
    while (list) {
        printf("%s\n", list->value);
        list = list->next;
    }
}

struct result reverse(LIST list) {
    struct result result; 
    if (list == NULL) {
        result.head = NULL;
        result.tail = NULL;
        return result;
    }
    if (list->next == NULL) {
        result.head = list;
        result.tail = list;
        return result;
    }
    struct result rest = reverse(list->next);
    result.head = rest.head;
    list->next->next = list;
    list->next = NULL;
    result.tail = list;
    return rest;
}

int main(int argc, char **argv) {
    struct result result;
    result.head = NULL;
    result.tail = NULL;
    result = append(result, "a");
    result = append(result, "b");
    result = append(result, "c");
    result = append(result, "d");
    result = reverse(result.head);
    debug(result.head);
    return 0;
}
