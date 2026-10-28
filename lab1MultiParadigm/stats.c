/*
 * Lab 1: The Multi-Paradigm Tour -- C implementation.
 *
 * Compile: gcc -O2 -o stats_c stats.c
 * Run:     ./stats_c 4 8 15 16 23 42
 *
 * Complete the TODO section. See the assignment,
 * Part B, for the full shared contract (all three language versions
 * must match it exactly, including the tie-breaking mode rule).
 */

#include <stdio.h>
#include <stdlib.h>

int compare_ints(const void *a, const void *b) {
    int int_a = *(const int *)a;
    int int_b = *(const int *)b;
    return (int_a > int_b) - (int_a < int_b);
}

//  argc = argument count   argv = argument values
// if argc less then 2 end program
// .exe is [0]
int main(int argc, char *argv[]) {
    if (argc < 2) {
        return 1;
    }

    int n = argc - 1; //sub 1 from count.(the.exe)
    int *nums = malloc(n * sizeof(int)); //malloc: ask computer to give enough memory to store the "n" interger. For example if the size is 6 then 6x4byte = 24byte allocated
    if (nums == NULL) {
        return 1;
    }
    for (int i = 0; i < n; i++) {
        nums[i] = atoi(argv[i + 1]);
    }

    /* TODO: compute mean, median, and mode from `nums` (length n).
     * - median: for even n, average the two middle values of the SORTED array.
     * - mode: most frequent value; on a tie, the SMALLEST tied value.
     * A sorted copy (via qsort + compare_ints) is useful for the median;
     * a simple O(n^2) frequency count is fine for mode at this input size.
     */
    double mean = 0.0;
    double median = 0.0;
    int mode = 0;

    // for if there is set array
    // int nums[] = {4, 8, 15, 16, 23, 42};
    // sizeof(nums) == 20bytes | int == 4bytes | 5int in array * 4bytes == 20bytes
    // sizeof[0] == 4bytes cuz it the int in the array.

    // always initialize it with something or else its random :(
    int total=0;
    
    // mean
    for (int i = 0; i < n; i++){
        total += nums[i];
    }
    mean = (double)total/n;
    // median
    qsort(nums, n,sizeof(int), compare_ints);
    // for (int i = 0; i < n; i++){
    //     printf("%d\n",nums[i]);
    // }
    if (n % 2 == 0){
        int m1 = nums[n/2];
        int m2 = nums[n/2 - 1];
        median = (m1 + m2)/2.0;
    } else {
        median = nums[n/2];
    }
    
    // mode
    mode = nums[0];
    int commonCount = 1;
    int largestCount = 1;

    for (int i = 1; i < n; i++){
        // printf("%d\n",nums[i]);
        if (nums[i] == nums[i-1]){
            commonCount +=1;
            // printf("common: %d\n", commonCount);
        } else {
            if (commonCount > largestCount){
                largestCount = commonCount;
                mode = nums[i - 1];
            }
            commonCount = 1;
        }
    }

    if (commonCount > largestCount){
        mode = nums[n - 1];
    }

    // printf("common: %d\n", commonCount);
    printf("Mean: %.2f\n", mean);
    printf("Median: %.2f\n", median);
    printf("Mode: %d\n", mode);

    free(nums);
    return 0;
}
