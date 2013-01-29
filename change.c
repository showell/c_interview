#include <stdio.h>
#include <string.h>

void make_change(int amount) {
    int quarters = 0;
    int dimes = 0;
    int nickels = 0;
    int pennies = 0;

    while (amount > 0) {
        if (amount > 25) {
            ++quarters;
            amount -= 25;
        }
        else if (amount > 10) {
            ++dimes;
            amount -= 10;
        }
        else if (amount > 5) {
            ++nickels;
            amount -= 5;
        }
        else {
            ++pennies;
            amount -= 1;
        }
    }
    printf("%d quarters, %d dimes, %d nickels, %d pennies\n",
        quarters,
        dimes,
        nickels,
        pennies
    );
}

int main(int argc, char **argv) {
    make_change(87);
    return 0;
}
