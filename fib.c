#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    int a = 1;
    int b = 1;

    while (a < 1000) {
        printf("%d\n", a);
        int c = a + b;
        a = b;
        b = c;
    }
}
