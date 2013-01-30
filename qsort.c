#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void swap(int *arr, int i, int j) {
    arr[i] = arr[i] ^ arr[j];
    arr[j] = arr[i] ^ arr[j];
    arr[i] = arr[i] ^ arr[j];
}

int partition(int *arr, int low, int high) {
    int mid = low;
    int pivot = arr[high-1];
    int i;

    for (i = low; i < high - 1; ++i) {
        if (arr[i] <= pivot) {
            if (mid < i) swap(arr, i, mid);
            ++mid;
        }
    }
    if (mid < i) swap(arr, i, mid);
    return mid;
}

int quick_sort(int *arr, int low, int high) {
    if (high <= low + 1) return;
    int mid = partition(arr, low, high);
    quick_sort(arr, low, mid);
    quick_sort(arr, mid+1, high);
}

int main(int argc, char **argv) {
    int len = 11;
    int arr[] = {100, -7, 1, 13, 5, 7, 14, -100, 8, 6, 9, 10};
    int i;
    int val;

    quick_sort(arr, 0, len);
    for (i = 0; i < len; ++i) {
        val = arr[i];
        printf("%d\n", val);
    }

    return 0;
}
