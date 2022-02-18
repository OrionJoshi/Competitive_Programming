# Method-2

from collections import Counter

def repeatedNTimes(nums):
    count = Counter(nums)
    
    for num in count:
        if count[num] > 1:
            return num

# Time Complexity : O(n)
# Space Complexity : O(n)
    