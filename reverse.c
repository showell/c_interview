#include <stdio.h>
#include <string.h>

void swap(char *s, int i, int j) {
    char c;

    c = s[i];
    s[i] = s[j];
    s[j] = c;
}

void reverse(char *s) {
    int len = strlen(s);
    int i;

    for (i = 0; i < len; ++i) {
        int other = len - i - 1;
        if (i >= other) break;
        swap(s, i, other);
    }
}

int main(int argc, char **argv) {
    char *s = strdup("hello");
    reverse(s);
    printf("%s\n", s);
    s = strdup("hello6");
    reverse(s);
    printf("%s\n", s);
}
