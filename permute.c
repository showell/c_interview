#include <stdio.h>
#include <string.h>

void _permute(char *s, char *t) {
    int len = strlen(t);

    if (len == 1) {
        printf("%s\n", s);
        return;
    }

    int i;
    char c = t[0];

    for (i = 0; i < len; ++i) {
        char old_c;
        t[0] = t[i];
        old_c = t[i];
        t[i] = c;
        _permute(s, t+1);
        t[i] = old_c;
        t[0] = c;
    }
}

void permute(char *s) {
    _permute(s, s);
}

int main(int argc, char **argv) {
    char *s = strdup("abc");
    permute(s);
    return 1;
}
