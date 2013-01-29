#include <stdio.h>
#include <string.h>

int is_prime(int n, int *primes, int num_primes) {
    int div;
    int i;

    i = 0;
    while (i < num_primes) {
        div = primes[i]; 
        if (div * div > n) return 1;
        if (n % div == 0) return 0;
        ++i;
    }
}

int main(int argc, char **argv) {
    int i = 0;
    int primes[10];
    int num_primes = 0;

    for (i = 2; num_primes < 10; ++i) {
        if (is_prime(i, primes, num_primes)) {
            printf("%d\n", i);
            primes[num_primes] = i;
            ++num_primes;
        }
    }
    return 0;
}
