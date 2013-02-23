#include <stdlib.h>
#include <stdio.h>

struct prime {
    int n;
    int max_multiple;
};

void sieve_out_multiples(
        int *sieve,
        struct prime *primes,
        int i,
        int n_start,
        int n_end)
{
    int offset;

    while (primes[i].max_multiple < n_end) {
        offset = (primes[i].max_multiple - n_start) / 2;
        sieve[offset] = 1;
        primes[i].max_multiple += 2 * primes[i].n;
    }
}

int count_odd_primes(n) {
    if (n % 2 == 0) --n;

    int chunk_size = 1000; // number of odds
    int n_start = 3;
    int n_end = n_start + 2 * chunk_size;
    if (n_end > n+2) n_end = n+2;
    int cnt = 0;

    chunk_size = (n_end - n_start) / 2;
    int alloc_size = chunk_size; // enough to get started
    struct prime *primes = malloc(alloc_size * sizeof(*primes));
    int *sieve = malloc(chunk_size * sizeof(int));
    int i;

    while (n_start <= n) {
        n_end = n_start + 2 * chunk_size;
        if (n_end > n+2) n_end = n+2;
        chunk_size = (n_end - n_start) / 2;

        for (i = 0; i < chunk_size; ++i) {
            sieve[i] = 0;
        }

        // mark all composities from primes so far
        for (i = 0; i < cnt; ++i) {
            sieve_out_multiples(sieve, primes, i, n_start, n_end);
        }

        for (i = n_start; i < n_end; i += 2) {
            int offset = (i - n_start) / 2;
            if (sieve[offset] == 0) {
                // we found a prime!
                // printf("prime %d\n", i);
                if (cnt >= alloc_size) {
                    alloc_size += chunk_size / 2 + 1;
                    primes = realloc(primes, alloc_size * sizeof(*primes));
                }
                primes[cnt].n = i;
                primes[cnt].max_multiple = 3 * i;
                sieve_out_multiples(sieve, primes, cnt, n_start, n_end);
                ++cnt;
            }
        }
        n_start = n_end;
        if (n_start % 2 == 0) ++n_start;
    }
    return cnt;
}

int count_primes(int n) {
    if (n <= 1) return 0;
    if (n == 2) return 1;
    return count_odd_primes(n) + 1;
}

int main(int argc, char **argv) {
    printf("%d\n", count_primes(100));
    printf("%d\n", count_primes(1000000));
    return 0;
}
