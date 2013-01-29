#include <stdio.h>
#include <string.h>

// GOAL: abcde -> cdeab
// abcde -> d abcae
// -> b adcae
// -> e adcab
// -> c adeab
// -> a cdeab

void rotate(char *s, int offset) {
    int len = strlen(s);
    int i = 0;
    int new_i = i + offset;
    int start = 0;
    int num_loops = 0;

    char c = s[0];


    while (1) {
        new_i = (i + offset) % len;
        char new_c = s[new_i];
        s[new_i] = c;
        c = new_c;
        i = new_i;
        if (i == start) {
            ++start;
            ++i;
            c = s[i];
        }
        if (++num_loops == len) break;
    }
}

int main(int argc, char **argv) {
    char *s = strdup("abcdef");
    rotate(s, 2);
    printf("%s\n", s);
    return 0;
}
