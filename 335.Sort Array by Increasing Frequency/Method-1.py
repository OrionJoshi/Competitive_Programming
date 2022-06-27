# Method-1

from collections import Counter

def frequencySort(nums):
    c = Counter(nums)
    nums.sort(reverse=True)
    nums.sort(key=lambda x: c[x])
    
    return nums

# Time Complexity : O(nlogn)
# Space Complexity : O(n)