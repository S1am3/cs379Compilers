"""
Lab 1: The Multi-Paradigm Tour -- Python implementation.

Run: python stats.py 4 8 15 16 23 42
Complete compute_stats() below. See the assignment,
Part B, for the full shared contract (all three language versions
must match it exactly).
"""

import sys
from typing import List, Tuple
import statistics


def compute_stats(nums: List[int]) -> Tuple[float, float, int]:
    """
    Return (mean, median, mode).
    - median: for an even count, average the two middle values after sorting.
    - mode: the most frequent value; on a tie, the SMALLEST tied value.
    """
    #4 8 15 16 23 42
    #mean
    length = len(nums)
    getSum = sum(nums)
    mean = getSum/length #18

    #median
    sortNum = sorted(nums)

    if length % 2 == 0:
        m1 = sortNum[length//2]
        m2 = sortNum[length//2 - 1]
        median = (m1 + m2)/2
    else:
        median = sortNum[length//2]
    # 15

    #mode
    m = statistics.multimode(sortNum)
    mode = min(m) #4
    
    return(mean,median, mode)
    # TODO
    


def main() -> int:
    if len(sys.argv) < 2:
        return 1
    nums = [int(a) for a in sys.argv[1:]]
    mean, median, mode = compute_stats(nums)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Mode: {mode}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
