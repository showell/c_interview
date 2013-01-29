#include <stdio.h>
#include <string.h>

void swap(char *s, int i, int j) {
    char c;

    c = s[i];
    s[i] = s[j];
    s[j] = c;
}

void reverse_word(char *s, int len) {
    int i;

    for (i = 0; i < len; ++i) {
        int other = len - i - 1;
        if (i >= other) break;
        swap(s, i, other);
    }
}

int word_len(char *s) {
    char *t = s;
    while (*t && !isspace(*t)) ++t;
    return t - s;
}

void reverse(char *s) {
    char *orig_s = s;

    while (*s) {
        int len = word_len(s);
        printf("%d\n", len);
        reverse_word(s, len);
        s += len;
        if (*s) ++s;
    }
    reverse_word(orig_s, strlen(orig_s));
}

int main(int argc, char **argv) {
    char *s = strdup("hello newman");
    reverse(s);
    printf("%s\n", s);
    return 0;
}
