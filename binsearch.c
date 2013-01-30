#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int search(int *arr, int low, int high, int val) {
    if (high <= low) return -1;
    int mid = (high + low) / 2;
    if (val == arr[mid]) return mid;
    if (val < arr[mid]) return search(arr, low, mid, val);
    return search(arr, mid + 1, high, val);
}

int main(int argc, char **argv) {
    int arr[] = {1, 3, 4, 7, 11, 18};
    int len = 6;
    int i;
    int val;

    for (i = 0; i < len; ++i) {
        val = arr[i];
        printf("%d %d\n", val, search(arr, 0, len, val));
    }
    val = 0; printf("%d %d\n", val, search(arr, 0, len, val));
    val = 10; printf("%d %d\n", val, search(arr, 0, len, val));
    val = 20; printf("%d %d\n", val, search(arr, 0, len, val));

    return 0;
}
